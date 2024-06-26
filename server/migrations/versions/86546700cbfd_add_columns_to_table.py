"""add columns to table

Revision ID: 86546700cbfd
Revises: 8c9e66cb009b
Create Date: 2024-04-10 21:44:28.233681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86546700cbfd'
down_revision = '8c9e66cb009b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
