from flask.cli import AppGroup

from .products import seed_products, undo_products
from .users import seed_users, undo_users
from .types import seed_types, undo_types
from .reviews import seed_reviews, undo_reviews
from .cart import seed_carts, undo_carts
from .order import seed_orders, undo_orders
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_types()
    seed_products()
    seed_reviews()
    seed_carts()
    seed_orders()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_products()
    undo_types()
    undo_reviews()
    undo_carts()
    undo_orders()
    # Add other undo functions here
