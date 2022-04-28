from itertools import product
import re
from flask import Blueprint, jsonify, request
from app.models import db, Review, review
from flask_login import login_required



review_routes = Blueprint("reviews", __name__)


@review_routes.route("/<int:id>")
def getReviews(id):
    reviews = Review.query.filter(id == Review.product_id).all()
    return jsonify([review.to_dict() for review in reviews])


@review_routes.route("/add", methods=["POST"])
@login_required
def add_review():
    data = request.json
    user_id = data["user_id"]
    product_id = data["product_id"]
    title= data["title"]
    body= data["body"]
    rating=data["rating"]
    new_review = Review(user_id=user_id, product_id=product_id, title=title, body=body, rating=rating)
    db.session.add(new_review)
    db.session.commit()
    return new_review.to_dict()

@review_routes.route("/delete/<int:id>", methods=["DELETE"])
@login_required
def delete_review(id):
    deleted_review = Review.query.filter(Review.id == id).first()
    db.session.delete(deleted_review)
    db.session.commit()
    return deleted_review.to_dict()

@review_routes.route("/edit", methods=["PUT"])
@login_required
def edit_review():
    data = request.json
    review = Review.query.get(data['id'])
    review.title = data['title']
    review.body = data['body']
    review.rating = data['rating']
    db.session.commit()
    return review.to_dict()
