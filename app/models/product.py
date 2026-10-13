from .db import db, environment, SCHEMA, add_prefix_for_prod, isoformat
from sqlalchemy import func


def _excerpt(text, length=160):
    return text if len(text) <= length else text[:length].rstrip() + '…'


class Product(db.Model):
    __tablename__ = 'products'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('types.id')), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    review = db.relationship("Review", back_populates="product", cascade="all, delete")
    type = db.relationship("Type", back_populates="product")
    cart = db.relationship("Cart", back_populates='product', cascade='all, delete')
    order = db.relationship("Order", back_populates='product')

    def to_dict(self, rating=None, review_count=0, full=True):
        return {
            'id': self.id,
            'type_id': self.type_id,
            'name': self.name,
            'description': self.description if full else _excerpt(self.description),
            'price': self.price,
            'image': self.image,
            'rating': round(float(rating), 2) if rating is not None else None,
            'review_count': review_count,
            'created_at': isoformat(self.created_at),
            'updated_at': isoformat(self.updated_at)
        }
