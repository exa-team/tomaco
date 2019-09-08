"""Set the email column as nullable

Revision ID: d5ba963e97fd
Revises: 7d0aea032eac
Create Date: 2019-09-08 15:57:39.781235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d5ba963e97fd"
down_revision = "7d0aea032eac"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("user", "email", existing_type=sa.VARCHAR(), nullable=True)


def downgrade():
    op.alter_column("user", "email", existing_type=sa.VARCHAR(), nullable=False)
