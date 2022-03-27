from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    user = db.relationship("User", back_populates="product")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'price': self.price,
            'rating': self.rating,
            'userId': self.userId
        }
