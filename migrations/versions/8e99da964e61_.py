"""empty message

Revision ID: 8e99da964e61
Revises: adb99ad2c2c9
Create Date: 2022-04-29 22:47:35.024490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e99da964e61'
down_revision = 'adb99ad2c2c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('isPrime', sa.Boolean(create_constraint=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'isPrime')
    # ### end Alembic commands ###
