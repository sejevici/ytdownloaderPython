from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("3963001e-233d-40d1-9754-74667a631b70"),
        first_name="Victor",
        last_name="Bischoff",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=UUID("cff7f082-dfe6-4f8c-83e6-cc8fd3da787d"),
        first_name="viggo",
        last_name="Bischoff",
        gender=Gender.male,
        roles=[Role.student]
    )
]
@app.get("/")
async def root():
    return {"Hello": "WORLD"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

