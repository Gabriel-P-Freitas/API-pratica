"""criando a tabela do recurso Phone para a API

Revision ID: d8729bdf9944
Revises: 
Create Date: 2024-08-04 22:00:14.426665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8729bdf9944'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phones',
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('ram_memory', sa.Integer(), nullable=True),
    sa.Column('storage', sa.Integer(), nullable=True),
    sa.Column('chipset', sa.String(length=20), nullable=True),
    sa.Column('battery', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('phones')
    # ### end Alembic commands ###
