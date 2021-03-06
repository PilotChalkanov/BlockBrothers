"""add type of subscription

Revision ID: b07abcc98ad7
Revises: 85fef974e13e
Create Date: 2021-12-23 10:22:40.927394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b07abcc98ad7'
down_revision = '85fef974e13e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscription', sa.Column('type', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subscription', 'type')
    # ### end Alembic commands ###
