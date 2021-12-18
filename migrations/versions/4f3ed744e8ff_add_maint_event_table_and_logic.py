"""add maint event table and logic

Revision ID: 4f3ed744e8ff
Revises: 57898188e7e9
Create Date: 2021-12-13 10:01:19.797018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f3ed744e8ff'
down_revision = '57898188e7e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maintenance_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('photo_url', sa.String(length=255), nullable=True),
    sa.Column('create_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('status', sa.Enum('pending', 'approved', 'rejected', name='state'), nullable=False),
    sa.Column('home_owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['home_owner_id'], ['home_owner.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('maintenance_event')
    # ### end Alembic commands ###