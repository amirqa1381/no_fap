from fastapi import FastAPI
from routers import user, streak, journal, post, comment


app = FastAPI()
app.include_router(user.router)
app.include_router(streak.router)
app.include_router(journal.router)
app.include_router(post.router)
app.include_router(comment.router)


@app.get("/")
async def index():
    return {"message": "Hello, World!"}
