"""create accounts

Revision ID: 329a29d17ced
Revises:
Create Date: 2022-10-24 21:21:11.613656

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "329a29d17ced"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "accounts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nickname", sa.Unicode(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("accounts")
