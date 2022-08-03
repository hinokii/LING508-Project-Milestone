from db.mysql_repo import *
import pandas as pd

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
    '''
    df = pd.read_csv('df.csv', index_col=0)

    tfidfs = df['tfidf'].tolist()
    words = df.index.values.tolist()
    pos = df['POS'].tolist()
    eng = df['English'].tolist()
    jp = df['Japanese'].tolist()
    repo = MysqlRepository()
    #repo.del_table
    #repo = MysqlRepository()
    repo.insert_table(words, tfidfs, jp, eng, pos)
    result = repo.load_lexicon()
    assert result[0]['tfidf'] == 0.358313

