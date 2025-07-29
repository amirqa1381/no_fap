from fastapi import FastAPI
from routers import user




app = FastAPI()
app.include_router(user.router)


@app.get("/")
async def index():
    return {"message": "Hello, World!"}
