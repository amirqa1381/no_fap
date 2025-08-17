from fastapi import FastAPI
from routers import user, streak, journal


app = FastAPI()
app.include_router(user.router)
app.include_router(streak.router)
app.include_router(journal.router)


@app.get("/")
async def index():
    return {"message": "Hello, World!"}
