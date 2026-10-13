from flask import Blueprint
from flask_login import current_user, login_required

from app.models import Cart, Product, db
from app.pricing import MAX_QUANTITY, summarize

from .utils import as_int, error, json_body

cart_routes = Blueprint('carts', __name__)


def cart_response(status=200):
    """The signed-in user's whole cart, with product details and totals"""
    items = db.session.scalars(
        db.select(Cart).where(Cart.user_id == current_user.id).order_by(Cart.id)).all()
    return {
        'items': [{**item.to_dict(), 'product': item.product.to_dict(full=False)} for item in items],
        'summary': summarize(
            [(item.product.price, item.quantity) for item in items], current_user.isPrime),
    }, status


def valid_quantity(value):
    quantity = as_int(value)
    return quantity if quantity is not None and 1 <= quantity <= MAX_QUANTITY else None


@cart_routes.route('/')
@login_required
def get_cart():
    return cart_response()


@cart_routes.route('/', methods=['POST'])
@login_required
def add_to_cart():
    """Add a product, or increase its quantity if it's already in the cart"""
    data = json_body()
    product_id = as_int(data.get('productId'))
    quantity = valid_quantity(data.get('quantity', 1))
    if quantity is None:
        return error(f'Choose a quantity from 1 to {MAX_QUANTITY}.')
    if product_id is None or not db.session.get(Product, product_id):
        return error('Product not found.', 404)

    item = db.session.scalar(
        db.select(Cart).where(Cart.user_id == current_user.id, Cart.product_id == product_id))
    if item:
        item.quantity = min(item.quantity + quantity, MAX_QUANTITY)
    else:
        db.session.add(Cart(user_id=current_user.id, product_id=product_id, quantity=quantity))
    db.session.commit()
    return cart_response(201)


def own_item(id):
    item = db.session.get(Cart, id)
    if not item or item.user_id != current_user.id:
        return None
    return item


@cart_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_quantity(id):
    item = own_item(id)
    if not item:
        return error('Cart item not found.', 404)
    quantity = valid_quantity(json_body().get('quantity'))
    if quantity is None:
        return error(f'Choose a quantity from 1 to {MAX_QUANTITY}.')
    item.quantity = quantity
    db.session.commit()
    return cart_response()


@cart_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def remove_from_cart(id):
    item = own_item(id)
    if not item:
        return error('Cart item not found.', 404)
    db.session.delete(item)
    db.session.commit()
    return cart_response()
