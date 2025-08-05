from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from database.models.user_model import User
from schemas.user_schema import UserBase, UserUpdateBasicBase
from auth.hashing import hash_password


def create_user(db: Session, request: UserBase):
    new_user = User(
        username=request.username,
        email=request.email,
        password_hash=hash_password(request.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_specific_user(id: int, db: Session, request: UserUpdateBasicBase):
    """
    Function for updating the specific user
    Args:
            db (Session): db base
            request (UserUpdateBasicBase): schema for updating
    """
    user = db.query(User).filter(User.user_id == id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="The user is not found"
        )
    user.username = request.username
    user.email = request.email
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session):
    """
    This function is for getting all the users
    """
    users = db.query(User).all()
    return users


def get_specific_user(db: Session, id: int):
    """
    This function is for getting the specifice user with id
    """
    user = db.query(User).filter(User.user_id == id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this id is not found.",
        )

    return user


def get_user_by_username(db: Session, username: str):
    """
    Function for getting the user by username
    Args:
        db (Session): db base
        username (str): username of the user
    """
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this username is not found.",
        )
    return user
