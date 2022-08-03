from db.mysql_repo import *
from app.services import *

def test_database_tfidf():
    '''
    url = "https://land.naver.com/news/newsRead.naver?type=headline&prsco_id=020&arti_id=0003440084"
    ws = WebScraper(url)
    file = ws.parse_from_web()

    text = open('web_data.txt', 'r').read()
    tk = TokenizeKoreanSent(text)
    tokenized = tk.tokenize_korean()
    tfidf = TFIDF(tokenized)
    df = tfidf.create_pandas_word_and_tfidf()
    print(df)

    #df.to_csv('tfidfs.csv', index=True)
    df = pd.read_csv('df.csv', index_col=0)

    tfidfs = df['tfidf'].tolist()
    words = df.index.values.tolist()
    pos = df['POS'].tolist()
    eng = df['English'].tolist()
    jp = df['Japanese'].tolist()

    b = Database(words, tfidfs, jp, eng, pos)
    b.deleted_table('korean_tfidf')
    db = Database(words, tfidfs, jp, eng, pos)
    db.create_database("korean_tfidf", "word", 'tfidf', 'japanese', 'english', 'pos')
    result = db.retrive_data("korean_tfidf")

    df = pd.read_csv('df.csv', index_col=0)

    #tfidfs = df['tfidf'].tolist()
    #words = df.index.values.tolist()
    pos = df['POS'].tolist()
    eng = df['English'].tolist()
    jp = df['Japanese'].tolist()
    '''

    text = open('web_data.txt', 'r').read()
    tk = TokenizeKoreanSent(text)
    tokenized = tk.tokenize_korean()
    df = VocabTFIDF(tokenized).df
    tfidfs = df['tfidf'].tolist()[:3]
    words = df.index.values.tolist()[:3]

    tags = [str([y for x, y in TaggedSentence(word, 'korean').tagged]) for word in words]
    j_lst = [TaggedSentence(word, 'korean').translate("ja") for word in words]
    e_lst = [TaggedSentence(word, 'korean').translate("en") for word in words]

    #repo = MysqlRepository()
    #repo.del_table()
    repo = MysqlRepository()
    repo.insert_table(words, tfidfs, j_lst, e_lst, tags)
    result = repo.load_lexicon()
    for i in range(len(result)):
        if result[i]['word'] == '고려':
            print(result[i])
        else:
            continue
    assert result[0] == {'word': '고려', 'tfidf': 0.358313, 'japanese': '考慮', 'english': 'Consideration', 'pos': "['Noun']"}

