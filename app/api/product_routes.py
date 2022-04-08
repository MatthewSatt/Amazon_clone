from flask import Blueprint, jsonify, request
from app.models import db, Product
from flask_login import login_required


product_routes = Blueprint("products", __name__)


@product_routes.route('/all')
def get_all_products():
    products = Product.query.all()

    print(product.to_dict() for product in products)


    return jsonify([product.to_dict() for product in products])
