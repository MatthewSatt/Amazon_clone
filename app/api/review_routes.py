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
