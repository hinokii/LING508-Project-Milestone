import abc
from model.word import *

class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load_lexicon(self) -> KoreanWords:
        raise NotImplementedError
