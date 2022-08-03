from app.services import *

'''
def test_service_korean():
    result = Services('단일화', 'korean').result
    assert result.tfidf == 0.179157
    assert result.japanese == '統一'
    assert result.english == 'Unification'
    assert result.pos == "['Modifier', 'Noun']"
'''

def test_service_japanese():
    result = Services('天守', 'japanese').result
    assert result.korean == '성 타워'
    assert result.english== 'Castle tower'
    assert result.pos == 'Verb'