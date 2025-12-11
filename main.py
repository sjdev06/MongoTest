from fastapi import FastAPI, HTTPException
from models import UserCreate, UserLogin, UserUpdate , Numbers
from database import users_collection
from bson import ObjectId
import bcrypt

app = FastAPI()

@app.get("/health")
def health():

    return "Server is running"

# Helper: Convert MongoDB object to dict
def serialize_user(user):
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "name": user["name"]
    }


# CREATE USER
@app.post("/users")
def create_user(user: UserCreate):
    # Check existing
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")

    #hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())

    user_doc = {
        "email": user.email,
        "name": user.name,
        "password": user.password,
    }

    result = users_collection.insert_one(user_doc)
    return {"id": str(result.inserted_id), "message": "User created"}


# GET USER
@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return serialize_user(user)


# UPDATE USER
@app.put("/users/{user_id}")
def update_user(user_id: str, data: UserUpdate):
    update_data = {}

    if data.name:
        update_data["name"] = data.name

    if data.password:
        update_data["password"] = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated"}


# DELETE USER
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}


# LOGIN / AUTHENTICATE USER
@app.post("/login")
def login(data: UserLogin):
    user = users_collection.find_one({"email": data.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not data.password == user["password"]:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful", "user": serialize_user(user)}

@app.post("/divide")
def add(data: Numbers):
    return {"sum": data.a/data.b}