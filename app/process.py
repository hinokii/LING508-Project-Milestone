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


# Return tuple of each morpheme (Korean or Japanese) and POS (English)
class TaggedSentence:
    # Take a sentence and language (Japanese or Korean)
    def __init__(self, sentence, languages):
        self.sent = sentence
        self.lang = languages

    def get_morpheme_and_pos(self):
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
            return "You entered an unknown language!"


# Translate a sentence using googletrans
class Translate:
    def __init__(self, sentence, language):
        self.sent = sentence
        self.lang = language

    def translate(self):
        translator = Translator()
        translated_text = translator.translate(self.sent, dest=self.lang)
        return translated_text.text

'''
# This is an optional project milestone for week 3. Although not required
# to submit, I incorporated into the main project mileston.
# Obtain text from web, parse and return tokenized text
class WebScraper:
    def __init__(self, url, language):
        self.url = url
        self.lang = language

    def parse_from_web(self):
        page = requests.get(self.url)
        doc = Document(page.text).summary()
        print(page)
        soup = BeautifulSoup(doc, "lxml")
        text = soup.get_text()
        return text

    def tokenize_text(self):
        if self.lang == "korean":
            kkma = Kkma()
            text = self.parse_from_web()
            tokenized = kkma.morphs(text)
            return tokenized

        elif self.lang == "japanese":
            tokenizer_obj = dictionary.Dictionary().create()
            mode = tokenizer.Tokenizer.SplitMode.A
            text = self.parse_from_web()
            tokenized = [m.surface() for m in
                         tokenizer_obj.tokenize(text, mode)]
            return tokenized

        else:
            return "You entered an unknown language!"
'''

# Compute TFIDF using sklearn and return pandas DataFrame with tokenized
# words and corresponding tfidf
class TFIDF:
    def __init__(self, sentences):
        self.sent = sentences

    def create_pandas_word_and_tfidf(self):
        vectorizer = TfidfVectorizer(use_idf=True)
        tfidf = vectorizer.fit_transform(self.sent)
        vocabulary = vectorizer.vocabulary_
        #print(vocabulary)
        df = pd.DataFrame(tfidf[0].T.todense(),
                          index=vectorizer.get_feature_names_out(),
                          columns=["tfidf"])
        df = df.sort_values(by=["tfidf"], ascending=False)
        return df
