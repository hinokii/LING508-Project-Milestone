from app.services import *

def test_service():
    result = Services('단일화').result
    assert result['tfidf'] == 0.179157
    assert result['japanese'] == '統一'
    assert result['english'] == 'Unification'
    assert result['pos'] == "['Modifier', 'Noun']"