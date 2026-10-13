from flask import Blueprint, jsonify, request
from sqlalchemy import func

from app.models import Product, Review, db

from .utils import as_int, error

product_routes = Blueprint('products', __name__)


def rated_products(*conditions):
    """(Product, average rating, review count) rows"""
    stats = (
        db.select(
            Review.product_id,
            func.avg(Review.rating).label('rating'),
            func.count(Review.id).label('count'))
        .group_by(Review.product_id)
        .subquery())
    return db.session.execute(
        db.select(Product, stats.c.rating, stats.c.count)
        .outerjoin(stats, Product.id == stats.c.product_id)
        .where(*conditions)
        .order_by(Product.id)).all()


@product_routes.route('/')
def get_products():
    """All products (descriptions shortened). Optional ?type_id= and ?q= filters."""
    conditions = []
    type_id = as_int(request.args.get('type_id'))
    if type_id is not None:
        conditions.append(Product.type_id == type_id)
    query = request.args.get('q', '').strip()
    if query:
        conditions.append(Product.name.ilike(f'%{query}%'))
    rows = rated_products(*conditions)
    return jsonify([
        product.to_dict(rating, count or 0, full=False)
        for product, rating, count in rows])


@product_routes.route('/<int:id>')
def get_product(id):
    rows = rated_products(Product.id == id)
    if not rows:
        return error('Product not found.', 404)
    product, rating, count = rows[0]
    return product.to_dict(rating, count or 0)
