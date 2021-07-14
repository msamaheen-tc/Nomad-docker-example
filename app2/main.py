import uvicorn
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def server_health():
    return {"message": "very healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1116)