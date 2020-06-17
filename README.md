# flask-rest-api
RESTful API Server using flask.

## Run the server on EC2 (First time)

1. Initiate an EC2 instance with opening port 80
2. Install Docker on the instance: `yum update && yum install docker`
3. Make sure the docker is running: `sudo service docker start`
4. Pull the necessary docker image: `sudo docker pull tiangolo/uwsgi-nginx-flask`
5. Clone this repo on the instance: `sudo yum install git` then `git clone <this repo url>`
6. `cd` to the directory where Dockerfile is located, then `sudo docker build -t <image name> .`
7. Start the server: `sudo docker run -d --rm -p 80:80 <image name> `

## When the server scripts are updated

1. (Assuming the server is running.) Find the container id: `sudo docker ps -a` then copy the container id. 
2. Stop the server `sudo docker stop <container id>`
3. Find the docker image id: `sudo docker images` then copy the image id of the image built above.
4. Delete the image: `sudo docker rmi <image id>`
5. `cd` to the repo folder 
6. 
