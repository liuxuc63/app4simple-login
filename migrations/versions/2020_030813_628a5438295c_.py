"""empty message

Revision ID: 628a5438295c
Revises: 235355381f53
Create Date: 2020-03-08 13:07:13.312858

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '628a5438295c'
down_revision = '235355381f53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mailbox', sa.Column('pgp_finger_print', sa.String(length=512), nullable=True))
    op.add_column('mailbox', sa.Column('pgp_public_key', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('can_use_pgp', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'can_use_pgp')
    op.drop_column('mailbox', 'pgp_public_key')
    op.drop_column('mailbox', 'pgp_finger_print')
    # ### end Alembic commands ###
