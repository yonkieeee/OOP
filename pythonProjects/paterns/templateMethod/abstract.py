from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def print_product(self):
        pass

class Creator(ABC):
    @abstractmethod
    def create_product(self):
        pass
