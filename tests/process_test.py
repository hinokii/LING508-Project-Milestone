from app.process import *
#import pytest

k_sent = '서울에 있는 냉면 맛집 찾아야겠다'
j_sent = '猫は基本的にほかの動物を捕らえて食べる肉食動物です'
e_sent = 'A cat is sleeping on a couch for 10 hours'


def test_k_pos():
    pos = TaggedSentence(k_sent,'korean')
    print(pos)
    k_pos = pos.get_morpheme_and_pos()
    assert k_pos == [('서울', 'Noun'), ('에', 'Josa'), ('있다', 'Adjective'),
                     ('냉면', 'Noun'), ('맛집', 'Noun'), ('찾다', 'Verb')]

'''
def test_j_pos():
    pos1 = TaggedSentence(j_sent, 'japanese')
    j_pos = pos1.get_morpheme_and_pos()
    assert j_pos == [('猫', 'Noun'), ('は', 'Post Positional Particle'),
                     ('基本', 'Noun'), ('的', 'Conjunction'),
                     ('に', 'Auxiliary Verb'), ('ほか', 'Noun'),
                     ('の', 'Post Positional Particle'), ('動物', 'Noun'),
                     ('を', 'Post Positional Particle'), ('捕らえ', 'Verb'),
                     ('て', 'Post Positional Particle'), ('食べる', 'Verb'),
                     ('肉食', 'Noun'), ('動物', 'Noun'),
                     ('です', 'Auxiliary Verb')]
'''

def test_translate_j_to_k():
    tran = Translate(j_sent, "ko")
    assert tran.translate() == '고양이는 기본적으로 다른 동물을 잡고 먹는 육식 ' \
                               '동물입니다.'

def test_translate_k_to_e():
    tran = Translate(k_sent, "en")
    assert tran.translate() == 'I need to find a cold noodle restaurant in ' \
                               'Seoul'
'''
def test_tfidf():
    URL = "https://land.naver.com/news/newsRead.naver?type=headline&prsco_id=020&arti_id=0003440084"
    web_scr = WebScraper(URL, "korean")
    kkma = Kkma()
    tx = kkma.sentences(web_scr.parse_from_web())
    tfidf = TFIDF(tx)
    df = tfidf.create_pandas_word_and_tfidf()
    result = df.loc[df.index == '고려', 'tfidf'].to_string(index=False)
    assert float(result) == 0.358313
'''