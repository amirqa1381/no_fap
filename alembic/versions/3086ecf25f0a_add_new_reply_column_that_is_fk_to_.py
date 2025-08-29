"""Add new reply column that is FK to Comment

Revision ID: 3086ecf25f0a
Revises: de3f75a192a7
Create Date: 2025-08-29 09:08:37.787335
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3086ecf25f0a"
down_revision: Union[str, Sequence[str], None] = "de3f75a192a7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.add_column(sa.Column("reply", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "fk_comments_reply_comments",  # give it a name
            "comments",
            ["reply"],
            ["comment_id"],
            ondelete="CASCADE",
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("comments", schema=None) as batch_op:
        batch_op.drop_constraint("fk_comments_reply_comments", type_="foreignkey")
        batch_op.drop_column("reply")
