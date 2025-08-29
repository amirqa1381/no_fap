from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas.post_schema import PostBase, PostResponse, PostUpdate
from schemas.comment_schema import CommentResponse
from database.models.post_model import Post
from sqlalchemy.orm import joinedload


def post_create(request: PostBase, db: Session) -> PostResponse:
    """
    create function for post model

    Args:
        request (PostBase): _description_
        db (Session): _description_

    Returns:
        PostResponse: response schema that we have
    """
    new_post = Post(
        user_id=request.user_id, title=request.title, content=request.content
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return PostResponse(
        post_id=new_post.post_id,
        user_id=new_post.user_id,
        title=new_post.title,
        content=new_post.content,
        created_at=new_post.created_at,
    )


def get_post_by_id(db: Session, id: int):
    """
    get post obj by id

    Args:
        db (Session): _description_
    """
    post = db.query(Post).filter(Post.post_id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The post with this id was not found",
        )

    return post


def update_post(id: int, request: PostUpdate, db: Session) -> PostResponse:
    """
    update post by id

    Args:
        id (int): _description_
        request (PostBase): _description_
        db (Session): _description_

    Raises:
        HTTPException: _description_

    Returns:
        PostResponse: _description_
    """
    post = get_post_by_id(db=db, id=id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The post with this id was not found",
        )

    post.title = request.title if request.title else post.title
    post.content = request.content if request.content else post.content

    db.commit()
    db.refresh(post)
    return PostResponse(
        post_id=post.post_id,
        user_id=post.user_id,
        title=post.title,
        content=post.content,
        created_at=post.created_at,
    )


def delete_post(id: int, db: Session):
    """
    delete post by id

    Args:
        id (int): _description_
        db (Session): _description_

    Raises:
        HTTPException: _description_
    """
    post = get_post_by_id(db=db, id=id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The post with this id was not found",
        )

    db.delete(post)
    db.commit()
    return {"detail": "Post deleted successfully"}


def get_all_posts(db: Session) -> list[PostResponse]:
    """
    get all posts

    Args:
        db (Session): _description_

    Returns:
        list[PostResponse]: _description_
    """
    posts = db.query(Post).options(joinedload(Post.comments)).all()
    return [
        PostResponse(
            post_id=post.post_id,
            user_id=post.user_id,
            title=post.title,
            content=post.content,
            created_at=post.created_at,
            comments=[CommentResponse.model_validate(comment) for comment in post.comments],
        )
        for post in posts
    ]
