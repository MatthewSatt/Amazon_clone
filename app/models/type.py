from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import ForeignKey, func


class Type(db.Model):
    __tablename__ = 'types'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), nullable=False)
    product = db.relationship("Product", back_populates="type")
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
