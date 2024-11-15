from classes.shoper import *

def main():
    bananaShpoer = ShoperBanana()

    print(bananaShpoer.create_product())

    appleShpoer = ShoperApple()
    print(appleShpoer.create_product())

if __name__ == "__main__":
    main()
