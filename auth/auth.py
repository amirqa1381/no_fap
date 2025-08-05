from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from security import verify_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Get the current user based on the provided token.

    Args:
        token (str, optional): Defaults to Depends(oauth2_scheme).
    """
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload.get("sub")  # Assuming 'sub' is the user identifier in the
