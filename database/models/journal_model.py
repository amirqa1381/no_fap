from database.db_connection import Base
from sqlalchemy import Integer, String, DateTime, func, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from datetime import datetime
from database.models.user_model import User


class Journal(Base):
    """
    Daily check-ins or reflections.

    Args:
        Base (declarative_base): inherits from SQLAlchemy's Base class to create a declarative model.
    """
    
    __tablename__ = "journals"
    
    journal_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False)
    entry_date: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    mood_rating: Mapped[int] = mapped_column(Integer, CheckConstraint('mood_rating >= 1 AND mood_rating <= 10'), nullable=False)
    
    # refrencing to the user part
    user: Mapped["User"] = relationship(back_populates="journals")
    
    @validates('mood_rating')
    def validate_mood_rating(self, value):
        if not (1 <= value <= 10):
            raise ValueError("Mood rating must be between 1 and 10.")
        return value