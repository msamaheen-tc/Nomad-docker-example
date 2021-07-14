import uvicorn
from fastapi import FastAPI
import requests
import os

app = FastAPI()

@app.get("/")
def server_health():
    password = os.environ['TARGET_PASSWORD']
    return {"message": "very healthy", "password": password}

@app.get("/info")
def get_app2_health():
    response = requests.get("http://localhost:1116")
    return {
        "message": "a message from app2",
        "content": response.content
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1115)