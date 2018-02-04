"""2/ Add winner slot to Game

Revision ID: 03745d9649bb
Revises: b0b1f904d165
Create Date: 2018-02-04 18:00:35.250715

"""

# revision identifiers, used by Alembic.
revision = '03745d9649bb'
down_revision = 'b0b1f904d165'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('winner', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game', 'winner')
    # ### end Alembic commands ###
