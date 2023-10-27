from numpy import random


def build_board():
    size = int(input("Please enter a square board size: "))
    board = random.choice(['empty', 'black', 'red'], (size, size))
    return board


board1 = build_board()
print("Your Board -")
print(board1)


def get_count():
    emptys = (board1 == 'empty')
    blacks = (board1 == 'black')
    reds = (board1 == 'red')
    print("Here's how many EMPTY spaces there are - ")
    print(emptys.sum())
    print("Here's how many BLACK spaces there are - ")
    print(blacks.sum())
    print("Here's how many RED spaces there are - ")
    print(reds.sum())


get_count()

if __name__ == "__main__":
    print("Please do not run this file directly. It should be imported from a separate main.py file.")
