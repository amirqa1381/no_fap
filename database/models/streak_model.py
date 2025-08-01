from __future__ import annotations
from typing import TYPE_CHECKING
from database.db_connection import Base
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

if TYPE_CHECKING:
    from database.models.user_model import User


class Streak(Base):
    """
    Tracks the current and past streaks of each user.

    Args:
        Base (declarative_base): inherits from SQLAlchemy's Base class to create a declarative model.
    """

    __tablename__ = "streaks"

    streak_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False
    )
    start_date: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    relapsed: Mapped[bool] = mapped_column(default=False)

    # refrencing to the user part
    user: Mapped["User"] = relationship(back_populates="streaks")
