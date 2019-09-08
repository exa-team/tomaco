"""Add username column

Revision ID: 7d0aea032eac
Revises: 707e0f9d6222
Create Date: 2019-09-08 15:45:18.985125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7d0aea032eac"
down_revision = "707e0f9d6222"
branch_labels = None
depends_on = None

# custom types, used by our data migration.
user_helper = sa.Table(
    "user",
    sa.MetaData(),
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("email", sa.String(), nullable=False),
    sa.Column("username", sa.String(), nullable=True),
)


def upgrade():
    connection = op.get_bind()

    op.add_column("user", sa.Column("username", sa.String(), nullable=True))

    for user in connection.execute(user_helper.select()):
        if not user.email:
            continue

        username, _ = user.email.split("@")
        connection.execute(
            user_helper.update()
            .where(user_helper.c.id == user.id)
            .values(username=username)
        )

    op.alter_column("user", "username", nullable=False)
    op.create_unique_constraint("uq_user_username", "user", ["username"])


def downgrade():
    op.drop_column("user", "username")
