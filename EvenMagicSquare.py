#  File: EvenMagicSquare.py
#  Description: This program prints all of the magic squares produced from a square containing number 1-16.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 12 October 2019
#  Date Last Modified: 15 October 2019

def main():

    global count
    count = 0

    #Creating list of integers for creating a magic square
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    #Permuting integers to produce all even magic squares
    permute(int_list, 0, 16)



def permute (a, lo, hi):
    """
    Permutes the magic square to determine all even magic squares.
    """

    global count

    if lo == hi:
        #Determines if square is a magic square
        magic_square = [a[i:i+4] for i in range(0, len(a), 4)]
        if check_square(magic_square) == True:
            print(a)
            count+=1
            if count == 10:
                quit()
    else:
        #Permutes magic square and is optimized so that only permutations with canonical sum are checked
        for i in range (lo, hi):
            a[i], a[lo] = a[lo], a[i]
            if lo == 3 and a[0] + a[1] + a[2] + a[3] != 34:
                pass
            elif lo == 7 and a[4] + a[5] + a[6] + a[7] != 34:
                pass
            elif lo == 11 and a[8] + a[9] + a[10] + a[11] != 34:
                pass
            elif lo == 12 and a[0] and a[0] + a[4] + a[8] + a[12] != 34 and a[0] + a[5] + a[10] + a[15] != 34:
                pass
            else:
                permute(a, lo+1, hi)
            a[i], a[lo] = a[lo], a[i]


def check_square(magic_square):
    """
    Determines if produced square is a magic square.
    """

    canonical_sum = 34

    #Determines sum of the rows
    for i in range(len(magic_square)):
        row_sum = 0
        for j in range(len(magic_square)):
            row_sum+=magic_square[i][j]
        if row_sum != canonical_sum:
            return False

    #Determines sum of the columns
    for i in range(len(magic_square)):
        column_sum = 0
        for j in range(len(magic_square)):
            column_sum+=magic_square[j][i]
        if column_sum != canonical_sum:
            return False

    #Determines sum of the diagonals
    row = 0
    left_column = 0
    right_column = 3
    diagonal1_sum = 0
    diagonal2_sum = 0
    for i in range(len(magic_square)):
        diagonal1_sum+=magic_square[row][left_column]
        row+=1
        left_column+=1
    if diagonal1_sum != canonical_sum:
        return False

    row = 0

    for i in range(len(magic_square)):
        diagonal2_sum+=magic_square[row][right_column]
        row+=1
        right_column-=1
    if diagonal2_sum != canonical_sum:
        return False

    return True


main()
