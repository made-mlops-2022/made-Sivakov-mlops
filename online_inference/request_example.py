import csv
import requests

file_dir = '../data/splitted_data/eval_data/eval_data_1_x.csv'
url = 'http://127.0.0.1:8080/predict'

with open(file_dir, 'r') as f:
    r = requests.post(url, files={'file': f})
    print(r.text)
