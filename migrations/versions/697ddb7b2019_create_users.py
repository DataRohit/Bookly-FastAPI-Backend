"""create_users

Revision ID: 697ddb7b2019
Revises: 
Create Date: 2024-10-08 09:16:58.217768

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "697ddb7b2019"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("uid", sa.UUID(), nullable=False),
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("username", sa.VARCHAR(), nullable=False),
        sa.Column("email", sa.VARCHAR(), nullable=False),
        sa.Column("first_name", sa.VARCHAR(), nullable=False),
        sa.Column("last_name", sa.VARCHAR(), nullable=False),
        sa.Column("role", sa.VARCHAR(), server_default="user", nullable=False),
        sa.Column("is_verified", sa.BOOLEAN(), nullable=False),
        sa.Column("is_active", sa.BOOLEAN(), nullable=False),
        sa.Column("hashed_password", sa.VARCHAR(), nullable=False),
        sa.Column("created_at", postgresql.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", postgresql.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint("uid"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("username"),
    )


def downgrade() -> None:
    op.drop_table("users")
