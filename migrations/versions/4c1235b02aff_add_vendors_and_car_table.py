"""add vendors and car table

Revision ID: 4c1235b02aff
Revises: d7709e205b2a
Create Date: 2021-12-18 16:22:17.249605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c1235b02aff'
down_revision = 'd7709e205b2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vendors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('registration_plate', sa.String(length=10), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('home_owner_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('home_owner_manager_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['home_owner_id'], ['home_owner.id'], ),
    sa.ForeignKeyConstraint(['home_owner_manager_id'], ['home_owner_manager.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('registration_plate')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle')
    op.drop_table('vendors')
    # ### end Alembic commands ###
