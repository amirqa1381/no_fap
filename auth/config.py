from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application, loaded from environment variables.

    Args:
        BaseSettings (_type_): Base class for settings management.
    """

    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = "key.env"
