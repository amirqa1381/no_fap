from fastapi import HTTPException, status
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from database.models.user_model import User
from schemas.user_schema import UserBase
from database.hashing import hash_password


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





def get_all_users(db: Session):
	"""
	This function is for getting all the users
	"""
	users = db.query(User).all()
	return users



def get_specifice_user(db:Session, id: int):
	"""
	This function is for getting the specifice user with id
	"""
	user = db.query(User).filter(User.user_id == id).first()
	if user is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user with this id is not found.")
	
	return user