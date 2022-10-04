from konlpy.tag import Okt
from sudachipy import tokenizer
from sudachipy import dictionary
from googletrans import Translator
# pip install googletrans==4.0.0rc1
import requests
from bs4 import BeautifulSoup
from readability import Document
from konlpy.tag import Kkma
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import nagisa
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
        with open('web_data2.txt', 'w') as file:
            file.write(text)
        return file
url = "https://n.news.naver.com/article/088/0000777415"
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
        try:
            translated_text = translator.translate(self.sent, dest=destination_language)
            return translated_text.text
        except:
             pass


class TokenizeKoreanSent:
    def __init__(self, text):
        self.text = text

    def tokenize_korean(self):
        kkma = Kkma()
        tx = kkma.sentences(self.text)
        return tx

# Compute TFIDF using sklearn and return pandas DataFrame with tokenized
# words and corresponding tfidf
class VocabTFIDF:
    def __init__(self, sentences, token_method=None):
        self.sent = sentences
        self.df = self._create_pandas(token_method)

    def _create_pandas(self, token_method=None):
        vectorizer = TfidfVectorizer(tokenizer=token_method, use_idf=True)
        tfidf = vectorizer.fit_transform(self.sent)
        vocabulary = vectorizer.vocabulary_
        #print(vocabulary)
        df = pd.DataFrame(tfidf[0].T.todense(),
                          index=vectorizer.get_feature_names_out(),
                          columns=['tfidf'])
        df = df.sort_values(by=['tfidf'], ascending=False)
        return df

class Services:
    def __init__(self):
        self.repo = MysqlRepository()
        self.k_dict = self._generate_korean_dct()
        self.j_dict = self._generate_japanese_dct()

    def _generate_korean_dct(self):
        #url
        #ws = WebScraper(url)
        #file = ws.parse_from_web()
        text = open('web_data2.txt', 'r').read()
        tokenized = TokenizeKoreanSent(text).tokenize_korean()
        df = VocabTFIDF(tokenized).df
        tfidfs = df['tfidf'].tolist()[:10]
        words = df.index.values.tolist()[:10]
        tags = [str([y for x, y in TaggedSentence(word, 'korean').tagged]) for word in words]
        j_lst = [TaggedSentence(word, 'korean').translate("ja") for word in words]
        e_lst = [TaggedSentence(word, 'korean').translate("en") for word in words]
        self.repo.insert_korean_table(words, tfidfs, j_lst, e_lst, tags)

        return self.repo.create_korean_dict()

    def _generate_japanese_dct(self):
        #URL = "https://www.yomiuri.co.jp/hobby/travel/20220802-OYT1T50077/"
        #web_scr = WebScraper(URL, "japanese").parse_from_web()
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
        self.repo.insert_japanese_table(words, tfidfs, k_lst, e_lst, tags)

        return self.repo.create_japanese_dict()

    # show tfidf, japanese, enlighs and pos of the JP or KR word (search_word)
    def show_result(self, word, language):
        result = ''

        if language == 'korean':
            db = self.repo.load_korean_lexicon()
            for i in db:
                if i.word == word:
                    result = i

        elif language == 'japanese':
            db1 = self.repo.load_japanese_lexicon()
            for j in db1:
                if j.word == word:
                    result = j

        if result is not None:
            return result
        else:
            return "I don't have that word!"

'''
REFERENCES
1. Ng Wai Foong. 2019. SudachiPy: A Japanese Morphological Analyzer in Python.
   Towards Data Science. 
   https://towardsdatascience.com/sudachipy-a-japanese-morphological-analyzer-in-python-5f1f8fc0c807

2. Kavita Ganesan. 2021. How to Use Tfidftransformer & Tfidfvectorizer? 
   AI Implementation, Hands-On NLP.
   https://kavita-ganesan.com/tfidftransformer-tfidfvectorizer-usage-differences/#.YvfDM2HMLJU
   
3. Jonathan Soma. How to use NLP with scikit-learn vectorizers in Japanese, Chinese 
   (and other East Asian languages) by using a custom tokenize.
   Data Science for Journalism a.k.a. investigate.ai.
   https://investigate.ai/text-analysis/how-to-make-scikit-learn-natural-language-processing-work-with-japanese-chinese/
'''
#result = Services().k_dict
#print(result)
print(Services().show_result("주택", "korean").japanese)
print(Services().show_result("주택", "korean").english)
print(Services().show_result("주택", "korean").pos)
#print(results)