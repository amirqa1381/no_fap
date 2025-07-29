from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from database.db_connection import get_db
from database.actions.user_action import create_user
from schemas.user_schema import UserResponse, UserBase

router = APIRouter(prefix="/user", tags=["user"])




@router.post("/", response_model=UserResponse)
async def create_user_route(request: UserBase,db: Session = Depends(get_db)):
    return create_user(db=db, request=request)
