from flask import Blueprint, jsonify, request
from app.models import db, Order, Cart
from flask_login import login_required


order_routes = Blueprint("orders", __name__)


@order_routes.route('/<int:userId>')
def get_user_orders(userId):
    orders = Order.query.filter(Order.user_id == userId)
    return jsonify([order.to_dict() for order in orders])

@order_routes.route("/add", methods=["POST"])
def product_types():
    data = request.json
    old_cart = data["submitOrder"]
    orders = []

    for obj in old_cart:
        cart_id = obj["id"]
        user_id = obj["user_id"]
        product_id = obj["product_id"]
        cart_item = Cart.query.get(cart_id)
        new_order = Order(user_id=user_id, product_id=product_id)
        orders.append(new_order)
        db.session.add(new_order)
        db.session.delete(cart_item)
        db.session.commit()
    # return jsonify([product.to_dict() for product in products])
    return {}



# {'created_at': 'Mon, 02 May 2022 22:08:40 GMT', 'id': 21, 'product_id': 1, 'quantity': 1, 'updated_at': 'Mon, 02 May 2022 22:08:40 GMT', 'user_id': 1}
