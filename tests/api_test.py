import pytest
import json
from app1 import *


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

def test_post_data(client):
    rv = client.post('/post_data',
                     data=json.dumps({"word": "의견", "japanese": "意見", "english": "Jones", "pos": "['Noun']"}),
                     content_type='application/json')
    response = json.loads(rv.data)
    assert response.get("msg") == "success"
    rv = client.get('/get_data')
    data = json.loads(rv.data)
    assert data[-1].get("japanese") == "意見"







