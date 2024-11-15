from templateMethod.classes.Apple import Apple
from templateMethod.classes.Banana import Banana
from templateMethod.abstract import *

class ShoperApple(Creator):
    def create_product(self):
        return str(Apple.print_product(self))

class ShoperBanana(Creator):
    def create_product(self):
        return str(Banana.print_product(self))