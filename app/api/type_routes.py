from flask import Blueprint, jsonify

from app.models import Type, db

type_routes = Blueprint('types', __name__)


@type_routes.route('/')
def get_all_types():
    types = db.session.scalars(db.select(Type).order_by(Type.id))
    return jsonify([type.to_dict() for type in types])
