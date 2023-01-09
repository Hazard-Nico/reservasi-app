"""tambah detail meja dengan update meja table

Revision ID: e7c3862d42cf
Revises: 53e7e591fe52
Create Date: 2023-01-08 06:56:31.956780

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e7c3862d42cf'
down_revision = '53e7e591fe52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meja', schema=None) as batch_op:
        batch_op.add_column(sa.Column('no_meja', sa.BigInteger(), nullable=False))
        batch_op.drop_column('bentuk')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meja', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bentuk', mysql.TEXT(), nullable=True))
        batch_op.drop_column('no_meja')

    # ### end Alembic commands ###