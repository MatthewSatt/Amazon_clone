from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import ForeignKey, func


class Product(db.Model):
    __tablename__ = 'products'

    id=db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)
    name=db.Column(db.String(255), nullable=False)
    description=db.Column(db.String(2000), nullable=False)
    price=db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


    review = db.relationship("Review", back_populates="product", cascade="all, delete")
    type = db.relationship("Type", back_populates="product")
    cart = db.relationship("Cart", back_populates='product', cascade='all, delete')


    def to_dict(self):
        return {
            'id': self.id,
            'type_id': self.type_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
