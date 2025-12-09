from pydantic import BaseModel
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()
    return app


app = create_app()


@app.get("/ping")
def ping():
    return {"status": "ok"}


mock_db = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Jim"},
]


@app.get("/users")
def get_users():
    return mock_db


@app.delete("/users/{user_id}", summary="Delete a user")
def remove_user(user_id: int):
    """Delete a user"""
    global mock_db
    return [user for user in mock_db if user["id"] != user_id]


class UpdateUser(BaseModel):
    name: str | None = None


@app.patch("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    global mock_db
    user_data = user.model_dump(exclude_unset=True)

    for item in mock_db:
        if item["id"] == user_id:
            item.update(user_data)
            return item
    return {"message": "User not found"}
