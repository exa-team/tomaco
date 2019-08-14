"""Create interval table and adjust user.email constraint

Revision ID: 707e0f9d6222
Revises: c8849ee391cc
Create Date: 2019-08-14 21:18:13.775465

"""
from alembic import op
import sqlalchemy_utils
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "707e0f9d6222"
down_revision = "c8849ee391cc"
branch_labels = None
depends_on = None


def upgrade():
    TYPES = (("break", "Break"), ("pomodoro", "Pomodoro"))

    op.create_table(
        "interval",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("finished_at", sa.DateTime(), nullable=False),
        sa.Column(
            "type", sqlalchemy_utils.types.choice.ChoiceType(TYPES), nullable=False
        ),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.alter_column("user", "email", existing_type=sa.VARCHAR(), nullable=False)


def downgrade():
    op.alter_column("user", "email", existing_type=sa.VARCHAR(), nullable=True)
    op.drop_table("interval")
