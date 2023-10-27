import checkers


def game():
    # size = int(input("Please enter a square board size: "))
    checkers.build_board()
    checkers.get_count()


if __name__ == '__main__':
    game()
