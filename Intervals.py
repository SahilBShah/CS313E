#File: Intervals.py
#Description: This program reads in an input file containing coordinates and collapses the intervals if they intersect until each interval is mutually exclusive.
#Student's Name: Sahil Shah
#Student's UT EID: sbs2756
#Course Name: CS 313E
#Unique Number: 50205
#Date Created: 6 September 2019
#Date Last Modified: 8 September 2019


def main():

    with open("intervals.txt") as f:
        input_file = [tuple(map(int, row.split(" "))) for row in f]
    interval_list = collapse_intervals(input_file)
    check = check_file(interval_list)

    while check == False:
        interval_list = collapse_intervals(interval_list)
        check = check_file(interval_list)

    print_intervals(interval_list)


def collapse_intervals(input_file):
    """
    Collapse intervals if they intersect.
    """

    new_interval_list = []
    num1 = 0
    num2 = 0

    #Collapses intervals if they intersect
    for i in range(0, len(input_file)):
        for j in range(0, len(input_file)):
            #input_file[i] != input_file[j]
            if i != j:
                num1 = 0
                num2 = 0
                #If the first number is positive do the following:
                if input_file[i][0] >= 0:
                    if input_file[i][0] >= input_file[j][0] and input_file[i][0] <= input_file[j][1]:
                            num1 = input_file[j][0]
                            if input_file[i][1] < input_file[j][1] or input_file[i][1] == input_file[j][1]:
                                num2 = input_file[j][1]
                            elif input_file[i][1] > input_file[j][1]:
                                num2 = input_file[i][1]
                            if (num1, num2) not in new_interval_list:
                                new_interval_list.append((num1, num2))

                #If both numbers in the interval are negative do the following:
                elif input_file[i][0] < 0 and input_file[i][1] < 0:
                    if input_file[i][0] >= input_file[j][0] and input_file[i][0] <= input_file[j][1]:
                            num1 = input_file[j][0]
                            if input_file[i][1] > input_file[j][1] or input_file[i][1] == input_file[j][1]:
                                num2 = input_file[i][1]
                            elif input_file[i][1] < input_file[j][1]:
                                num2 = input_file[j][1]
                            if (num1, num2) not in new_interval_list:
                                new_interval_list.append((num1, num2))
                    elif input_file[i][1] <= input_file[j][0] and input_file[i][1] >= input_file[j][1]:
                        num2 = input_file[j][1]
                        if input_file[i][0] > input_file[j][0]:
                            num1 = input_file[i][0]
                        elif input_file[i][0] < input_file[j][0]:
                            num1 = input_file[j][0]
                        if (num1, num2) not in new_interval_list:
                            new_interval_list.append((num1, num2))

                #If the first number in the interval is negative and the second is positive do the following:
                elif input_file[i][0] < 0 and input_file[i][1] >= 0:
                    if input_file[i][0] >= input_file[j][0] and input_file[i][0] <= input_file[j][1]:
                            num1 = input_file[j][0]
                            if input_file[i][1] < input_file[j][1] or input_file[i][1] == input_file[j][1]:
                                num2 = input_file[j][1]
                            elif input_file[i][1] > input_file[j][1]:
                                num2 = input_file[i][1]
                            if (num1, num2) not in new_interval_list:
                                new_interval_list.append((num1, num2))

            #If the interval is mutually exclusive then add it to the new list
            elif num1 == 0 and num2 == 0 and j == len(input_file) - 1 and i == j:
                num1 = input_file[i][0]
                num2 = input_file[i][1]
                if (num1, num2) not in new_interval_list:
                    new_interval_list.append((num1, num2))

    return new_interval_list

def check_file(input_file):
    """
    Determines if there are any intervals that can be further collapsed.
    """

    check = True

    for i in range(0, len(input_file)):
        if check == False:
            break
        for j in range(1, len(input_file)):
            if input_file[i][0] >= 0:
                if input_file[i][0] >= input_file[j][0] and input_file[i][0] <= input_file[j][1] and i != j:
                    check = False
                    break
                else:
                    check = True
            elif input_file[i][0] < 0 and input_file[i][1] < 0:
                if i != j and ((input_file[i][0] >= input_file[j][0] and input_file[i][0] <= input_file[j][1]) or (input_file[i][1] >= input_file[j][0] and input_file[i][1] <= input_file[j][1])):
                    check = False
                    break
                else:
                    check = True
            elif input_file[i][0] < 0 and input_file[i][1] >= 0:
                if i != j and input_file[i][0] >= input_file[j][0] and input_file[i][0] <= input_file[j][1]:
                    check = False
                    break
                else:
                    check = True
    return check

def print_intervals(input_file):
    """
    Prints out the final output of all collapsed intervals by ascending order first then by ascending magnitudes.
    """

    input_list = []
    ordered_list = []
    diff_list = []

    #Prints intervals by ascending order of first number
    input_list = sorted(input_file)
    for item in range(len(input_list)):
        print(input_list[item])

    print()

    #Prints intervals by ascending magnitude
    for line in input_file:
        diff = abs(line[1] - line[0])
        diff_list.append(diff)

    for diff, interval in sorted(zip(diff_list, input_file)):
        ordered_list.append(interval)
    for item in range(len(ordered_list)):
        print(ordered_list[item])


if __name__ == "__main__":
    main()
