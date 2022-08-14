import pytest
import json
from app.app1 import *


@pytest.fixture
def client():
    a = create_app()
    with a.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/hello')
    assert b"Hello World!" in rv.data

def test_get_data(client):
    rv = client.get('/get_data')
    data = json.loads(rv.data)
    assert data[0].get('word') == "고려"








'''
import requests

BASE = "http://127.0.0.1:5000/"

def test_get_api():
    response = requests.get(BASE + "word/天守")
    print(response.json())
    assert response.json() == {'english': 'Castle tower',
                                'korean': '성 타워',
                                'pos': "['Noun']",
                                'tfidf': 0.491773,
                                'word': '天守'}
'''
