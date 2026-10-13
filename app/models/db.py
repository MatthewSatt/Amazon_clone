import os

from flask_sqlalchemy import SQLAlchemy

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get('SCHEMA')

db = SQLAlchemy()


# In production every table lives in SCHEMA (see migrations/env.py),
# so foreign keys need the schema prefix too
def add_prefix_for_prod(attr):
    if environment == "production":
        return f"{SCHEMA}.{attr}"
    return attr


def isoformat(value):
    return value.isoformat() if value else None


def qualified(table):
    """Table name including the schema when running in production"""
    return f"{SCHEMA}.{table}" if environment == "production" else table
