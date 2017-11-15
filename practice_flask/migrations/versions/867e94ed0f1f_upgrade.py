"""upgrade

Revision ID: 867e94ed0f1f
Revises: fb2f16b38147
Create Date: 2017-11-12 22:38:41.248801

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '867e94ed0f1f'
down_revision = 'fb2f16b38147'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_roles_default', table_name='roles')
    op.drop_column('roles', 'default')
    op.drop_column('roles', 'permissions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('permissions', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('roles', sa.Column('default', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.create_index('ix_roles_default', 'roles', ['default'], unique=False)
    # ### end Alembic commands ###
