#File: BabyNames.py
#Description: This program creates a database of the 1000 most popular names in ever decade from 1900 to 2010 and outputs information that the user wants.
#Student's Name: Sahil Shah
#Student's UT EID: sbs2756
#Course Name: CS 313E
#Unique Number: 50205
#Date Created: 8 September 2019
#Date Last Modified: 12 September 2019

def main():

    name_dict = {}
    menu = []
    check = False
    decade_list = ["1900", "1910", "1920", "1930", "1940", "1950", "1960", "1970", "1980", "1990", "2000"]
    user_input = 0

    #Creating menu options
    with open("names.txt") as f:
        for row in f:
            row_split = row.split()
            name_dict[row_split[0]] = list(map(int, row_split[1:]))
    menu.append("Enter 1 to search for names.")
    menu.append("Enter 2 to display data for one name.")
    menu.append("Enter 3 to display all names that appear in only one decade.")
    menu.append("Enter 4 to display all names that appear in all decades.")
    menu.append("Enter 5 to display all names that are more popular in every decade.")
    menu.append("Enter 6 to display all names that are less popular in every decade.")
    menu.append("Enter 7 to quit.")

    #User inputs desired option
    while True:
        print("Options:")
        for option in range(len(menu)):
            print(menu[option])
        print()
        try:
            user_input = input("Enter choice: ")
            while user_input.isdigit() == False:
                user_input = input("Enter choice: ")
                if user_input.isdigit() == True and (int(user_input) > 7 or int(user_input) == 0):
                    user_input = "retry"
            if user_input.isdigit() == True:
                print()
            user_input = int(user_input)
        except ValueError:
            user_input = int(input("Enter choice: "))
        finally:
            if user_input == 1:
                names_search(name_dict, decade_list)
            elif user_input == 2:
                name_data(name_dict, decade_list)
            elif user_input == 3:
                one_decade(name_dict, decade_list)
            elif user_input == 4:
                all_decades(name_dict)
            elif user_input == 5:
                more_popular(name_dict)
            elif user_input == 6:
                less_popular(name_dict)
            elif user_input == 7:
                print()
                print("Goodbye.")
                break


def names_search(name_dict, decades_list):
    """
    Searches database to see if the user inputted name is in there.
    """

    years_list = []

    #Determines if name is in database
    name_input = input("Enter a name: ")
    print()
    if name_input in name_dict:
        name_values = name_dict[name_input]
        for value, year in sorted(zip(name_values, decades_list)):
            if value > 0:
                years_list.append(year)
        print("The matches with their highest ranking decade are:")
        print(name_input, years_list[0])
        print()
        return True
    else:
        print(name_input, "does not appear in any decade.")
        print()
        print()
        return False


def name_data(name_dict, decades_list):
    """
    Searches for name in database and if found outputs all its relevant information
    """

    #Prints data of inputted name for every decade
    name_input = input("Enter a name: ")
    print()
    if name_input in name_dict:
        name_list = name_dict[name_input]
        print(name_input + ":", (" ".join(map(str, name_dict[name_input]))))
        print(decades_list[0] + ":", name_list[0])
        print(decades_list[1] + ":", name_list[1])
        print(decades_list[2] + ":", name_list[2])
        print(decades_list[3] + ":", name_list[3])
        print(decades_list[4] + ":", name_list[4])
        print(decades_list[5] + ":", name_list[5])
        print(decades_list[6] + ":", name_list[6])
        print(decades_list[7] + ":", name_list[7])
        print(decades_list[8] + ":", name_list[8])
        print(decades_list[9] + ":", name_list[9])
        print(decades_list[10] + ":", name_list[10])
        print()
    else:
        print(name_input, "does not appear in any decade.")
        print()


def one_decade(name_dict, decades_list):
    """
    User inputs desired decade and all names that were in the top 1000 for that decade will be shown in order of rank.
    """

    value_list = []
    name_list = []

    #Input decade
    try:
        decade_input = input("Enter decade: ")
        while decade_input.isdigit() == False or int(decade_input) > 2000 or int(decade_input) < 1900 or int(decade_input) % 10 != 0:
            decade_input = input("Enter decade: ")
    except ValueError:
        decade_input = input("Enter decade: ")
    finally:
        if decade_input.isdigit() == False or int(decade_input) > 2000 or int(decade_input) < 1900 or int(decade_input) % 10 != 0:
            print()

        decade = decades_list.index(decade_input)

        for name in name_dict:
            name_values = name_dict[name]
            if name_values[decade] > 0 and name not in name_list:
                value_list.append(name_values[decade])
                name_list.append(name)
        #Prints ranking in descending order for inputted decade
        print("The names are in order of rank:")
        for value, item in sorted(zip(value_list, name_list)):
            print(item + ":", value)
        print()


def all_decades(name_dict):
    """
    Outputs all names that were in the top 1000 every decade.
    """

    names_list = []
    names_sum = 0

    #Determines names that appear in all decades
    for name in name_dict:
        name_values = name_dict[name]
        sum = 0
        for i in range(len(name_values)):
            if name_values[i] > 0:
                sum+=1
        if sum == 11:
            names_list.append(name)
            names_sum+=1
    name_list = sorted(names_list)
    #Prints names in alphabetic order
    print(names_sum, "names appear in every decade. The names are:")
    for item in names_list:
        print(item)
    print()


def more_popular(name_dict):
    """
    Outputs all names that got increasingly popular from each decade.
    """

    names_list = []
    names_sum = 0

    #Determines which names get more popular in every decade
    for name in name_dict:
        name_values = name_dict[name]
        sum = 0
        for i in range(1, len(name_values)):
            if name_values[i] > 0 and name_values[i] < name_values[i-1]:
                sum+=1
        if sum == 10:
            names_list.append(name)
            names_sum+=1

    #Prints names that get more popular in every decade
    print(names_sum, "names are more popular in every decade.")
    for item in sorted(names_list):
        print(item)
    print()


def less_popular(name_dict):
    """
    Outputs all names that got decreasingly popular from each decade.
    """

    names_list = []
    names_sum = 0

    #Determines which names get less popular in every decade
    for name in name_dict:
        name_values = name_dict[name]
        sum = 0
        check = False
        for i in range(1, len(name_values)):
            if name_values[i] > 0 and name_values[i] > name_values[i-1]:
                sum+=1
        if sum == 9 and name_values[10] == 0:
            sum+=1
        if sum == 10:
            names_list.append(name)
            names_sum+=1

    #Prints names that get less popular in every decade
    print(names_sum, "names are less popular in every decade.")
    for item in sorted(names_list):
        print(item)
    print()




if __name__ == "__main__":
    main()
