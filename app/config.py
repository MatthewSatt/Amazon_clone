import os

environment = os.environ.get('FLASK_ENV')


def _database_url():
    url = os.environ.get('DATABASE_URL', 'postgresql://localhost/amazon_clone')
    # SQLAlchemy 1.4+ only accepts the 'postgresql' scheme, but some hosts
    # (Heroku, older Render) still hand out 'postgres://'
    return url.replace('postgres://', 'postgresql://', 1)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        if environment == 'production':
            raise RuntimeError('SECRET_KEY must be set in production')
        SECRET_KEY = 'dev-secret-key-change-me'

    SQLALCHEMY_DATABASE_URI = _database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.environ.get('SQLALCHEMY_ECHO', '').lower() in ('1', 'true')

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = environment == 'production'

    # CSRF tokens live as long as the session instead of expiring after an hour
    WTF_CSRF_TIME_LIMIT = None
