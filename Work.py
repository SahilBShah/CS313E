#  File: Work.py
#  Description: This program counts the number of lines written given the total number of lines that needs to be written and the productivity factor which is related to the number of cups of coffee a person drinks: v // k**p.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 28 September 2019
#  Date Last Modified: 30 September 2019

def main():

    values_list = []

    #Read in input file
    with open("work.txt") as f:
        for row in f:
            values_list.append(row.split())
    #Prints number of lines that are written
    for i in range(int(values_list[0][0])):
        print(binary_search(int(values_list[i+1][0]), int(values_list[i+1][1])))


def binary_search(n, k):
    """
    Uses the binary search algorithm to find the number of lines that is written.
    """

    lo = 0
    hi = n
    lines = 0
    while lo <= hi:
        v = (lo + hi) // 2
        mid = count_lines(v, k)
        if mid > n:
          mid2 = count_lines(v-1, k)
          if mid2 < n:
              return v
          hi = v + 1
        elif mid < n:
          lo = v - 1
        else:
          return v
    return 0


def count_lines(v, k):
    """
    Counts number of lines as the exponent increases each iteration.
    """

    p = 0
    total_lines = 0

    while v // k**p != 0:
        total_lines += v // k**p
        p+=1
    return total_lines


if __name__ == "__main__":
    main()
