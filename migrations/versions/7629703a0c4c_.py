"""empty message

Revision ID: 7629703a0c4c
Revises: 
Create Date: 2019-01-30 14:16:49.076278

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7629703a0c4c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('bodies', sa.Text(), nullable=False))
    op.drop_column('message', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('body', mysql.TEXT(), nullable=False))
    op.drop_column('message', 'bodies')
    # ### end Alembic commands ###
