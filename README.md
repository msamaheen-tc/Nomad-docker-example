# Nomad-docker example
in this example, you will learn how to build a docker file to your python code with the [FastAPI](https://fastapi.tiangolo.com/deployment/docker/) web framework. then write a nomad file for this image.

In this example we will build two applications that can communicate with each other. The first app has a root route that returns the string "app1", and when we route to "/info" the first app will ask for a getting request from the other app (app2) to return "hello world". We chose port 1117 for the first app and 1116 for the second one. but you can choose any port you want.
<hr>

## how the application will look like
after running this example on our local device. it will lokes like this.

| url | message |
| ------ | ------ |
| `http://localhost:1117` | app1|
| `http://localhost:1117/info` | hello world|
`http://localhost:1116` | app2|
| `http://localhost:1116/info` | hello world|

Note that the first application does not contain "hello world", but we used the info-function from the other app.
<br>
<hr>
<br> 

## how to write DockerFile 
there is a common structure when writing docker files. In our case, we have the following steps:


- Image name and version. in our case we used `Python:3.8` as follows: 
    >### `FROM python:3.8`
- defined our application location 
    >`COPY . /app`  
    >`WORKDIR /app` 
- defined the requirements (you can use requirements.txt file and cahnge a bit in the code)
    >`RUN pip3 install uvicorn fastapi asyncio requests`

- final command to run, you can use `python <APP_NAME>.py` command. but in this example we used `uvicorn` by
    >`CMD ["uvicorn", "script1:app", "--host", "0.0.0.0", "--port", "1117"]`

do the same thing for the other app. but change the port number for the second app.

<hr>

## What is Nomad
Nomad enables developers to use declarative infrastructure-as-code for deploying applications. so we can determine for each task how many resources we need. all that to efficiently schedule jobs and optimize for resource utilization.


## Getting Started <hr>

### Requirements 
* [Docker](https://docs.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Python: 3.8](https://www.python.org/)
* [nomad](https://www.nomadproject.io/downloads)
* A good programming text editor (such as vscode, vim) or IDE (PyCharm)


### Run locally
this example was running in a UNIX environment  (Linux, Mac). so if you use windows, you may see some differences.

1. open two terminals and go to root access for each one. by using this command.
   >`sudo -i`
2. for each terminal, go to one of the app directory.
3. if you don't have a [docker hub](https://hub.docker.com/) account go and create one.
4. to login into your local machine, in the terminal write
   >`docker login`
5. now we need to create an image for each app. to do that we use the docker build command with a tag argument named like this: `USER_NAME/IMAGE_NAME`, in our example we named it `app1` and `app2` and the user name is `msamaheen`. but don't forget the dot "`.`", then do the same thing for the second app in the second terminal.
   >`docker build -t msamaheen/app1 .`  

   >`docker build -t msamaheen/app2 .`
6. now to see if our images are running or not. do that we use docker run command with name (container name) and the port argument `docker run -p PORT:PORT --name CONTAINER_NAME USER_NAME/IMAGE_NAME`
   >`docker run -p 1117:1117 --name app1  msamaheen/app1 `  

   >`docker run -p 1116:1116 --name app2  msamaheen/app2 `
7. to access a Docker container from another container we need to create a docker network that open another terminal and write this command by using `docker network create
NETWORK_NAME` . in our example we named it `ping-pong-network` 
    >`docker network create ping-pong-network`
8. now we need to add our container to the Docker network to do that we use `docker network connect NETWORK_NAME APP_NAME`
   >`docker network connect ping-pong-network app1`

   >`docker network connect ping-pong-network app2`
9. when we do Docker inspect, the containers property will show both those containers
    >`docker network inspect ping-pong-network`
10. to see how the app running, open then  browser the type `http://localhost:1117` ,refer to the table above to check out every route.
