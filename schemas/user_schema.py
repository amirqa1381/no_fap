from pydantic import BaseModel, EmailStr, SecretStr, PastDatetime


class UserBase(BaseModel):
    """
    This class is for handling the create user model
    """

    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
	"""
	This class is for response of the request that user is sent 
	"""
	user_id: int
	username: str
	email: EmailStr
	password_hash: SecretStr
	is_active: bool
	created_at: PastDatetime
	