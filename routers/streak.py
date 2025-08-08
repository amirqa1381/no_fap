from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm.session import Session
from schemas.streak_schema import StreakBase, StreakResponse
from database.db_connection import get_db
from database.models.streak_model import Streak
from database.actions.streak_action import create_streak,get_all_user_streaks, get_streak_by_id, delete_streak
from services.streak_service import calculate_streak_days


router = APIRouter(prefix="/streak", tags=["streak"])



@router.post("/new", response_model=StreakResponse, status_code=status.HTTP_201_CREATED)
async def create_streak_route(request: StreakBase, db: Session = Depends(get_db)):
    """
    Endpoint to create a new streak for a user.

    Args:
        request (StreakBase): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).
    """
    return create_streak(db, request)


@router.get("/calculate_days/{streak_id}", response_model=int, status_code=status.HTTP_200_OK)
async def calculate_streak_days_route(streak_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to calculate the number of days in a streak.

    Args:
        streak_id (int): ID of the streak to calculate days for.
        db (Session, optional): Defaults to Depends(get_db).
    """
    streak = db.query(Streak).filter(Streak.streak_id == streak_id).first()
    if not streak:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Streak not found")
    
    return calculate_streak_days(streak)


# get all streaks for a user
@router.get("/user/{user_id}", response_model=list[StreakResponse], status_code=status.HTTP_200_OK)
async def get_all_streaks_for_user_route(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all streaks for a user.

    Args:
        user_id (int): ID of the user to retrieve streaks for.
        db (Session, optional): Defaults to Depends(get_db).
    """
    return get_all_user_streaks(db, user_id)


# get specific streak by ID
@router.get("/{streak_id}", response_model=StreakResponse, status_code=status.HTTP_200_OK)
async def get_streak_by_id_route(streak_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve a streak by its ID.

    Args:
        streak_id (int): ID of the streak to retrieve.
        db (Session, optional): Defaults to Depends(get_db).
    """
    return get_streak_by_id(db, streak_id)



# delete streak by ID
@router.delete("/{streak_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_streak_by_id_route(streak_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete a streak by its ID.

    Args:
        streak_id (int): ID of the streak to delete.
        db (Session, optional): Defaults to Depends(get_db).
    """
    return delete_streak(db, streak_id)