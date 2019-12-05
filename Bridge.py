#File: Bridge.py
#Description: This program
#Student's Name: Sahil Shah
#Student's UT EID: sbs2756
#Course Name: CS 313E
#Unique Number: 50205
#Date Created: 30 September 2019
#Date Last Modified: 3 October 2019

def main():

    people = []

    with open("bridge.txt") as f:
        for row in f:
            row_split = row.split()
            if row_split != []:
                people.append(row_split)
    #Number of test cases are found
    test_case = int(people[0][0])
    people.pop(0)
    for i in range(test_case):
        cross_times = []
        cross_times2 = []
        count_pop = 0
        #For each test case, the speeds for each person is added to a list
        for j in range(int(people[0][0])):
            cross_times.append(people[j+1][0])
            cross_times2.append(people[j+1][0])
            count_pop+=1
        #Removes each value in the list related to each test case
        for count in range(count_pop+1):
            people.pop(0)
        #Converts the list of strings to a list of ints
        for num in range(len(cross_times)):
            cross_times[num] = int(cross_times[num])
            cross_times2[num] = int(cross_times2[num])
        time1 = get_min_time(cross_times)
        cross_times2.sort()
        time2 = second_strategy(cross_times2)
        if time1 <= time2:
            print(time1)
        else:
            print(time2)
        print()


def get_min_time(times):
    """
    Returns the shortest amount of time it takes everyone to cross the bridge.
    """

    times.sort()
    total_time = 0
    crossed_bridge = []

    if len(times) == 1:
        return times[0]
    elif len(times) == 2:
        return times[1]
    else:
        while times != []:
            values = calc_time(times, crossed_bridge)
            total_time += values[0]
            times = values[1]
            crossed_bridge = values[2]
            if len(times) == 2:
                total_time+=get_min_time(times)
                break

    return total_time


def calc_time(times, people_crossed):
    """
    Calculates the amount of time it takes for the two fastest, two slowest, and the fastest person on the other side of the bridge to cross the bridge.
    """

    total_time = 0

    total_time += times[0] + times[1]
    total_time += times[-1]
    people_crossed.append(times[1])
    people_crossed.append(times[-2])
    people_crossed.append(times[-1])
    times.pop(1)
    times.pop(-1)
    times.pop(-1)
    if times != [] and len(times) != 2:
        total_time += min(people_crossed)
        people_crossed.sort()
        times.append(people_crossed[0])
        people_crossed.pop(0)
    people_crossed.sort()
    times.sort()
    return(total_time, times, people_crossed)


def second_strategy(times):
    """
    Second strategy where fastest person takes everyone across the bridge.
    """

    total_time2 = 0
    crossed_bridge = []

    if len(times) == 1:
        return times[0]
    elif len(times) == 2:
        return times[1]
    else:
        while times != []:
            total_time2 += times[0] + times[1]
            crossed_bridge.append(times[1])
            times.pop(1)
            if len(times) == 2:
                total_time2 += max(times)
                break

    return total_time2


if __name__ == "__main__":
    main()
