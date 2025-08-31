from __future__ import annotations
from typing import TYPE_CHECKING
from database.db_connection import Base
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


if TYPE_CHECKING:
    from database.models.user_model import User


class Achievement(Base):
    """
    This model is for defining the different achivements with different badge
    """

    __tablename__ = "achivements"

    achivenet_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    days_required: Mapped[int] = mapped_column(Integer)

    users: Mapped["UserAchievement"] = relationship(
        back_populates="achivement", cascade="all, delete-orphan"
    )


class UserAchievement(Base):
    """
    This class is for connecting the achivement class with user class for collecting those
    """

    __tablename__ = "user_achievements"
    ua_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id", ondelete="CASCADE")
    )
    achivement_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("achivements.achivenet_id", ondelete="CASCADE")
    )
    unlocked_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    user: Mapped["User"] = relationship(back_populates="achivements")
    achivement: Mapped["Achievement"] = relationship(back_populates="users")
