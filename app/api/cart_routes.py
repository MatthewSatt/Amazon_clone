from flask import Blueprint, jsonify, request
from app.models import db, Product, Cart, User
from flask_login import login_required


cart_routes = Blueprint("carts", __name__)

#passing in id of user
@cart_routes.route('/<int:userId>')
def user_cart_products(userId):
    cart_items = Cart.query.filter(Cart.user_id == userId).all()
    return jsonify([cart.to_dict() for cart in cart_items])


@cart_routes.route('/delete/<int:id>', methods=["DELETE"])
def user_cart_delete(id):
    cart_item = Cart.query.get(id)
    db.session.delete(cart_item)
    db.session.commit()
    return cart_item.to_dict()



@cart_routes.route('/add', methods=["POST"])
def user_cart_add():
    # data = {"productId": 1, }
    data = request.json
    product_id = data['productId']
    user_id = data['userId']
    quantity = data['quantity']
    product = Product.query.get(product_id)

    cart_item = Cart(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity,
    )

    db.session.add(cart_item)
    db.session.commit()

    return {"product": product.to_dict()}
