"""empty message

Revision ID: 7561b5b26dea
Revises: 15bbe69411cc
Create Date: 2019-12-07 22:06:56.949212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7561b5b26dea'
down_revision = '15bbe69411cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # op.add_column('product', sa.Column('quantity', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'quantity')
    # ### end Alembic commands ###
