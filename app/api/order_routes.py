from flask import Blueprint, jsonify, request
from app.models import db, Product
from flask_login import login_required


order_routes = Blueprint("orders", __name__)


@order_routes.route('/')
def get_user_orders():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

# @order_routes.route("/<int:typeId>")
# def product_types(typeId):
#     products = Product.query.filter(Product.type_id == typeId)
#     return jsonify([product.to_dict() for product in products])
