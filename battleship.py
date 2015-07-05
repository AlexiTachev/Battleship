from random import random

class Board:

    def __init__(self):
        ''' Creates a game board, a list of strings (5x5).
        Ships are represented as a "#", water is represented
        as a "~", a hit is represented as a "X", and a miss
        is represented as a "O". '''
        self.board = []
        for i in range(5):
            row = ""
            for j in range(5):
                row += "#" if random() < 0.2 else "~"
            self.board.append(row)
