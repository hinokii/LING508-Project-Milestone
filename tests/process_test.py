from app.services import TaggedSentence
import pytest
import os


k_sent = '서울에 있는 냉면 맛집 찾아야겠다'
j_sent = '猫は基本的にほかの動物を捕らえて食べる肉食動物です'
e_sent = 'A cat is sleeping on a couch for 10 hours'

def test_k_pos():
    pos = TaggedSentence(k_sent,'korean')
    assert pos.tagged == [('서울', 'Noun'), ('에', 'Josa'), ('있다', 'Adjective'),
                     ('냉면', 'Noun'), ('맛집', 'Noun'), ('찾다', 'Verb')]

def test_j_pos():
    pos1 = TaggedSentence(j_sent, 'japanese')
    print(pos1)
    assert pos1.tagged == [('猫', 'Noun'),
                           ('は', 'Post Positional Particle'),
                           ('基本', 'Noun'),
                           ('的', 'Conjunction'),
                           ('に', 'Auxiliary Verb'),
                           ('ほか', 'Noun'),
                           ('の', 'Post Positional Particle'),
                           ('動物', 'Noun'),
                           ('を', 'Post Positional Particle'),
                           ('捕らえ', 'Verb'),
                           ('て', 'Post Positional Particle'),
                           ('食べる', 'Verb'),
                           ('肉食', 'Noun'),
                           ('動物', 'Noun'),
                           ('です', 'Auxiliary Verb')]

def test_translate_j_to_k():
    tran = TaggedSentence(j_sent, "japanese")
    assert tran.translate("ko") == '고양이는 기본적으로 다른 동물을 잡고 먹는 육식 ' \
                               '동물입니다.'

def test_translate_k_to_e():
    tran = TaggedSentence(k_sent, "korean")
    assert tran.translate("en") == 'I need to find a cold noodle restaurant in ' \
                               'Seoul'
'''
def test_tfidf():
    #URL = "https://land.naver.com/news/newsRead.naver?type=headline&prsco_id=020&arti_id=0003440084"
    #web_scr = WebScraper(URL, "korean")
    tx = open('web_data.txt', 'r').read()

    tokenized = TokenizeKoreanSent(tx)
    tfidf = VocabTFIDF(tokenized.tokenize_korean())
    df = tfidf.df
    result = df.loc[df.index == '고려', 'tfidf'].to_string(index=False)
    assert float(result) == 0.358313
'''   
