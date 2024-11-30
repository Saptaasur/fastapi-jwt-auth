def get_user_by_id(user_id: str):
    return users_collection.find_one({"_id": user_id})

def get_all_users():
    return list(users_collection.find({}, {"password": 0}))

def update_user(user_id: str, updates: dict):
    users_collection.update_one({"_id": user_id}, {"$set": updates})

def delete_user(user_id: str):
    users_collection.delete_one({"_id": user_id})
