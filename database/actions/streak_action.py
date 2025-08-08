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
    
    
    
def get_streak_by_id(db: Session, streak_id: int) -> StreakResponse:
    """
    Function to retrieve a streak by its ID.

    Args:
        db (Session): Database session.
        streak_id (int): ID of the streak to retrieve.

    Returns:
        StreakResponse: Response model containing the streak details.
    """
    streak = db.query(Streak).filter(Streak.streak_id == streak_id).first()
    if not streak:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Streak not found")
    
    return StreakResponse(
        streak_id=streak.streak_id,
        user_id=streak.user_id,
        start_date=streak.start_date,
        end_date=streak.end_date,
        relapsed=streak.relapsed
    )
    
    
def get_all_user_streaks(db: Session, user_id: int) -> list[StreakResponse]:
    """
    Function to retrieve all streaks for a user.

    Args:
        db (Session): Database session.
        user_id (int): ID of the user whose streaks are to be retrieved.

    Returns:
        list[StreakResponse]: List of streaks associated with the user.
    """
    streaks = db.query(Streak).filter(Streak.user_id == user_id).all()
    
    return [StreakResponse(
        streak_id=streak.streak_id,
        user_id=streak.user_id,
        start_date=streak.start_date,
        end_date=streak.end_date,
        relapsed=streak.relapsed
    ) for streak in streaks]
    

def delete_streak(db: Session, streak_id: int):
    """
    Function to delete a streak by its ID.

    Args:
        db (Session): Database session.
        streak_id (int): ID of the streak to delete.

    Raises:
        HTTPException: If the streak is not found.
    """
    streak = db.query(Streak).filter(Streak.streak_id == streak_id).first()
    if not streak:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Streak not found")
    
    db.delete(streak)
    db.commit()
    return {"detail": "Streak deleted successfully"}