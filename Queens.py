#  File: Queens.py
#  Description: This program provides all the solutions to placing queens on a board in spaces where none of the queens can capture one another.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 18 October 2019
#  Date Last Modified: 24 October 2019

import copy

class Queens(object):
    #Initialize the board
    def __init__(self, n=8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    #Print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()

    #Check if no queens can capture another
    def is_valid(self, row, col):
        for i in range(self.n):
            if self.board[row][i] == 'Q' or self.board[i][col] == 'Q':
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if row_diff == col_diff and self.board[i][j] == 'Q':
                    return False
        return True

    #Do a recursive backtracking solution
    def recursive_solve(self, col):

        global soln
        ct = 0

        if col == self.n:
            if self.num_queens() == self.n:
                soln+=1
                self.print_board()
                print()
            return True
        else:
            cont = False
            for i in range(self.n):
                if self.is_valid(i, col):
                    self.board[i][col] = 'Q'
                    if self.recursive_solve(col+1) or cont == True:
                        cont = True
                    else:
                        cont = False
                    self.board[i][col] = '*'

    #Counts number of queens on board
    def num_queens(self):
        tot = 0
        for i in range(self.n):
            tot+=self.board[i].count('Q')
        return tot

    #If the problem has a solution print the board
    def solve(self):
        board = copy.deepcopy(self.board)
        for i in range(self.n):
            self.recursive_solve(i)
            self.board = board

        print('There are', soln, 'solutions for a ' + str(self.n) + 'x' + str(self.n) + ' board.')

def main():

    global soln
    soln = 0

    #User inputs desired board dimensions
    dim = input('Enter the size of board: ')
    while dim.isdigit() == False or int(dim) < 1 or int(dim) > 8:
        dim = input('Enter the size of board: ')
    print()
    dim = int(dim)

    #Create a regular chess board
    game = Queens(dim)

    #Place the queens on the board
    game.solve()


main()
