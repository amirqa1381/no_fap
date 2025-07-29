from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    This function is for hashing the password that user insert
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    This function is for checking and verifyingthe user plain password with main hashed password
    """
    checked = pwd_context.verify(plain_password, hashed_password)
    return checked
