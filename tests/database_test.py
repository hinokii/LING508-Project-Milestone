from app.database import *
from app.process import *

def test_database():
    '''
    text = open('web_data.txt', 'r').read()
    tk = TokenizeKoreanSent(text)
    tokenized = tk.tokenize_korean()
    tfidf = TFIDF(tokenized)
    df = tfidf.create_pandas_word_and_tfidf()
    df.to_csv('tfidf.csv', index=True)
    '''
    f = pd.read_csv('tfidf.csv', index_col=0)
    tfidfs = f['tfidf'].tolist()
    words = f.index.values.tolist()

    db = Database(words, tfidfs)
    db.deleted_table('korean_tfidf')
    db = Database(words, tfidfs)
    data = db.create_database("korean_tfidf", "word", 'tfidf')
    result = db.retrive_data("korean_tfidf", 'tfidf')
    assert result[0] == ('고려', 0.358313)
