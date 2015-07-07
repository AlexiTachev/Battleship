from random import random

class Game:

    def __init__(self):
        ''' The game keeps track of a board for each player, as well as
        whose turn it currently is. '''
        self.turn = 0
        self.players = [Board(), Board()]

    def parseGuess(self, guess):
        ''' This function takes a guess in the form of "A0",
        and returns the coordinates (0,0) to be used to find
        in a game board. '''
        return int(guess[1]) - 1, ord(guess[0].upper()) - 65

    def play(self):
        ''' Main game loop, continues to run while neither
        player hasLost. Take input from user, apply the
        guess to the opponent board, check to see if the
        opponent has lost, then change turn. If a player
        loses, exit the loop and print the winner. '''
        while not self.players[0].hasLost() and not self.players[1].hasLost():
            self.players[(self.turn - 1) % 2].display()
            guess = raw_input("Player %s turn to guess: " % (self.turn +1))
            x, y = self.parseGuess(guess)
            self.players[self.turn].display()
            self.players[(self.turn - 1) % 2].guess(x, y)
            self.turn = (self.turn - 1) % 2
        if self.players[0].hasLost():
            print "Player 2 wins!"
        else:
            print "Player 1 wins!"

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
        ''' Prints the game board to the screen. Replaces any ships with water so
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
                    print
                    print "HIT"
                    print
                else:
                    row += "O"
                    print
                    print "MISS"
                    print
            else:
                row += self.board[x][i]
        self.board[x] = row

    def hasLost(self):
        ''' Checks to see if the board has any ships
        left. Returns True if no ships are left, or False
        otherwise. '''
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == "#":
                    return False
        return True

Game().play()