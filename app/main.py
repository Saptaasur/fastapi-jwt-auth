from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI JWT Authentication Service"}

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/users")
