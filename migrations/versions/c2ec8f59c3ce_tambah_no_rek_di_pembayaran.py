"""tambah no_rek di pembayaran

Revision ID: c2ec8f59c3ce
Revises: 9002123fa30e
Create Date: 2023-01-09 16:26:13.338745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2ec8f59c3ce'
down_revision = '9002123fa30e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pembayaran',
    sa.Column('id_pembayaran', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('no_rek', sa.Text(), nullable=True),
    sa.Column('jenis_pembayaran', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_pembayaran')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pembayaran')
    # ### end Alembic commands ###
