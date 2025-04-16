"""Add resume builder tables

Revision ID: a53aa48881cf
Revises: 4420809520bf
Create Date: 2025-04-15 20:51:10.762248

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a53aa48881cf'
down_revision = '4420809520bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='likes_post_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='likes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='likes_pkey')
    )
    # ### end Alembic commands ###
