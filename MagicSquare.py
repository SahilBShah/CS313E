#Description: This program creates a magic square with user-defined parameters, prints out the magic square, and verifies that the square created is a magic square.
#Student's Name: Sahil Shah
#Student's UT EID: sbs2756
#Course Name: CS 313E
#Unique Number: 50205
#Date Created: 2 September 2019
#Date Last Modified: 2 September 2019

def main():

    user_value = int(input("Please enter an odd number: "))
    while user_value < 0 or user_value % 2 == 0:
        user_value = int(input("Please enter an odd number: "))
    magic_square = make_square(user_value)
    canonical_sum = (len(magic_square) * (len(magic_square) ** 2 + 1)) / 2
    print_square(magic_square)
    is_magic_square = check_square(magic_square)
    if is_magic_square == True:
        print("This is a magic square and the canonical sum is", int(canonical_sum))
    else:
        print("This is not a magic square")


def make_square(n):
    """
    Creates an n x n magic square with user inputed parameters.
    """

    working_square = []
    number = 1
    row = n - 1
    column = int(n / 2)

    #Creates the starting square with a 1 in the middle column, last row
    working_square = [[0 for i in range(n)] for j in range(n)]
    working_square[row][column] = number
    number+=1

    #Completes the magic square
    while number <= n**2:
        if row+1 > n-1 and column+1 > n-1:
            row-=1
        elif row+1 > n-1:
            row = 0
            column+=1
        elif column+1 > n-1:
            column = 0
            row+=1
        elif working_square[row+1][column+1] == 0:
            row+=1
            column+=1
        elif working_square[row+1][column+1] != 0:
            row-=1
        working_square[row][column] = number

        number+=1
    return working_square


def print_square(magic_square):
    """
    Prints out the magic square in a list without brackets.
    """

    print("Here is a", len(magic_square), "x", len(magic_square), "magic square:")
    #Prints out the magic square
    for i in range(len(magic_square)):
        print(' '.join(map(str, magic_square[i])).rjust(len(magic_square)*3))


def check_square(magic_square):
    """
    Determines if produced square is a megic square.
    """

    canonical_sum = (len(magic_square) * (len(magic_square) ** 2 + 1)) / 2
    row_sum = 0
    column_sum = 0
    diagonal_sum = 0

    #Determines sum of the rows
    for i in range(len(magic_square)):
        for j in range(len(magic_square)):
            row_sum+=magic_square[i][j]
    row_sum = row_sum / len(magic_square)

    #Determines sum of the columns
    for i in range(len(magic_square)):
        for j in range(len(magic_square)):
            column_sum+=magic_square[j][i]
    column_sum = column_sum / len(magic_square)

    #Determines sum of the diagonals
    row = 0
    left_column = 0
    right_column = len(magic_square) - 1
    for i in range(len(magic_square)):
        diagonal_sum+=magic_square[row][left_column]
        diagonal_sum+=magic_square[row][right_column]
        row+=1
        left_column+=1
        right_column-=1
    diagonal_sum = diagonal_sum / 2

    if row_sum == canonical_sum and column_sum == canonical_sum and diagonal_sum == canonical_sum:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
