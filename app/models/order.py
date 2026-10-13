from .db import db, environment, SCHEMA, add_prefix_for_prod, isoformat
from sqlalchemy import func


class Order(db.Model):
    __tablename__ = 'orders'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1, server_default='1')
    # Unit price at the time of purchase, so later price changes don't rewrite history
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    user = db.relationship("User", back_populates="order")
    product = db.relationship("Product", back_populates="order")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': self.price if self.price is not None else self.product.price,
            'created_at': isoformat(self.created_at),
            'updated_at': isoformat(self.updated_at)
        }
