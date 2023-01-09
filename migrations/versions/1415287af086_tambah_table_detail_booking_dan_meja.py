"""tambah table detail_booking dan meja

Revision ID: 1415287af086
Revises: 2d00ff6c143a
Create Date: 2023-01-05 11:17:06.856952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1415287af086'
down_revision = '2d00ff6c143a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('detail_booking',
    sa.Column('id_detail', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('id_booking', sa.BigInteger(), nullable=False),
    sa.Column('id_meja', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id_detail')
    )
    op.create_table('meja',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('slot_kursi', sa.Integer(), nullable=False),
    sa.Column('bentuk', sa.Text(), nullable=True),
    sa.Column('tipe_meja', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meja')
    op.drop_table('detail_booking')
    # ### end Alembic commands ###