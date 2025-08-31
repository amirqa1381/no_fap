from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from database.models.comment_model import Comment
from schemas.comment_schema import CommentBase, CommentResponse


def create_comment(db: Session, request: CommentBase) -> CommentResponse:
    """
    Create a new comment.
    """
    new_comment = Comment(
        title=request.title,
        content=request.content,
        post_id=request.post_id,
        user_id=request.user_id,
        reply=request.reply,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return CommentResponse(
        comment_id=new_comment.comment_id,
        title=new_comment.title,
        content=new_comment.content,
        post_id=new_comment.post_id,
        user_id=new_comment.user_id,
        created_at=new_comment.created_at,
        reply=new_comment.reply,
        replies=[],
    )
    
    
    
def get_comment_by_id(db: Session, comment_id: int) -> CommentResponse:
    """
    Retrieve a comment by its ID, including nested replies.
    """
    comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment with ID {comment_id} not found",
        )
    return CommentResponse.from_orm_with_replies(comment)
