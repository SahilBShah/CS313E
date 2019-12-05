#  File: ConvexHull.py
#  Description: This program uses the Graham scan algorithm to find the convex polygon around a set of points and determines the area of the convex polygon found.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 25 September 2019
#  Date Last Modified: 26 September 2019

import math

class Point (object):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return False
          else:
            return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return True
          else:
            return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return False
          else:
            return (self.y > other.y)
        return (self.x > other.x)

    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return True
          else:
            return (self.y >= other.y)
        return (self.x >= other.x)

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det (p, q, r):
    """
    Determines the determinant given three points.
    """

    return p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y * p.x


# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull (sorted_points):
    """
    Determines the convex hull given a set of points.
    """

    #Creates empty list for upper and lower hulls of convex polygon
    upper_hull = []
    lower_hull = []

    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])

    #Determines which points in the upper hull move to the right of one another
    for i in range(0, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0:
            upper_hull.pop(-2)

    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])

    #Determines which points in the lower hull move to the right of one another
    for i in range(len(sorted_points)-1, -1, -1):
        lower_hull.append(sorted_points[i])
        while(len(lower_hull)) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0:
            lower_hull.pop(-2)
    lower_hull.pop(0)
    lower_hull.pop(-1)

    convex_hull = upper_hull + lower_hull
    return convex_hull



# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly (convex_poly):

    determinant = 0

    #Determines the determinant for the convex polygon found
    for x in range(len(convex_poly)):
        if x+1 != len(convex_poly):
            determinant += convex_poly[x].x * convex_poly[x+1].y
            determinant -= convex_poly[x].y * convex_poly[x+1].x
        else:
            determinant += convex_poly[x].x * convex_poly[0].y
            determinant -= convex_poly[x].y * convex_poly[0].x

    #Returns the area of the convex polygon
    return 0.5 * abs(determinant)

def main():

    # create an empty list of Point objects
    points_list = []

    # open file points.txt for reading and creates Point objects stored in a list
    with open("points.txt") as f:
        next(f)
        for row in f:
            line = row.split()
            point = Point(int(line[0]), int(line[1]))
            points_list.append(point)

    # sort the list according to x-coordinates
    points_list.sort()

    # get the convex hull
    convex_hull_final = convex_hull(points_list)

    # print the convex hull
    print("Convex Hull")
    for i in range(len(convex_hull_final)):
        print('(' + str(convex_hull_final[i].x) + ', ' + str(convex_hull_final[i].y) + ')')
    print()

    # get the area of the convex hull
    convex_hull_area = area_poly(convex_hull_final)

    # print the area of the convex hull
    print("Area of Convex Hull =", convex_hull_area)

# YOU MUST WRITE THIS LINE AS IS
if __name__ == "__main__":
  main()
