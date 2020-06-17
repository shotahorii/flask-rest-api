#!/bin/sh
sudo docker stop $(sudo docker ps -q)
sudo docker rmi shotahorii/flask-rest-api-env