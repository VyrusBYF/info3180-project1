"""empty message

Revision ID: 54357aeca082
Revises: 221b71f19678
Create Date: 2020-04-11 19:29:54.525927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54357aeca082'
down_revision = '221b71f19678'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('profiles_email_key', 'profiles', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('profiles_email_key', 'profiles', ['email'])
    # ### end Alembic commands ###