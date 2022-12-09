FROM python:3.6
COPY requirements.txt /requirements.txt
COPY train.py /train.py

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "train.py"]
