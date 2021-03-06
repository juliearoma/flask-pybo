"""empty message

Revision ID: 692a8acd0cdd
Revises: f9de9efa00ca
Create Date: 2021-08-26 12:49:12.473955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '692a8acd0cdd'
down_revision = 'f9de9efa00ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###
