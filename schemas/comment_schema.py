from pydantic import BaseModel, Field, PositiveInt, PastDatetime
from datetime import datetime
from typing import Optional, List


class CommentBase(BaseModel):
    title: str = Field(..., max_length=255)
    content: str = Field(..., max_length=500)
    post_id: PositiveInt
    user_id: PositiveInt
    reply: Optional[PositiveInt] = None  # New field for parent comment ID


class CommentResponse(CommentBase):
    comment_id: int
    created_at: PastDatetime
    replies : List["CommentResponse"] = []

    model_config = {
        "from_attributes": True
    }
    
    @classmethod
    def from_orm_with_replies(cls, comment):
        """
        Build CommentResponse manually to prevent recursion errors
        """
        
        return cls(
            comment_id=comment.comment_id,
            title=comment.title,
            content=comment.content,
            post_id=comment.post_id,
            user_id=comment.user_id,
            created_at=comment.created_at,
            reply=comment.reply,
            replies=[cls.from_orm_with_replies(c) for c in comment.replies] if comment.replies else []
        )
