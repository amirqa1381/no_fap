from pydantic import BaseModel, Field, PositiveInt, PastDatetime
from datetime import datetime
from typing import Optional



class CommentBase(BaseModel):
    title: str = Field(..., max_length=255)
    content: str = Field(..., max_length=500)
    post_id: PositiveInt
    user_id: PositiveInt
    reply: Optional[PositiveInt] = None  # New field for parent comment ID
    
    
    

class CommentResponse(CommentBase):
    comment_id: int
    title: str
    content: str
    post_id: PositiveInt
    user_id: PositiveInt
    created_at: PastDatetime
    reply: Optional[list["CommentResponse"]] = []  # List of replies to this comment
    

    class Config:
        orm_mode = True