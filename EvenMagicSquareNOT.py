#  File: EvenMagicSquare.py

#  Description: Generating a user-dictated number of magic squares of order 4 using permutation

#  Student Name: Sakina Daresalamwala

#  Student UT EID: ssd849

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 10/19/2018

#  Date Last Modified: 10/25/2018

import math

#create global list and global order of 4 for squares
square_list = []
n = 4

# set magic number based on n
n = float(n)
magic_num = int(n * ((n ** 2 + 1) / 2))
n = int(n)

def check(a, num_squares):
    # make 2-D list/actual square
    square = []
    for i in range(0, n):
        each_row = []
        for j in range(0, n):
            each_row.append(a[(i * n) + j])
        square.append(each_row)

    # check if rows add up to magic sum
    for i in range(0, n):
        row = square[i]
        row_sum = 0
        for j in range(0, n):
            row_sum += row[j]

        if row_sum == magic_num:
            continue
        else:
            return False

    # check if columns add up to magic sum
    for i in range(0, n):
        col_sum = 0
        for j in range(0, n):
            col_sum += square[j][i]

        if col_sum == magic_num:
            continue
        else:
            return False

    # check if diagonal from top left to bottom right adds up to magic sum
    diag1_sum = 0
    count = 0
    for i in range(0, n):
        diag1_sum += square[i][count]
        count += 1

    if diag1_sum == magic_num:
        pass
    else:
        return False

    # check if diagonal from bottom left to top right adds up to magic sum
    diag2_sum = 0
    count = 0
    for i in range(n - 1, -1, -1):
        diag2_sum += square[i][count]
        count += 1

    if diag2_sum == magic_num:
        pass
    else:
        return False

    #print the number of squares requested by the user
    square_list.append(square)
    print_squares(square)

    if len(square_list) >= num_squares:
        quit()

    return True

def optimized(a, lo):
    #checks if row totals are equal to the magic number
    row = ((lo + 1) // n) - 1

    checklist = []
    for i in range(0, n):
        row_list = []
        for j in range(0, n):
            row_list.append(a[(i * n) + j])
        checklist.append(row_list)

    if sum(checklist[row]) != magic_num:
        return False
    else:
        return True

def permute(a, lo, num_squares):
    # permute list of numbers
    hi = len(a)
    row_len = int(math.sqrt(hi))

    if (lo == hi):
        check(a, num_squares)
    else:
        for i in range(lo, hi):
            a[lo], a[i] = a[i], a[lo]
            if (lo + 1) % row_len == 0:
                if not optimized(a,lo):
                    a[lo], a[i] = a[i], a[lo]
                    continue
            permute(a, lo + 1, num_squares)
            a[lo], a[i] = a[i], a[lo]

def print_squares(square):
    #print squares neatly in right justified format
    print("")
    for line in square:
        print('{:>3} {:>3} {:>3} {:>3}'.format(*line))

def main():
    #get number of squares to generate
    num_squares = int(input("Enter number of magic squares (1 - 10): "))
    while (num_squares < 1) or (num_squares > 10):
        num_squares = int(input("Enter number of magic squares (1 - 10): "))

    #populate list with numbers based on order n (in this case, 4)
    integer_list = []
    for i in range(1, n**2 + 1):
        integer_list.append(i)

    #permute the list and generate magic squares
    permute(integer_list, 0, num_squares)

if __name__ == "__main__":
    main()