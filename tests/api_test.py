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
