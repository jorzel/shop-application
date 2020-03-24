"""Removed UserOauth table and added -type- column to User

Revision ID: 89f84998844c
Revises: 34d746638238
Create Date: 2020-03-24 22:08:54.708122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89f84998844c'
down_revision = '34d746638238'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_oauth')
    op.add_column('user', sa.Column('type', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'type')
    op.create_table('user_oauth',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('picture', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('role', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_oauth_pkey'),
    sa.UniqueConstraint('email', name='user_oauth_email_key'),
    sa.UniqueConstraint('username', name='user_oauth_username_key')
    )
    # ### end Alembic commands ###
