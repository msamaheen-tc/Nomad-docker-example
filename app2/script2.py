import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def read_root():
    return "app2"

@app.get("/info")
def send_info():
    return "hello world"

# this app work on port:1116 
if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=1116)