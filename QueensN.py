#  File: Queens.py

#  Description: Counts how many solutions there are

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/25/2019

#  Date Last Modified: 4/1/2019

# var to count solutions
solutions = 0

# queen class


class Queens (object):
  # initialize the board
  def __init__(self, n=8):
    self.board = []
    self.n = n
    for i in range(self.n):
      row = []
      for j in range(self.n):
        row.append('*')
      self.board.append(row)

  # print the board
  def print_board(self):
    for i in range(self.n):
      for j in range(self.n):
        print (self.board[i][j], end=' ')
      print()
    print()

  # check if no queen captures another
  def is_valid(self, row, col):
    for i in range(self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range(self.n):
      for j in range(self.n):
        row_diff = abs(row - i)
        col_diff = abs(col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve(self, col):
    global solutions
    if (col == self.n):
      queenCounter = self.queenCounter()
      if (queenCounter == self.n):
        solutions += 1
      return True
    else:
      correct = False
      for row in range(self.n):
        if (self.is_valid(row, col)):
          self.board[row][col] = 'Q'
          if self.recursive_solve(col + 1) or correct == True:
            correct == True
          else:
            correct == False
          self.board[row][col] = '*'

# makes sure the number of queens are nxn
  def queenCounter(self):
    total = 0
    for i in range(self.n):
      total += self.board[i].count('Q')
    return total

  # solves the board
  def solve(self):
    for i in range(self.n):
      self.recursive_solve(i)


def main():
  # create a chess board
  boardSize = int(input('Enter the size of board: '))
  print()
  while (boardSize <= 0 or boardSize > 16):
    boardSize = int(input('Enter the size of board: '))
    print()

  game = Queens(boardSize)
  game.solve()

  print('Number of solutions: ' + str(solutions))
  print()


main()
