from konlpy.tag import Okt
from sudachipy import tokenizer
from sudachipy import dictionary
from googletrans import Translator
# pip install googletrans==4.0.0rc1
import requests
from bs4 import BeautifulSoup
# from readability import Document
from konlpy.tag import Kkma
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from db.mysql_repo import *

'''
class WebScraper:
    def __init__(self, url):
        self.url = url

    def parse_from_web(self):
        page = requests.get(self.url)
        doc = Document(page.text).summary()
        print(page)
        soup = BeautifulSoup(doc, "lxml")
        text = soup.get_text()
        with open('web_data.txt', 'w') as file:
            file.write(text)
        return file

url = "https://land.naver.com/news/newsRead.naver?type=headline&prsco_id=020&arti_id=0003440084"
ws = WebScraper(url)
file = ws.parse_from_web()
'''

# Return tuple of each morpheme (Korean or Japanese) and POS (English)
class TaggedSentence:
    # Take a sentence and language (Japanese or Korean)
    def __init__(self, sentence, language):
        self.sent = sentence
        self.lang = language
        self.tagged = self._get_tagged()

    def _get_tagged(self):
        # For Korean, use konlpy.tag to get pos
        if self.lang == "korean":
            okt = Okt()
            k_trans = (okt.pos(self.sent, norm=True, stem=True, join=True))
            k_pos = []
            for i in k_trans:
                k_pos.append(tuple(i.split('/')))
            return k_pos

        # For Japanese, use sudachipy to get pos
        elif self.lang == "japanese":
            tokenizer_obj = dictionary.Dictionary().create()
            mode = tokenizer.Tokenizer.SplitMode.A

            # Tokenize to get morphemes
            j_mor = [m.surface() for m in
                     tokenizer_obj.tokenize(self.sent, mode)]

            pos = [j.part_of_speech() for j in
                   tokenizer_obj.tokenize(self.sent, mode)]

            # Since pos is returned in Japanese, convert to English
            # Dict of Japanese pos as keys and corresponding English
            # as values
            d = {'名詞': 'Noun', '助詞': "Post Positional Particle",
                 '接尾辞': "Conjunction", '助動詞': "Auxiliary Verb",
                 '動詞': "Verb"}

            # Use the first pos in Japanese (pos above returns various
            # pos names)
            first_pos = [i[0] for i in pos]
            pos = []
            for i in first_pos:
                for k, v in d.items():
                    if i == k:
                        pos.append(v)

            j_pos = list(zip(j_mor, pos))

            return list(j_pos)

        else:
            raise NotImplementedError

    # Translate a sentence using googletrans
    def translate(self, destination_language):
        translator = Translator()
        translated_text = translator.translate(self.sent, dest=destination_language)
        return translated_text.text


class TokenizeKoreanSent:
    def __init__(self, text):
        self.text = text

    def tokenize_korean(self):
        kkma = Kkma()
        tokenized = kkma.morphs(self.text)
        tx = kkma.sentences(self.text)
        return tx


# Compute TFIDF using sklearn and return pandas DataFrame with tokenized
# words and corresponding tfidf
class VocabTFIDF:
    def __init__(self, sentences):
        self.sent = sentences
        self.df = self._create_pandas()

    def _create_pandas(self):
        vectorizer = TfidfVectorizer(use_idf=True)
        tfidf = vectorizer.fit_transform(self.sent)
        vocabulary = vectorizer.vocabulary_
        #print(vocabulary)
        df = pd.DataFrame(tfidf[0].T.todense(),
                          index=vectorizer.get_feature_names_out(),
                          columns=['tfidf'])
        df = df.sort_values(by=['tfidf'], ascending=False)
        return df

class Services:
    def __init__(self, search_word):
        self.search_word = search_word
        self.repo = MysqlRepository()
        self.result = self._show_result()

    def generate_table(self):
        text = open('web_data.txt', 'r').read()
        tk = TokenizeKoreanSent(text)
        tokenized = tk.tokenize_korean()
        df = VocabTFIDF(tokenized).df
        tfidfs = df['tfidf'].tolist()[:7]
        words = df.index.values.tolist()[:7]
        tags = [str([y for x, y in TaggedSentence(word, 'korean').tagged]) for word in words]
        j_lst = [TaggedSentence(word, 'korean').translate("ja") for word in words]
        e_lst = [TaggedSentence(word, 'korean').translate("en") for word in words]
        self.repo.insert_table(words, tfidfs, j_lst, e_lst, tags)

        return self.repo.load_lexicon()

    def _show_result(self):  # show tfidf, japanese, enlighs and pos of the Korean word (search_word)
        db = self.generate_table()
        result = ''
        for i in range(len(db)):
            if db[i]['word'] == self.search_word:
                result = db[i]
        if result is not None:
            return result
        else:
            return "I don't have that word!"
