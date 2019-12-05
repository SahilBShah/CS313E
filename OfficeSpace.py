#  File: OfficeSpace.py
#  Description: This program allocates the appropriate amount of space for each person and employee by determining if the spaces requested overlap one another.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 21 September 2019
#  Date Last Modified: 23 September 2019

def main():

    global space_left
    row_list = []
    personal_list = []
    employee_list = []
    space_left = {}
    employee_space = {}

    #Import file
    in_file = open('office.txt', 'r')
    line = in_file.readline()
    line = line.strip()
    line = line.split()
    row_list.append([line[0], line[1]])
    num_people = in_file.readline()
    num_people = num_people.strip()
    row_list.append([num_people])
    for i in range(int(num_people)):
        line = in_file.readline()
        line = line.strip()
        line = line.split()
        row_list.append([line[0], line[1], line[2], line[3], line[4]])

    #Creates list with only the "employee's" info
    line = in_file.readline()
    line = line.strip()
    line = line.split()
    employee_list.append([line[0], line[1]])
    num_employees = in_file.readline()
    num_employees = num_employees.strip()
    employee_list.append([num_employees])
    for j in range(int(num_employees)):
        line = in_file.readline()
        line = line.strip()
        line = line.split()
        employee_list.append([line[0], line[1], line[2], line[3], line[4]])

    set_up(row_list, space_left)
    print()
    set_up(employee_list, employee_space)


def set_up(row_list, dict):
    """
    Calculates all values (total, unallocated, and contested space) regardless of type of person.
    """

    start = 0

    total_square_feet = int(row_list[0][0]) * int(row_list[0][1])
    print("Total", total_square_feet)

    #Creates an initial dictionary with each person and the area requested
    for a in range(2, int(row_list[1][0])+2):
        name_area = (int(row_list[a][3]) - int(row_list[a][1])) * (int(row_list[a][4]) - int(row_list[a][2]))
        dict.update({row_list[a][0]: name_area})

    conflicting_area = calc_requested_space(row_list, dict)

    #Determines how much space conflicts with each other and subtracts the total by the space requested and space conflicting
    for b in range(2, int(row_list[1][0])+2):
        total_square_feet -= list(dict.items())[start][1]
        start+=1
    total_square_feet -= conflicting_area
    print("Unallocated", total_square_feet)
    print("Contested", conflicting_area)

    start = 0

    #Prints out the space allocated for each person
    for c in range(2, int(row_list[1][0])+2):
        print(row_list[c][0], list(dict.items())[start][1])
        if start < len(list(dict)):
            start+=1


def make_grid(rows, columns):
    """
    Creates a grid of zeroes determined by inputted specifications.
    """

    working_grid = [[0 for i in range(columns)] for j in range(rows)]
    return working_grid


def calc_requested_space(row_list, dict):
    """
    Calculates the amount of space that conflicts between requests.
    """

    total_area = 0

    for x in range(2, int(row_list[1][0])+2):
        for y in range(x+1, int(row_list[1][0])+2):

            if row_list[x] != row_list[y]:
                tmp_grid = make_grid(int(row_list[0][0]), int(row_list[0][1]))
                area = 0

                for i in range(int(row_list[x][1]), int(row_list[x][3])):
                    for j in range(int(row_list[x][2]), int(row_list[x][4])):
                        tmp_grid[i][j] += 1

                for i in range(int(row_list[y][1]), int(row_list[y][3])):
                    for j in range(int(row_list[y][2]), int(row_list[y][4])):
                        tmp_grid[i][j] += 1

                for a in range(len(tmp_grid)):
                    for b in range(len(tmp_grid[0])):
                        if tmp_grid[a][b] == 2:
                            total_area += 1
                            area += 1
                calc_personal_space(row_list, x, y, area, dict)
    return total_area


def calc_personal_space(row_list, x, y, area, dict):
    """
    Calculates the amount of area each person receives.
    """

    global dictionary
    dictionary = dict

    name1 = row_list[x][0]
    name2 = row_list[y][0]
    name1_area = dictionary[name1] - area
    name2_area = dictionary[name2] - area
    dictionary.update({row_list[x][0]: name1_area, row_list[y][0]: name2_area})


if __name__ == "__main__":
    main()
