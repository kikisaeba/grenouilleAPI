"""1/ Initial simple database.

Revision ID: d8c97ac97e6c
Revises: None
Create Date: 2017-09-13 04:18:32.293966

"""

# revision identifiers, used by Alembic.
revision = 'd8c97ac97e6c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('nickname', sa.String(), server_default='Anonymous', nullable=False),
    sa.Column('nickname_verified', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('avatar', sa.String(), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_refresh_token',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'refresh_token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_refresh_token')
    op.drop_table('user')
    # ### end Alembic commands ###