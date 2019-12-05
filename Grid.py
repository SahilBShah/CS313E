#  File: Grid.py
#  Description: This program creates a grid with specified numbers and determines the total number of paths to get from the top left ot the bootom right and calculates the greatest sum to reach the end.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 12 October 2019
#  Date Last Modified: 12 October 2019

# counts all the possible paths in a grid recursively
def count_paths (n, row, col):
    if row == n-1 or col == n-1:
        return 1
    else:
        return count_paths(n, row+1, col) + count_paths(n, row, col+1)


# recursively gets the greatest sum of all the paths in the grid
def path_sum (grid, n, row, col):
    if row == n-1 and col == n-1:
        return grid[row][col]
    elif row < n-1 and col < n-1:
        val1 = grid[row][col] + path_sum(grid, n, row+1, col)
        val2 = grid[row][col] + path_sum(grid, n, row, col+1)
        return max(val1, val2)
    elif row < n-1:
        return grid[row][col] + path_sum(grid, n, row+1, col)
    elif col < n-1:
        return grid[row][col] + path_sum(grid, n, row, col+1)


def main():
    # open file for reading
    in_file = open ("./grid.txt", "r")

    # read the dimension of the grid
    dim = in_file.readline()
    dim = dim.strip()
    dim = int(dim)
    # open file for reading
    in_file = open ("./grid.txt", "r")

    # read the dimension of the grid
    dim = in_file.readline()
    dim = dim.strip()
    dim = int(dim)

    # create an empty grid
    grid = []

    # populate the grid
    for i in range (dim):
        line = in_file.readline()
        line = line.strip()
        row = line.split()
        for j in range (dim):
            row[j] = int (row[j])
        grid.append (row)

    # close the file
    in_file.close()

    # get the number of paths in the grid and print
    num_paths = count_paths (dim, 0, 0)
    print ('Number of paths in a grid of dimension', dim, 'is', num_paths)
    print ()

    # get the maximum path sum and print
    max_path_sum = path_sum (grid, dim, 0, 0)
    print ('Greatest path sum is', max_path_sum)


main()
