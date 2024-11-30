from app.config import MONGO_URI
from pymongo import MongoClient
from passlib.context import CryptContext

client = MongoClient(MONGO_URI)
db = client["your_database"]
users_collection = db["users"]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(email: str, password: str):
    user = users_collection.find_one({"email": email})
    if user and pwd_context.verify(password, user["password"]):
        return user
    return None

def create_user(email: str, full_name: str, password: str, role: str = "user"):
    hashed_password = pwd_context.hash(password)
    user_data = {
        "email": email,
        "full_name": full_name,
        "password": hashed_password,
        "role": role,
    }
    users_collection.insert_one(user_data)
    return user_data
