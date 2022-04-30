from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, db

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route("/prime/<int:id>", methods=["PUT"])
@login_required
def set_prime(id):
    user = User.query.get(id)
    if(user.isPrime == False):
        user.isPrime = True
    elif(user.isPrime == True):
        user.isPrime = False
    db.session.commit()
    return user.to_dict()
