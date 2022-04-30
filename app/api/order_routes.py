from flask import Blueprint, jsonify, request
from app.models import db, Order
from flask_login import login_required


order_routes = Blueprint("orders", __name__)


@order_routes.route('/<int:userId>')
def get_user_orders(userId):
    orders = Order.query.filter(Order.user_id == userId)
    return jsonify([order.to_dict() for order in orders])

# @order_routes.route("/<int:typeId>")
# def product_types(typeId):
#     products = Product.query.filter(Product.type_id == typeId)
#     return jsonify([product.to_dict() for product in products])
