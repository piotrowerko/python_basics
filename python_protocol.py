# https://www.freecodecamp.org/news/python-property-decorator/

# https://www.pythontutorial.net/python-oop/python-protocol/
from typing import List, Protocol

class Item(Protocol):
    quantity: float
    price: float

def main():
    ppp = Item
    print(ppp)

if __name__ == '__main__':
    main()