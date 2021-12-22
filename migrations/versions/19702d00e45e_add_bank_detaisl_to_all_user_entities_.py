"""add bank detaisl to all user entities, create payment table

Revision ID: 19702d00e45e
Revises: f5a7cb7c1961
Create Date: 2021-12-21 17:12:47.957214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19702d00e45e'
down_revision = 'f5a7cb7c1961'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('role', sa.Enum('user', 'home_owner', 'home_owner_manager', 'admin', name='roletype'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('home_owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('role', sa.Enum('user', 'home_owner', 'home_owner_manager', 'admin', name='roletype'), nullable=False),
    sa.Column('bank_details', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('home_owner_manager',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('role', sa.Enum('user', 'home_owner', 'home_owner_manager', 'admin', name='roletype'), nullable=False),
    sa.Column('payment_method', sa.Enum('card', 'alipay', 'sepa_debit', name='paymentmethodtype'), nullable=False),
    sa.Column('bank_details', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('role', sa.Enum('user', 'home_owner', 'home_owner_manager', 'admin', name='roletype'), nullable=False),
    sa.Column('payment_method', sa.Enum('card', 'alipay', 'sepa_debit', name='paymentmethodtype'), nullable=False),
    sa.Column('bank_details', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('maintenance_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('photo_url', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('pending', 'closed', 'raised', name='state'), nullable=False),
    sa.Column('home_owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['home_owner_id'], ['home_owner.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'vehicle', 'home_owner_manager', ['home_owner_manager_id'], ['id'])
    op.create_foreign_key(None, 'vehicle', 'home_owner', ['home_owner_id'], ['id'])
    op.create_foreign_key(None, 'vehicle', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vehicle', type_='foreignkey')
    op.drop_constraint(None, 'vehicle', type_='foreignkey')
    op.drop_constraint(None, 'vehicle', type_='foreignkey')
    op.drop_table('maintenance_event')
    op.drop_table('users')
    op.drop_table('home_owner_manager')
    op.drop_table('home_owner')
    op.drop_table('admins')
    # ### end Alembic commands ###
