"""add field phone to all users

Revision ID: f5e1515692cb
Revises: 4f3ed744e8ff
Create Date: 2021-12-13 10:05:21.148442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5e1515692cb'
down_revision = '4f3ed744e8ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins', sa.Column('phone', sa.String(length=13), nullable=False))
    op.add_column('home_owner', sa.Column('phone', sa.String(length=13), nullable=False))
    op.add_column('home_owner_manager', sa.Column('phone', sa.String(length=13), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('home_owner_manager', 'phone')
    op.drop_column('home_owner', 'phone')
    op.drop_column('admins', 'phone')
    # ### end Alembic commands ###
