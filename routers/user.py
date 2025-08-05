from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from database.db_connection import get_db
from database.actions.user_action import (
    create_user,
    get_all_users,
    get_specific_user,
    update_specific_user,
    get_user_by_username,
)
from auth.hashing import verify_password
from auth.security import create_access_token
from schemas.user_schema import UserResponse, UserBase, UserUpdateBasicBase

router = APIRouter(prefix="/user", tags=["user"])


# create user instance
@router.post("/", response_model=UserResponse)
async def create_user_route(request: UserBase, db: Session = Depends(get_db)):
    """
    Function for creating a user instance

    Args:
        request (UserBase): schema for creating the user
        db (Session, optional): Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    return create_user(db=db, request=request)


# getting user instances
@router.get("/all", response_model=list[UserResponse])
async def get_all_users_route(db: Session = Depends(get_db)):
    """
    This function is for getting the all the users
    """
    return get_all_users(db=db)


@router.get("/specific-user/{user_id}", response_model=UserResponse)
async def get_specific_user_route(user_id: int, db: Session = Depends(get_db)):
    """
    this function is for getting the specific user
    Args:
        user_id (int): path parameter that user will be insert
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        UserResponse: Response model that we have
    """
    return get_specific_user(db=db, id=user_id)


# updating the user instances


@router.put("/update/{user_id}", response_model=UserResponse)
async def update_user_route(
    user_id: int, request: UserUpdateBasicBase, db: Session = Depends(get_db)
):
    """
    This function is for updating the specific user
    Args:
        user_id (int): _id of the user that we want to update
        request (UserUpdateBasicBase): schema for updating the user
        db (Session, optional): Defaults to Depends(get_db).
    """
    return update_specific_user(id=user_id, db=db, request=request)


# login user
@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Function for login user and getting the access token

    Args:
        form_data (OAuth2PasswordRequestForm, optional): Defaults to Depends().
        db (Session, optional): Defaults to Depends(get_db).
    """
    user = get_user_by_username(db=db,username=form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect username or password")
    
    # creating the access token
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}