from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from database.models.streak_model import Streak
from schemas.streak_schema import StreakBase, StreakResponse



def create_streak(db:Session, request: StreakBase) -> StreakResponse:
    """
    Function to create a new streak for a user.
    """
    new_streak = Streak(
        user_id=request.user_id,
        start_date=request.start_date,
        end_date=request.end_date,
        relapsed=request.relapsed
    )

    db.add(new_streak)
    db.commit()
    db.refresh(new_streak)
    
    return StreakResponse(
        streak_id=new_streak.streak_id,
        user_id=new_streak.user_id,
        start_date=new_streak.start_date,
        end_date=new_streak.end_date,
        relapsed=new_streak.relapsed
    )