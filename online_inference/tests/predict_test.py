from fastapi.testclient import TestClient
import requests
from main import app

client = TestClient(app)


def test_predict():
    file_dir = '../../data/splitted_data/eval_data/eval_data_1_x.csv'
    url = 'http://127.0.0.1:8000/predict'
    with open(file_dir, 'rb') as f:
        response = client.post(url=url, files={'file': f})

    assert response.status_code == 200
    assert response.text == '{"predictions":"[1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1]"}'