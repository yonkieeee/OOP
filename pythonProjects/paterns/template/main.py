from template.classes.shos_1 import Shos_One
from template.classes.shos_2 import ShosTwo

def main():
    shos1 = Shos_One()
    shos2 = ShosTwo()

    shos1.print_message('efefwfw')
    shos2.print_message('efefwfw')
    shos1.count_shos(2, 3)
    shos2.count_shos(2, 3)

if __name__ == '__main__':
    main()