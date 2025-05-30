"""Add game_user Association Table

Revision ID: 1c39e55bd048
Revises: 0103ea2f2e15
Create Date: 2025-05-26 23:24:49.310638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c39e55bd048'
down_revision = '0103ea2f2e15'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_users',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_game_users_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_game_users_user_id_users')),
    sa.PrimaryKeyConstraint('game_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_users')
    # ### end Alembic commands ###
