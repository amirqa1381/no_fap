from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from database.db_connection import get_db
from schemas.comment_schema import CommentBase, CommentResponse
from database.actions.comment_action import create_comment


router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post(
    "/new", summary="Create a new comment", status_code=status.HTTP_201_CREATED
)
async def create_comment_route(
    request: CommentBase, db: Session = Depends(get_db)
) -> CommentResponse:
    """
    Create a new comment.
    """
    return create_comment(db, request)
