from flask import Blueprint, jsonify, request
from app.models import db, Type
from flask_login import login_required


type_routes = Blueprint("types", __name__)


@type_routes.route('/all')
def get_all_types():
    types = Type.query.all()
    return jsonify([type.to_dict() for type in types])
