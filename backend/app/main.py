
from  fastapi import FastAPI
def create_app() -> FastAPI:
    app = FastAPI()
    return app

app = create_app()
@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
        {"id": 3, "name": "Jim"},
    ]