"""users table

Revision ID: 9d3fd9168698
Revises: 
Create Date: 2018-03-11 16:59:53.784841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d3fd9168698'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_city'), 'user', ['city'], unique=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('top_artists',
    sa.Column('spotify_username', sa.String(length=64), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('top_artists', sa.Text(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('spotify_username')
    )
    op.create_index(op.f('ix_top_artists_timestamp'), 'top_artists', ['timestamp'], unique=False)
    op.create_index(op.f('ix_top_artists_top_artists'), 'top_artists', ['top_artists'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_top_artists_top_artists'), table_name='top_artists')
    op.drop_index(op.f('ix_top_artists_timestamp'), table_name='top_artists')
    op.drop_table('top_artists')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_city'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
