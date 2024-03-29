"""menambah booking table

Revision ID: 98af243c1c25
Revises: 0e4cf30ed691
Create Date: 2023-01-05 10:54:47.561725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98af243c1c25'
down_revision = '0e4cf30ed691'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('id_booking', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.Column('jam_mulai', sa.DateTime(), nullable=True),
    sa.Column('jam_akhir', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id_booking')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    # ### end Alembic commands ###
