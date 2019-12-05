import math

class Point (object):
  # constructor
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # test for equality of two Point objects
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

def main():
  # create an empty list of Point objects
  points_list = []
  new_list = []


  # open file points.txt for reading
  with open("points.txt") as f:
      for row in f:
         new_list = row.split()
         c = Point(int(new_list[0]), int(new_list[1]))
         print(c)
  #print(new_list)
  # read the file line by line, create Point objects and add to the list

  # initialize a variable to hold the shortest distance

  # Use a pair of nested loops to go through all pairs of Point objects
  # Find the minimum distance between all pairs

  # print the shortest distance

main()
