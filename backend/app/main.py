
from  fastapi import FastAPI
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

@app.delete("/users/{user_id}")
def remove_user(user_id: int):
    global mock_db
    return [user for user in mock_db if user["id"] != user_id]