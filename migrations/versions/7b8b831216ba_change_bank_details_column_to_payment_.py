"""change bank_details column to payment_provider_id

Revision ID: 7b8b831216ba
Revises: 14bd0544facf
Create Date: 2021-12-22 11:08:41.447328

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7b8b831216ba'
down_revision = '14bd0544facf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('home_owner', sa.Column('payment_provider_id', sa.String(length=255), nullable=False))
    op.drop_column('home_owner', 'bank_details')
    op.add_column('home_owner_manager', sa.Column('stripe_id', sa.Enum('card', 'alipay', 'sepa_debit', name='paymentmethodtype'), nullable=False))
    op.drop_column('home_owner_manager', 'payment_method')
    op.drop_column('home_owner_manager', 'bank_details')
    op.add_column('users', sa.Column('payment_provider_id', sa.String(length=255), nullable=False))
    op.drop_column('users', 'bank_details')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bank_details', sa.VARCHAR(length=25), autoincrement=False, nullable=False))
    op.drop_column('users', 'payment_provider_id')
    op.add_column('home_owner_manager', sa.Column('bank_details', sa.VARCHAR(length=25), autoincrement=False, nullable=False))
    op.add_column('home_owner_manager', sa.Column('payment_method', postgresql.ENUM('card', 'alipay', 'sepa_debit', name='paymentmethodtype'), autoincrement=False, nullable=False))
    op.drop_column('home_owner_manager', 'stripe_id')
    op.add_column('home_owner', sa.Column('bank_details', sa.VARCHAR(length=25), autoincrement=False, nullable=False))
    op.drop_column('home_owner', 'payment_provider_id')
    # ### end Alembic commands ###
