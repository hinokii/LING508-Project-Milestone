from app.database import *
from app.process import *

def test_database():
    '''
    url = "https://land.naver.com/news/newsRead.naver?type=headline&prsco_id=020&arti_id=0003440084"
    ws = WebScraper(url)
    file = ws.parse_from_web()
    text = open('web_data.txt', 'r').read()
    tk = TokenizeKoreanSent(text)
    tokenized = tk.tokenize_korean()
    tfidf = TFIDF(tokenized)
    df = tfidf.create_pandas_word_and_tfidf()
    tfidfs = df['tfidf'].tolist()
    words = df.index.values.tolist()

    tags = []
    j_lst = []
    e_lst = []
    for word in words:
        tags.append([y for x,y in TaggedSentence(word, 'korean').get_morpheme_and_pos()])
        e_lst.append(Translate(word, "en").translate())
        j_lst.append(Translate(word, "ja").translate())

    df.insert(1, "Japanese", j_lst, True)
    df.insert(2, "English", e_lst, True)
    df.insert(3, "POS", tags, True)
    df.to_csv('df.csv', index=True)
    '''
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

    assert result[0] == ('고려', 0.358313, '考慮', 'Consideration', "['Noun']")

