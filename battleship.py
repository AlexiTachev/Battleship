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

    def display(self):
        ''' Prints the game board to the screen. Replace any ships with water so
        the opponent cannot see them when guessing. '''
        for i in range(5):
            row = ""
            for j in range(5):
                if self.board[i][j] == "#":
                    row += "~"
                else:
                    row += self.board[i][j]
            print row

    def guess(self, x, y):
        ''' Applies the guess to the board. If there is a
        ship, it replaces it with an "X" and print "HIT", otherwise
        replace with a "O" and print "MISS". '''
        row = ""
        for i in range(5):
            if y == i:
                if self.board[x][i] == "#":
                    row += "X"
                else:
                    row += "O"
            else:
                row += self.board[x][i]
        self.board[x] = row

    def hasLost(self):
        ''' Check to see if the board has any more ships
        left. Return True if no ships are left, or False
        otherwise. '''
        # Your code here

#Game().play()

# peek at board
b = Board()
b.display()
b.guess(4,1)
b.display()