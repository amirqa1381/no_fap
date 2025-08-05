from jose import jwt, JWTError
from datetime import datetime, timedelta
from config import Settings
from typing import Optional


setting = Settings()


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Creating the access token for the user if login into the system

    Args:
        data (dict):
        expires_delta (timedelta, optional): _description_. Defaults to None.
    """
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, setting.secret_key, algorithm=setting.algorithm)


def verify_token(token: str):
    """
    Verify the token for the user

    Args:
        token (str):

    Raises:
        JWTError: Could not validate credential.
    """
    try:
        payload = jwt.decode(token, setting.secret_key, algorithms=[setting.algorithm])
        return payload
    except JWTError:
        raise JWTError("Could not validate credentials")
