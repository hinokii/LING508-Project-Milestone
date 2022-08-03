from db.mysql_repo import *
from app.process import *

def test_japanese_database():
    text = open('web_data1.txt', 'r').read()
    words = [x for x, y in TaggedSentence(text, 'japanese').tagged][1:10]
    tags = [y for x, y in TaggedSentence(text, 'japanese').tagged]
    k_lst = [TaggedSentence(word, 'japanese').translate("ko") for word in words]
    e_lst = [TaggedSentence(word, 'japanese').translate("en") for word in words]
    repo = MysqlRepository()
    repo.insert_japanese_table(words, k_lst, e_lst, tags)
    result = repo.load_japanese_lexicon()
    print(result)
    assert result[0]['korean'] == '마른'