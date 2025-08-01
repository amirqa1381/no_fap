from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from database.db_connection import get_db
from database.actions.user_action import create_user, get_all_users, get_specific_user
from schemas.user_schema import UserResponse, UserBase

router = APIRouter(prefix="/user", tags=["user"])




@router.post("/", response_model=UserResponse)
async def create_user_route(request: UserBase,db: Session = Depends(get_db)):
    return create_user(db=db, request=request)


@router.get("/all", response_model=list[UserResponse])
async def get_all_users_route(db:Session = Depends(get_db)):
    """
    This function is for getting the all the users
    """
    return get_all_users(db=db)



@router.get("/specific-user/{user_id}", response_model=UserResponse)
async def get_specific_user_route(user_id: int, db:Session = Depends(get_db)):
    """
    this function is for getting the specific user
    Args:
        user_id (int): path parameter that user will be insert
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        UserResponse: Response model that we have
    """
    return get_specific_user(db=db, id=user_id)