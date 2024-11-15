from abc import ABC, abstractmethod

class Template_class(ABC):
    @abstractmethod
    def print_message(self, message):
        pass

    @abstractmethod
    def count_shos(self, count1, coubt2):
        pass