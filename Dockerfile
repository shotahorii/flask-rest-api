FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN pip install flask_restful
RUN pip install -U flask-cors

COPY ./app /app


# FROM python:3.8

# RUN apt-get update
# RUN apt-get install nginx -y

# remove # below in production
# COPY . /app
# WORKDIR /app

# RUN pip install flask
# RUN pip install flask_restful
# RUN pip install -U flask-cors

# remove # below in production
# ENTRYPOINT ["python"]
# CMD ["app.py"]

# comment out below in production
# CMD ["bash"]