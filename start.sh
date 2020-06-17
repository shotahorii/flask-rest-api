#!/bin/sh
sudo docker build -t shotahorii/flask-rest-api-env .
sudo docker run -d --rm -p 80:80 shotahorii/flask-rest-api-env