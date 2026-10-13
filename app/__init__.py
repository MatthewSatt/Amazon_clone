import os

from flask import Flask, jsonify, redirect, request
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFError, CSRFProtect, generate_csrf

from .api.auth_routes import auth_routes
from .api.cart_routes import cart_routes
from .api.order_routes import order_routes
from .api.product_routes import product_routes
from .api.review_routes import review_routes
from .api.type_routes import type_routes
from .api.user_routes import user_routes
from .config import Config
from .models import User, db
from .seeds import seed_commands

DIST_DIR = os.path.join(os.path.dirname(__file__), '..', 'react-app', 'dist')
IS_PRODUCTION = os.environ.get('FLASK_ENV') == 'production'

app = Flask(__name__, static_folder=DIST_DIR, static_url_path='/')
app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)
csrf = CSRFProtect(app)

login = LoginManager(app)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


@login.unauthorized_handler
def unauthorized():
    return jsonify(errors={'form': ['You must be signed in.']}), 401


app.cli.add_command(seed_commands)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(type_routes, url_prefix='/api/types')
app.register_blueprint(product_routes, url_prefix='/api/products')
app.register_blueprint(review_routes, url_prefix='/api/reviews')
app.register_blueprint(cart_routes, url_prefix='/api/carts')
app.register_blueprint(order_routes, url_prefix='/api/orders')


@app.route('/api/health')
def health():
    return {'status': 'ok'}


# Hosts like Heroku terminate TLS in front of us, so redirect plain-http
# requests (as reported by the proxy) to https in production.
@app.before_request
def https_redirect():
    if IS_PRODUCTION and request.headers.get('X-Forwarded-Proto') == 'http':
        return redirect(request.url.replace('http://', 'https://', 1), code=301)


# The React app reads this cookie and echoes it back in the X-CSRFToken header
@app.after_request
def inject_csrf_token(response):
    if response.mimetype in ('application/json', 'text/html'):
        response.set_cookie(
            'csrf_token',
            generate_csrf(),
            secure=IS_PRODUCTION,
            samesite='Lax',
            httponly=False)
    if request.path.startswith('/api/'):
        response.headers['Cache-Control'] = 'no-store'
    elif request.path.startswith('/assets/'):
        # Vite fingerprints everything in /assets
        response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    return response


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.errorhandler(CSRFError)
def csrf_error(e):
    return jsonify(errors={'form': ['Your session expired. Please refresh the page.']}), 400


@app.errorhandler(404)
def not_found(e):
    if request.path.startswith('/api/'):
        return jsonify(errors={'form': ['Not found.']}), 404
    # The static route catches every file path, so anything unknown here is a
    # client-side route (e.g. a refreshed /orders): let React Router handle it
    if os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return app.send_static_file('index.html')
    return e


@app.errorhandler(405)
def method_not_allowed(e):
    if request.path.startswith('/api/'):
        return jsonify(errors={'form': ['Method not allowed.']}), 405
    return e


@app.errorhandler(500)
def server_error(e):
    if request.path.startswith('/api/'):
        return jsonify(errors={'form': ['Something went wrong. Please try again.']}), 500
    return e
