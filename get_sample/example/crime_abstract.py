from abc import *

class EditorBase(metaclass=ABCMeta):
    @abstractmethod
    def dropna(self):
        pass

class printerBase(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class ReaderBase(printerBase):


    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass

    @abstractmethod
    def json(self):
        pass

    @abstractmethod
    def gmaps(self):
        pass

class ScraperBase(metaclass=ABCMeta):
    @abstractmethod
    def scrap(self):
        pass



