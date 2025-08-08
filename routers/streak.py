from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from schemas.streak_schema import StreakBase, StreakResponse
from database.db_connection import get_db
from database.actions.streak_action import create_streak


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