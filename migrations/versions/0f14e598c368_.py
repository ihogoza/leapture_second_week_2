"""empty message

Revision ID: 0f14e598c368
Revises: 726f329b2990
Create Date: 2022-03-04 07:26:54.015780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f14e598c368'
down_revision = '726f329b2990'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('role', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'role')
    # ### end Alembic commands ###
