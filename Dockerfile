FROM amd64/python:3.9-buster

WORKDIR /docker

COPY .. .

RUN pip install -r requirements.txt
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8080