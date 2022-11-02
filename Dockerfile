FROM amd64/python:3.9-buster

WORKDIR /docker

COPY . .

RUN pip install -r requirements.txt