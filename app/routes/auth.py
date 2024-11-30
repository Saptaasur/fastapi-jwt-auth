from fastapi import APIRouter, HTTPException
from app.utils.security import create_access_token
from app.services.auth_service import authenticate_user

router = APIRouter()

@router.post("/login")
def login(email: str, password: str):
    user = authenticate_user(email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user["email"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}
