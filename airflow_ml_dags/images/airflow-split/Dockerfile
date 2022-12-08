FROM python:3.6
COPY requirements.txt /requirements.txt
COPY preprocess.py /preprocess.py

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "split.py"]
