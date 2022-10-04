from app.services import *


def test_service_korean():
    result = Services().show_result("주택", "korean")
    assert result.tfidf == 0.296352
    assert result.japanese == 'ハウジング'
    assert result.english == 'Housing'
    assert result.pos == "['Noun']"

def test_service_japanese():
    result = Services().show_result('天守', 'japanese')
    assert result.tfidf == 0.491773
    assert result.korean == '성 타워'
    assert result.english== 'Castle tower'
    assert result.pos == "['Noun']"