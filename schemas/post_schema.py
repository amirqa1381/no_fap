from pydantic import BaseModel, PositiveInt, Field
from datetime import datetime


class PostBase(BaseModel):
    """
    The post schema model

    Args:
        BaseModel (Base): this is the pydantic base model
    """

    user_id: PositiveInt = Field(..., description="User ID")
    title: str = Field(..., description="Title of the post")
    content: str = Field(..., description="content of the post")


class PostResponse(BaseModel):
    """
    response of the post model

    Args:
        BaseModel (Base): pydantic base model
    """

    post_id: PositiveInt
    user_id: PositiveInt
    title: str
    content: str
    created_at: datetime
