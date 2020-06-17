# flask-rest-api
RESTful API Server using flask.

## Run the server on EC2 (First time)

1. Initiate an EC2 instance with opening port 80
2. Install Docker on the instance: `yum update && yum install docker`
3. Make sure the docker is running: `sudo service docker start`
4. Pull the necessary docker image: `sudo docker pull tiangolo/uwsgi-nginx-flask`
5. Clone this repo on the instance: `sudo yum install git` then `git clone <this repo url>`
6. `cd` to the directory where Dockerfile is located
7. `sh start.sh`

## When the server scripts are updated

1. `cd` to the repo folder 
2. `sh stop.sh`
3. `git pull`
4. Files in `storage/` folder (listed in .gitignore) need to be uploaded manually with `scp -i /path/to/pem/file/XXX.pem /path/to/file/to/upload/YYY.py ec2-user@ec2-XX-XX-XX.compute-1.amazonaws.com:/home/ec2-user/ZZZ`
5. `sh start.sh`