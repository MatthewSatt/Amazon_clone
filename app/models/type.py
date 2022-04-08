from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import ForeignKey, func


class Type(db.Model):
    __tablename__ = 'types'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), nullable=False)


    product = db.relationship("Product", back_populates="type")



    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
