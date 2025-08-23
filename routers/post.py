from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from database.actions.post_action import get_all_posts, get_post_by_id, post_create, update_post, delete_post
from database.db_connection import get_db
from schemas.post_schema import PostResponse, PostBase



router = APIRouter(prefix="/posts", tags=["Posts"])

# Get part

@router.get("/", response_model=list[PostResponse])
def get_posts_route(db: Session = Depends(get_db)):
    """
    Retrieve all posts from the database.
    """
    return get_all_posts(db=db)


@router.get("/{post_id}", response_model=PostResponse)
def get_post_route(post_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific post by its ID.
    """
    post = get_post_by_id(db=db, id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found"
        )
    return post


# Post part

@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post_route(request: PostBase, db: Session = Depends(get_db)):
    """
    Create a new post in the database.
    """
    return post_create(db=db, request=request)



# Update part

@router.put("/{post_id}", response_model=PostResponse)
def update_post_route(post_id: int, request: PostBase, db: Session = Depends(get_db)):
    """
    Update an existing post by its ID.
    """
    return update_post(id=post_id, request=request, db=db)


# Delete part

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post_route(post_id: int, db: Session = Depends(get_db)):
    """
    Delete a post by its ID.
    """
    return delete_post(id=post_id, db=db)