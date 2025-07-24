from re import Pattern
from database.db_connection import Base
from sqlalchemy import ForeignKey, Integer, String, DateTime, func, Enum, true
from sqlalchemy.orm import Mapped, MapperEvents, mapped_column, relationship
from datetime import datetime
import enum
from database.models.streak_model import Streak
from database.models.journal_model import Journal
from database.models.post_model import Post
from database.models.comment_model import Comment


class User(Base):
    """
    User model for the application.

        Args:
            Base (declarative_base): inherits from SQLAlchemy's Base class to create a declarative model.
    """

    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=True)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    last_login: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    # refrence to the other models
    streaks: Mapped[list["Streak"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    journals: Mapped[list["Journal"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    comments: Mapped[list["Comment"]] = relationship(
        back_populates="post", cascade="all, delete-orphan"
    )
    sent_requests: Mapped["AccountabilityPartner"] = relationship(
        foreign_keys="AccountabilityPartner.user_id",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    received_requests: Mapped["AccountabilityPartner"] = relationship(
        foreign_keys="AccountabilityPartner.partner_id",
        back_populates="partner",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class PartnerStatus(enum.Enum):
    """
    enumaration part
    """

    pending = "pending"
    accepted = "accepted"
    declined = "declined"


class AccountabilityPartner(Base):
    """
    Optional user-to-user accountability pairing.
    """

    __tablename__ = "accountability_partners"

    acc_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False
    )
    partner_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False
    )
    status: Mapped[str] = mapped_column(
        Enum(PartnerStatus), nullable=False, default=PartnerStatus.pending
    )
    requested_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    # relationships
    user: Mapped["User"] = relationship(
        foreign_keys=[user_id], back_populates="sent_requests"
    )
    partner: Mapped["User"] = relationship(
        foreign_keys=[partner_id], back_populates="received_requests"
    )
