#File: Geom.py
#Description: This program reads in an input file containing coordinates and determines if a square, circle, or point intersect each other or are located within one another.
#Student's Name: Sahil Shah
#Student's UT EID: sbs2756
#Course Name: CS 313E
#Unique Number: 50205
#Date Created: 19 September 2019
#Date Last Modified: 20 September 2019

import math

class Point (object):

    # constructor
    # x and y are floats
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__ (self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):

    # constructor
    # x, y, and radius are floats
    def __init__ (self, radius = 1, x = 0, y = 0):
        self.radius = radius
        self.center = Point (x, y)

    # compute cirumference
    def circumference (self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area (self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside (self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside (self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # but neither is completely inside the other
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap (self, c):
        if self.center.dist(c.center) + c.radius < self.radius:
            return False
        elif self.center.dist(c.center) < c.radius + self.radius:
            return True
        else:
            return False

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribe (self, r):
        center_x = r.ul_x + ((r.lr_x - r.ul_x) / 2)
        center_y = r.lr_y + ((r.ul_y - r.lr_y) / 2)
        center = Point(center_x, center_y)
        radius = self.center.dist(r.ul)
        return "Radius: " + str(radius) + ", Center: " + str(center)

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__ (self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__ (self, other):
        tol = 1.0e-8
        return abs(self.radius - other.radius) < tol

class Rectangle (object):
    # constructor
    def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
          self.ul = Point (ul_x, ul_y)
          self.lr = Point (lr_x, lr_y)
        else:
          self.ul = Point (0, 1)
          self.lr = Point (1, 0)
        self.ul_x = ul_x
        self.ul_y = ul_y
        self.lr_x = lr_x
        self.lr_y = lr_y
        self.center_x = self.ul_x + ((self.lr_x - self.ul_x) / 2)
        self.center_y = self.lr_y + ((self.ul_y - self.lr_y) / 2)
        self.center = Point(self.center_x, self.center_y)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length (self):
        rect_length = self.lr_x - self.ul_x
        return rect_length

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width (self):
        rect_width = self.ul_y - self.lr_y
        return rect_width

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter (self):
        rect_length = self.length()
        rect_width = self.width()
        rect_perimeter = 2 * rect_length + 2 * rect_width
        return rect_perimeter

    # determine the area
    # takes no arguments, returns a float
    def area (self):
        rect_length = self.length()
        rect_width = self.width()
        return rect_length * rect_width

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside (self, p):
        if self.center.dist(p) < self.center.dist(self.ul) and p.x > self.ul_x and p.x < self.lr_x and p.y < self.ul_y and p.y > self.lr_y:
            return True
        else:
            return False

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside (self, r):
        if self.ul == r.ul and self.lr == r.lr:
            return False
        elif r.ul_x < self.lr_x and r.ul_x > self.ul_x and r.ul_y < self.ul_y and r.ul_y > self.lr_y and r.lr_x > self.ul_x and r.lr_x < self.lr_x and r.lr_y < self.ul_y and r.lr_y > self.lr_y:
            return True
        else:
            return False

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap (self, r):
        if r.ul_x > self.ul_x and r.ul_x < self.lr_x and r.ul_y > self.lr_y and r.ul_y < self.ul_y and (r.lr_x > self.lr_x or r.lr_y < self.lr_y):
            return True
        elif r.lr_x > self.ul_x and r.lr_x < self.lr_x and r.lr_y > self.lr_y and r.lr_y < self.ul_y and (r.ul_x < self.ul_x or r.ul_y > self.ul_y):
            return True
        else:
            return False

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rectangle_circumscribe (self, c):
        rect_ul_x = c.center.x - c.radius
        rect_ul_y = c.center.y + c.radius
        rect_lr_x = c.center.x + c.radius
        rect_lr_y = c.center.y - c.radius
        rect_ul = Point(rect_ul_x, rect_ul_y)
        rect_lr = Point(rect_lr_x, rect_lr_y)
        return "UL: " + str(rect_ul) + ", LR: " + str(rect_lr)

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__ (self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__ (self, other):
        tol = 1.0e-8
        if abs(self.center.dist(self.ul) - other.center.dist(other.ul)) < tol and abs(self.center.dist(self.lr) - other.center.dist(other.lr)) < tol:
            return True
        else:
            return False

def main():

    line_list = []
    new_list = []

    # open the file geom.txt
    with open('geom.txt') as f:
        for line in f:
            line_list.append(line.split('#')[0].split())
    for item in line_list:
        if len(item) == 2:
            new_list.append([float(item[0]), float(item[1])])
        elif len(item) == 3:
            new_list.append([float(item[0]), float(item[1]), float(item[2])])
        elif len(item) == 4:
            new_list.append([float(item[0]), float(item[1]), float(item[2]), float(item[3])])

    # create Point objects P and Q
    P = Point(new_list[0][0], new_list[0][1])
    Q = Point(new_list[1][0], new_list[1][1])

    # print the coordinates of the points P and Q
    print("Coordinates of P:", P)
    print("Coordinates of Q:", Q)

    # find the distance between the points P and Q
    distance_pq = P.dist(Q)
    print("Distance between P and Q:", distance_pq)

    # create two Circle objects C and D
    C = Circle(new_list[2][0], new_list[2][1], new_list[2][2])
    D = Circle(new_list[3][0], new_list[3][1], new_list[3][2])

    # print C and D
    print("Circle C:", C)
    print("Circle D:", D)

    # compute the circumference of C
    print("Circumference of C:", C.circumference())

    # compute the area of D
    print("Area of D:", D.area())

    # determine if P is strictly inside C
    is_inside_cd = C.circle_inside(D)
    if is_inside_cd == True:
        print("D is inside C")
    else:
        print("D is not inside C")

    # determine if C is strictly inside D
    is_inside_dc = D.circle_inside(C)
    if is_inside_dc == True:
        print("C is inside D")
    else:
        print("C is not inside D")

    # determine if C and D intersect (non zero area of intersection)
    is_intersect = C.circle_overlap(D)
    if is_intersect == True:
        print("C does intersect D")
    else:
        print("C does not intersect D")

    # determine if C and D are equal (have the same radius)
    if C == D:
        print("C is equal to D")
    else:
        print("C is not equal to D")

    # create two rectangle objects G and H
    G = Rectangle(new_list[4][0], new_list[4][1], new_list[4][2], new_list[4][3])
    H = Rectangle(new_list[5][0], new_list[5][1], new_list[5][2], new_list[5][3])

    # print the two rectangles G and H
    print("Recatngle G:", G)
    print("Rectange H:", H)

    # determine the length of G (distance along x axis)
    print("Length of G:", G.length())

    # determine the width of H (distance along y axis)
    print("Width of H:", H.width())

    # determine the perimeter of G
    print("Perimeter of G:", G.perimeter())

    # determine the area of H
    print("Area of H:", H.area())

    # determine if point P is strictly inside rectangle G
    is_point_inside = G.point_inside(P)
    if is_point_inside == True:
        print("P is inside G")
    else:
        print("P is not inside G")

    # determine if rectangle G is strictly inside rectangle H
    is_rect_inside = H.rectangle_inside(G)
    if is_rect_inside == True:
        print("G is inside H")
    else:
        print("G is not inside H")

    # determine if rectangles G and H overlap (non-zero area of overlap)
    does_overlap = G.rectangle_overlap(H)
    if does_overlap == True:
        print("G does overlap H")
    else:
        print("G does not overlap H")

    # find the smallest circle that circumscribes rectangle G
    # goes through the four vertices of the rectangle
    print("Circle that circumscribes G:", Circle().circle_circumscribe(G))

    # find the smallest rectangle that circumscribes circle D
    # all four sides of the rectangle are tangents to the circle
    print("Rectangle that circumscribes D:", Rectangle().rectangle_circumscribe(D))

    # determine if the two rectangles have the same length and width
    if G == H:
        print("G is equal to H")
    else:
        print("G is not equal to H")

    # close the file geom.txt
    f.close()

    # This line above main is for grading purposes. It will not affect how
    # your code will run while you develop and test it.
    # DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
