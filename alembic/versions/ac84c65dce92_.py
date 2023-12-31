"""empty message

Revision ID: ac84c65dce92
Revises: b2715552a7ea
Create Date: 2023-09-20 01:41:43.295109

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'ac84c65dce92'
down_revision: Union[str, None] = 'b2715552a7ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'genders',
        sa.Column('pk', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('pk')
    )
    op.create_table(
        'languages',
        sa.Column('pk', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('pk')
    )
    op.add_column(
        'users', sa.Column('language_id', sa.Integer(), nullable=True),
    )
    op.add_column('users', sa.Column('gender_id', sa.Integer(), nullable=True))
    op.alter_column(
        'users', 'city_id', existing_type=sa.INTEGER(), nullable=True,
    )
    op.create_foreign_key(None, 'users', 'genders', ['gender_id'], ['pk'])
    op.create_foreign_key(None, 'users', 'languages', ['language_id'], ['pk'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.alter_column(
        'users', 'city_id', existing_type=sa.INTEGER(), nullable=False,
    )
    op.drop_column('users', 'gender_id')
    op.drop_column('users', 'language_id')
    op.drop_table('languages')
    op.drop_table('genders')
    # ### end Alembic commands ###
