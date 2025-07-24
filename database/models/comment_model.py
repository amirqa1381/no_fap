from database.db_connection import Base
from sqlalchemy import Integer, String, DateTime, func, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, mapper, relationship, validates
from datetime import datetime
from database.models.user_model import User
from database.models.post_model import Post



class Comment(Base):
	"""
	Comments on forum posts.
	"""
	__tablename__ = "comments"

	comment_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
	post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.post_id"), nullable=False)
	user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
	title:Mapped[str] = mapped_column(String(255))
	content: Mapped[str] = mapped_column(String(500), name="Content")
	created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

	post: Mapped["Post"] = relationship(back_populates="comments")
	user: Mapped["User"] = relationship(back_populates="comments")