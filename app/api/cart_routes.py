from flask import Blueprint, jsonify, request
from app.models import db, Product, Cart, User
from flask_login import login_required


cart_routes = Blueprint("carts", __name__)

#passing in id of user
@cart_routes.route('/<int:userId>')
def user_cart_products(userId):
    cart_items = Cart.query.filter(Cart.user_id == userId).all()
    user_items = []
    for item in cart_items:
        user_product = Product.query.filter(Product.id == item.product_id).first()
        user_items.append(user_product.to_dict())
    return {"cart_product": user_items}


@cart_routes.route('/delete/<int:productId>', methods=["DELETE"])
def user_cart_delete(productId):
    cart_item = Cart.query.filter(Cart.product_id == productId).first()
    db.session.delete(cart_item)
    db.session.commit()
    return cart_item.to_dict()


# @cart_routes.route('/add', methods=["POST"])
# def user_cart_add():
#     data = {"productId": 1, }
#     data = request.json
#     product_id = data['productId']
#     user_id = data['userId']
#     product = Product.query.get(product_id)
#     return {"productId": product_id}
