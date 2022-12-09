FROM python:3.6
COPY requirements.txt /requirements.txt
COPY validate.py /validate.py

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "validate.py"]
