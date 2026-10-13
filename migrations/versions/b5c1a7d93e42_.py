"""orders: record quantity and the price paid

Revision ID: b5c1a7d93e42
Revises: 013554297838
Create Date: 2026-10-13 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = 'b5c1a7d93e42'
down_revision = '013554297838'
branch_labels = None
depends_on = None

# In production the tables live in their own schema
schema = SCHEMA if environment == "production" else None
prefix = f"{SCHEMA}." if schema else ""


def upgrade():
    op.add_column('orders', sa.Column('quantity', sa.Integer(), nullable=False, server_default='1'), schema=schema)
    op.add_column('orders', sa.Column('price', sa.Float(), nullable=True), schema=schema)
    # Existing orders were paid at the product's current price
    op.execute(
        f"UPDATE {prefix}orders SET price = {prefix}products.price "
        f"FROM {prefix}products WHERE {prefix}products.id = {prefix}orders.product_id")


def downgrade():
    op.drop_column('orders', 'price', schema=schema)
    op.drop_column('orders', 'quantity', schema=schema)
