"""empty message

Revision ID: adb99ad2c2c9
Revises: ccbc5a2a9b0a
Create Date: 2022-04-09 12:25:10.888572

"""
from alembic import op
import sqlalchemy as sa
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = 'adb99ad2c2c9'
down_revision = 'ccbc5a2a9b0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'image')
    # ### end Alembic commands ###
