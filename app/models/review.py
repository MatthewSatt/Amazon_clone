from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey, func


class Review(db.Model):
    __tablename__ = 'reviews'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    title=db.Column(db.String(255), nullable=False)
    body=db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    user = db.relationship("User", back_populates="review")
    product = db.relationship("Product", back_populates="review")



    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'title': self.title,
            'body': self.body,
            'rating': self.rating,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
