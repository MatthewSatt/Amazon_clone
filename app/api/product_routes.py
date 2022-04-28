from flask import Blueprint, jsonify, request
from app.models import db, Product
from flask_login import login_required


product_routes = Blueprint("products", __name__)


@product_routes.route('/all')
def get_all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@product_routes.route("/<int:typeId>")
def product_types(typeId):
    products = Product.query.filter(Product.type_id == typeId)
    return jsonify([product.to_dict() for product in products])

@product_routes.route("/delete/<int:id>",  methods=['DELETE'])
@login_required
def delete_product(id):
    product = Product.query.filter(Product.id == id).first()
    db.session.delete(product)
    db.session.commit()
    return product.to_dict()
