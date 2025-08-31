from __future__ import annotations
from typing import TYPE_CHECKING
from database.db_connection import Base
from sqlalchemy import Integer, String, DateTime, func, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from datetime import datetime

if TYPE_CHECKING:
    from database.models.user_model import User
    from database.models.post_model import Post


class Comment(Base):
    """
    Comments on forum posts.
    """

    __tablename__ = "comments"

    comment_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    reply: Mapped[int] = mapped_column(
        Integer, ForeignKey("comments.comment_id", ondelete="CASCADE"), nullable=True
    )
    post_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("posts.post_id", ondelete="CASCADE"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(String(500), name="Content")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    post: Mapped["Post"] = relationship(back_populates="comments")
    user: Mapped["User"] = relationship(back_populates="comments")

    # parent side
    parent: Mapped["Comment"] = relationship(
        "Comment", remote_side=[comment_id], back_populates="replies"
    )

    # replies side
    replies: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="parent",
        single_parent=True,
        cascade="all, delete-orphan",
        order_by="Comment.created_at",
    )
