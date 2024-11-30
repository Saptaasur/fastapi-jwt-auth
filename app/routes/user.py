from fastapi import APIRouter, Depends, HTTPException
from app.utils.security import decode_access_token, oauth2_scheme
from app.services.user_service import get_all_users, get_user_by_id, update_user, delete_user

router = APIRouter()

@router.get("/users")
def list_users(token: str = Depends(oauth2_scheme)):
    decoded = decode_access_token(token)
    if decoded["role"] != "admin":
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    return get_all_users()
