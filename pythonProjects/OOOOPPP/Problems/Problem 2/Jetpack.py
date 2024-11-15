from Problems.Problem1and3.Backpack import Backpack


class Jetpack(Backpack):
    """
    Клас для реактивного ранця.

        Атрибути:
            name (str): Ім'я власника рюкзака.
            color (str): Колір рюкзака.
            max_size (int): Максимальна кількість предметів, які можна вмістити.
            contents (list): Список предметів у рюкзаку.
            fuel (int): Пальне
    """
    def __init__(self, name, color, max_size = 5, fuel = 4):
        """
        Ініцалізовуємо реактивного ранець
        Викликаючи __init__ з батківського класу
        :param name: імя
        :param color: колір
        :param max_size: розмір
        :param fuel: пальне
        """
        super().__init__(name, color, max_size)

        self.fuel = fuel


    def fly(self, amount):
        if amount > self.fuel:
            print("АААААААААААА падаю")
            exit()
        else:
            self.fuel -= amount


    def dump(self):
        super().dump()
        self.fuel = 0


def test_jetpack():
    jet = Jetpack("John", "silver")
    print(jet)
    jet.put("toolkit")
    jet.fly(5)
    print(f"Remaining fuel: {jet.fuel}")
    jet.dump()
    print(f"After dump: Contents={jet.contents}, Fuel={jet.fuel}")

test_jetpack()

if "__main__" == __name__:
    test_jetpack()