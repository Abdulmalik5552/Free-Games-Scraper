"""Adding game table

Revision ID: 1b0042fb25ca
Revises: 
Create Date: 2022-09-03 11:49:45.063545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b0042fb25ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('is_free_now', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_game_end_date'), 'game', ['end_date'], unique=False)
    op.create_index(op.f('ix_game_id'), 'game', ['id'], unique=False)
    op.create_index(op.f('ix_game_start_date'), 'game', ['start_date'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_game_start_date'), table_name='game')
    op.drop_index(op.f('ix_game_id'), table_name='game')
    op.drop_index(op.f('ix_game_end_date'), table_name='game')
    op.drop_table('game')
    # ### end Alembic commands ###
