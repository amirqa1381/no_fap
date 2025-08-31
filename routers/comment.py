from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from database.db_connection import get_db
from schemas.comment_schema import CommentBase, CommentResponse
from database.actions.comment_action import create_comment, get_comment_by_id


router = APIRouter(prefix="/comments", tags=["Comments"])

# post route to create a new comment
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




# get route to retrieve a comment by its ID, including nested replies

@router.get("/{comment_id}", summary="Get comment by ID", response_model=CommentResponse)
async def get_comment_by_id_route(comment_id: int, db: Session = Depends(get_db)) -> CommentResponse:
    """
    Retrieve a comment by its ID, including nested replies.
    """
    return get_comment_by_id(db, comment_id)