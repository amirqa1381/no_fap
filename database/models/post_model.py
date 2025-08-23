from __future__ import annotations
from typing import TYPE_CHECKING
from database.db_connection import Base
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from database.models.comment_model import Comment

if TYPE_CHECKING:
    from database.models.user_model import User


class Post(Base):
    """
    For a community/forum-style interaction.
    """

    __tablename__ = "posts"

    post_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(String(500), name="Content")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    # refrence to the user
    user: Mapped["User"] = relationship(back_populates="posts")
    # refrence to the comment
    comments: Mapped[list["Comment"]] = relationship(
        back_populates="post", cascade="all, delete-orphan"
    )
