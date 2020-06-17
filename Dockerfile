FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN pip install flask_restful

COPY ./app /app

# docker run -d --rm -p 80:80 shotahorii/flask-rest-api-env
# http://127.0.0.1