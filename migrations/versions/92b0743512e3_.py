"""empty message

Revision ID: 92b0743512e3
Revises: 0f14e598c368
Create Date: 2022-03-04 08:18:53.865685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92b0743512e3'
down_revision = '0f14e598c368'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('lastname', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'lastname')
    # ### end Alembic commands ###
