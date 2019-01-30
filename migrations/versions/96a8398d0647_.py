"""empty message

Revision ID: 96a8398d0647
Revises: 7629703a0c4c
Create Date: 2019-01-30 14:17:17.785259

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '96a8398d0647'
down_revision = '7629703a0c4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('body', sa.Text(), nullable=False))
    op.drop_column('message', 'bodies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('bodies', mysql.TEXT(), nullable=False))
    op.drop_column('message', 'body')
    # ### end Alembic commands ###