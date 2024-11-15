


class Backpack:
    """
        Клас для рюкзака.

        Атрибути:
            name (str): Ім'я власника рюкзака.
            color (str): Колір рюкзака.
            max_size (int): Максимальна кількість предметів, які можна вмістити.
            contents (list): Список предметів у рюкзаку.
        """

    def __init__(self, name, color, max_size = 5): # This function is the constructor.
        """
        Ініціалізує рюкзак ого

        :param name: імя власника
        :param color: колір рююкзака
        :param max_size: розмір його
        """
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        """Додає предмет до рюкзака, якщо є місце."""
        if len(self.contents) < self.max_size:
            self.contents.append(item)
        else:
            print("Нема місця")

    def take(self, item):
        """Беремо предмети"""
        self.contents.remove(item)

    def dump(self):
        """Викидуємо всі предмети в смітник"""
        self.contents.clear()

    def __eq__(self, other):
        return (self.name == other.name
                and self.color == other.color
                and self.max_size == other.max_size)


    def __str__(self):
        """Говорить"""
        return f"""Власник:{self.name}
Колір:{self.color}
Розмір:{self.max_size}
Предмети:{self.contents}"""




def test_backpack():
    testpack_one = Backpack("Barry", "black")
    if testpack_one.name != "Barry":
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack_one.put(item)

    print(testpack_one)

    testpack_one.take("pencil")

    print("Забрали олівець:\n", testpack_one)

    testpack_one.dump()

    print("Після очистки:\n", testpack_one, "\n--------------------------------------------------\n")

    testpack_two = Backpack("Barry", "black")
    print(testpack_two==testpack_one)

    testpack_three = Backpack("Michael", "white")

    print(testpack_two == testpack_three)


if "__main__" == __name__:
    test_backpack()