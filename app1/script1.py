import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import requests
import asyncio 
import os


app = FastAPI()


@app.get("/")
def read_root():
    return "app1"

@app.get("/info")
def get_info():
    data = requests.get('http://app2:1116/info')
    
    return data.content

# this app work on port:1117
if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=1117)
