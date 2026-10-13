from flask.cli import AppGroup
from sqlalchemy import text

from app.models.db import db, qualified

from .products import seed_products, undo_products
from .users import seed_users, undo_users
from .types import seed_types, undo_types
from .reviews import seed_reviews, undo_reviews
from .cart import seed_carts, undo_carts
from .order import seed_orders, undo_orders

# `flask seed --help`
seed_commands = AppGroup('seed')

TABLES = ['users', 'types', 'products', 'reviews', 'carts', 'orders']


# `flask seed all` wipes the tables first, so it's safe to run repeatedly
@seed_commands.command('all')
def seed():
    for table in TABLES:
        db.session.execute(text(f'TRUNCATE {qualified(table)} RESTART IDENTITY CASCADE;'))
    db.session.commit()

    seed_users()
    seed_types()
    seed_products()
    seed_reviews()
    seed_carts()
    seed_orders()


# `flask seed undo`
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_products()
    undo_types()
    undo_reviews()
    undo_carts()
    undo_orders()
