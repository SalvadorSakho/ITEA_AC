"""empty message

Revision ID: 5fb6af3e3fc2
Revises: ef84eaa7bbd1
Create Date: 2020-03-15 22:30:15.103585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fb6af3e3fc2'
down_revision = 'ef84eaa7bbd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'like_count')
    op.drop_column('post', 'dislike_count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('dislike_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('like_count', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
