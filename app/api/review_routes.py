from flask import Blueprint, jsonify, request
from app.models import db, Product
from flask_login import login_required



review_routes = Blueprint("reviews", __name__)


# @review_routes.route('/all')
# @login_required
# def get_all_products():
#     products = Product.query.all()

#     print(product.to_dict() for product in products)


#     return jsonify([product.to_dict() for product in products])
