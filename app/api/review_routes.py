from flask import Blueprint, jsonify
from flask_login import current_user, login_required

from app.models import Product, Review, db

from .utils import as_int, error, json_body

review_routes = Blueprint('reviews', __name__)


def clean_review(data):
    """(fields, errors) from a request body"""
    title = str(data.get('title') or '').strip()
    body = str(data.get('body') or '').strip()
    rating = as_int(data.get('rating'))
    errors = {}
    if not 1 <= len(title) <= 255:
        errors['title'] = ['Add a headline (up to 255 characters).']
    if not 1 <= len(body) <= 5000:
        errors['body'] = ['Write a review (up to 5000 characters).']
    if rating is None or not 1 <= rating <= 5:
        errors['rating'] = ['Choose a rating from 1 to 5 stars.']
    return {'title': title, 'body': body, 'rating': rating}, errors


@review_routes.route('/product/<int:product_id>')
def get_reviews(product_id):
    reviews = db.session.scalars(
        db.select(Review)
        .where(Review.product_id == product_id)
        .order_by(Review.created_at.desc(), Review.id.desc()))
    return jsonify([review.to_dict() for review in reviews])


@review_routes.route('/product/<int:product_id>', methods=['POST'])
@login_required
def add_review(product_id):
    if not db.session.get(Product, product_id):
        return error('Product not found.', 404)
    already_reviewed = db.session.scalar(
        db.select(Review.id).where(
            Review.product_id == product_id, Review.user_id == current_user.id))
    if already_reviewed:
        return error('You have already reviewed this product. Edit your review instead.', 409)

    fields, errors = clean_review(json_body())
    if errors:
        return jsonify(errors=errors), 400

    review = Review(user_id=current_user.id, product_id=product_id, **fields)
    db.session.add(review)
    db.session.commit()
    return review.to_dict(), 201


def own_review(id):
    review = db.session.get(Review, id)
    if not review:
        return None, error('Review not found.', 404)
    if review.user_id != current_user.id:
        return None, error('You can only change your own reviews.', 403)
    return review, None


@review_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_review(id):
    review, problem = own_review(id)
    if problem:
        return problem
    fields, errors = clean_review(json_body())
    if errors:
        return jsonify(errors=errors), 400
    for name, value in fields.items():
        setattr(review, name, value)
    db.session.commit()
    return review.to_dict()


@review_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_review(id):
    review, problem = own_review(id)
    if problem:
        return problem
    db.session.delete(review)
    db.session.commit()
    return {'id': id}
