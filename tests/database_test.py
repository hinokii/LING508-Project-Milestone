import nagisa
from db.mysql_repo import *
from app.services import *

def test_japanese_database():
    #text = open('web_data1.txt', 'r').read()
    #words = [x for x, y in TaggedSentence(text, 'japanese').tagged][1:10]
    #tags = [y for x, y in TaggedSentence(text, 'japanese').tagged]
    text = []
    with open('web_data1.txt', 'r') as f:
        text.append(f.read())

    def tokenize_jp(text):
        doc = nagisa.filter(text, filter_postags=['助詞', '補助記号', '助動詞'])
        return doc.words
    df = VocabTFIDF(text, tokenize_jp).df
    tfidfs = df['tfidf'].tolist()[:10]
    words = df.index.values.tolist()[:10]

    tags = [str([y for x, y in TaggedSentence(word, 'japanese').tagged]) for word in words]
    k_lst = [TaggedSentence(word, 'japanese').translate("ko") for word in words]
    e_lst = [TaggedSentence(word, 'japanese').translate("en") for word in words]
    repo = MysqlRepository()
    repo.insert_japanese_table(words, tfidfs, k_lst, e_lst, tags)
    result = repo.load_japanese_lexicon()
    for i in result:
        if i.word == '時計':
            assert i.english == 'clock'
