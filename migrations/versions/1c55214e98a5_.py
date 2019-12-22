"""empty message

Revision ID: 1c55214e98a5
Revises: cf95695636c4
Create Date: 2019-09-26 21:53:02.432656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c55214e98a5'
down_revision = 'cf95695636c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('time', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'time')
    # ### end Alembic commands ###