FROM python:3.6
COPY requirements.txt /requirements.txt
COPY predict.py /predict.py

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "predict.py"]
