from sqlalchemy.orm.session import Session
from schemas.post_schema import PostBase, PostResponse
from database.models.post_model import Post


def post_create(request: PostBase, db: Session) -> PostResponse:
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
