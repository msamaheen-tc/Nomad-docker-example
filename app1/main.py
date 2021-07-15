import uvicorn
from fastapi import FastAPI
import requests
import os
import consul
import json

app = FastAPI()

consul_host = '0ecff8f4088e.ngrok.io'
consul_port = 80

@app.get("/")
def server_health():
    return {"message": "very healthy"}

@app.get("/info")
def get_app2_health():
    response = requests.get("http://localhost:1116")
    return {
        "message": "a message from app2",
        "content": response.content
    }

@app.get("/secret")
def check_password(password = None):
    config = get_config()
    if config['needs_password'] == False:
        return { "message": "ok, no need for password" }
    else:
        target_password = os.environ['TARGET_PASSWORD']
        if password and password == target_password:
            return { "message": "ok, correct password" }
        else:
            return { "message": "error, incorrect password" }

@app.post("/secret")
def change_config(password = None):
    flipped_needs_password = not (get_config()['needs_password'])
    consul_client = consul.Consul(host=consul_host, port=consul_port)
    consul_client.kv.put('myconfig', '{"needs_password": ' + str(flipped_needs_password).lower() + ' }')
    return { "message": "flipped" }


def get_config():
    consul_client = consul.Consul(host=consul_host, port=consul_port)
    index, config_json = consul_client.kv.get("myconfig")
    
    config = json.loads(config_json['Value'])
    return config

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1115)