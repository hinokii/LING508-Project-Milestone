import abc
from model.word import *

class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load_korean_lexicon(self) -> KoreanWords:
        raise NotImplementedError

    @abc.abstractmethod
    def load_japanese_lexicon(self) -> JapaneseWords:
        raise NotImplementedError
