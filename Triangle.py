#  File: Triangle.py
#  Description: This program compares four different algorithms in order to see which is the fastest in finding the greatest sum path in a pyramid.
#  Student's Name: Sahil Shah
#  Student's UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 4 December 2019
#  Date Last Modified: 5 December 2019

import time
import copy

#returns the greatest path sum using exhaustive search
def exhaustive_search(grid):
    sum_list = []
    exhaustive_helper(grid, 0, 0, 0, sum_list)
    return max(sum_list)

def exhaustive_helper(grid, row, col, sum, sum_list):
    if row == len(grid):
        sum_list.append(sum)
    else:
        sum+=grid[row][col]
        return exhaustive_helper(grid, row+1, col, sum, sum_list) or exhaustive_helper(grid, row+1, col+1, sum, sum_list)

#return the greatest path sum using the greedy approach
def greedy(grid):
    col = 0
    sum = 0
    for row in range(len(grid)-1):
        sum+=grid[row][col]
        if grid[row+1][col] <= grid[row+1][col+1]:
            col+=1
    sum+=grid[row+1][col]
    return sum

#returns the greatest path sum using divide and conquer (recursive) approach
def rec_search(grid):
    return rec_helper(grid, 0, 0)

def rec_helper(grid, row, col):
    if row == len(grid)-1:
        return grid[row][col]
    else:
        return grid[row][col] + max((rec_helper(grid, row+1, col)), rec_helper(grid, row+1, col+1))

#returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    new_grid = copy.deepcopy(grid)
    for row in range(len(new_grid)-1, -1, -1):
        for col in range(0, len(new_grid[row])-1):
            greatest_int = max(new_grid[row][col], new_grid[row][col+1])
            new_grid[row-1][col] = new_grid[row-1][col] + greatest_int
    return new_grid[0][0]

#reads the file and returns a 2-D list that represents the triangle
def read_file():
    pyramid = []
    file = open("./triangle.txt", "r")
    height = int(file.readline().strip())
    for i in range(height):
        line = file.readline().strip()
        row_list = line.split()
        for i in range(len(row_list)):
            row_list[i] = int(row_list[i])
        pyramid.append(row_list)
    return pyramid


def main():
    #read triangular grid from file
    pyr = read_file()

    ti = time.time()
    # output greatest path from exhaustive search
    exh_sum = exhaustive_search(pyr)
    tf = time.time()
    print("The greatest path sum through exhaustive search is " + str(exh_sum) + ".")
    del_t = tf - ti
    # print time taken using exhaustive search
    print("The time taken for exhaustive search is", del_t, "seconds.")
    print()

    ti = time.time()
    # output greatest path from greedy approach
    greedy_sum = greedy(pyr)
    tf = time.time()
    print("The greatest path sum through greedy search is " + str(greedy_sum) + ".")
    del_t = tf - ti
    # print time taken using greedy approach
    print("The time taken for greedy approach is", del_t, "seconds.")
    print()

    ti = time.time()
    # output greatest path from divide-and-conquer approach
    rec_sum = rec_search(pyr)
    tf = time.time()
    print("The greatest path sum through recursive search is " + str(rec_sum) + ".")
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print("The time taken for recursive search is", del_t, "seconds.")
    print()

    ti = time.time()
    # output greatest path from dynamic programming
    dyn_sum = dynamic_prog(pyr)
    tf = time.time()
    print("The greatest path sum through dynamic programming is " + str(dyn_sum) + ".")
    del_t = tf - ti
    # print time taken using dynamic programming
    print("The time taking for dynamic programming is", del_t, "seconds.")

if __name__ == '__main__':
    main()
