from flask import Blueprint, jsonify
from flask_login import current_user, login_required

from app.models import Cart, Order, db
from app.pricing import summarize

from .utils import error

order_routes = Blueprint('orders', __name__)


def order_json(order):
    return {**order.to_dict(), 'product': order.product.to_dict(full=False)}


@order_routes.route('/')
@login_required
def get_orders():
    orders = db.session.scalars(
        db.select(Order)
        .where(Order.user_id == current_user.id)
        .order_by(Order.created_at.desc(), Order.id.desc()))
    return jsonify([order_json(order) for order in orders])


@order_routes.route('/', methods=['POST'])
@login_required
def place_order():
    """Turn the signed-in user's cart into orders, priced at today's prices"""
    items = db.session.scalars(
        db.select(Cart).where(Cart.user_id == current_user.id).order_by(Cart.id)).all()
    if not items:
        return error('Your cart is empty.')

    summary = summarize(
        [(item.product.price, item.quantity) for item in items], current_user.isPrime)
    orders = []
    for item in items:
        order = Order(
            user_id=current_user.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price)
        orders.append(order)
        db.session.add(order)
        db.session.delete(item)
    db.session.commit()
    return {'orders': [order_json(order) for order in orders], 'summary': summary}, 201
