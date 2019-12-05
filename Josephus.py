#  File: Josephus.py
#  Description: This program uses the Circular Linked Lists data structure to solve the infamous Josephus problem.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 1 November 2019
#  Date Last Modified: 4 November 2019

class Link():

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularList():

    #constructor
    def __init__(self):
        self.first = None
        self.lst = []

    #Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        current = self.first
        if current == None:
            self.first = new_link
            new_link.next = self.first
            return
        else:
            current = self.first
            while current.next != self.first:
                current = current.next
            current.next = new_link
            new_link.next = self.first

    #Find the link with the given data
    def find(self, data):
        current = self.first
        while current.data != data:
            current = current.next
        return current

    #Delete a link with a given data (value)
    def delete(self, data):
        previous = None
        current = self.first
        while current:
            if current.data == data and current == self.first:
                if current.next == self.first:
                    current = None
                    self.first = None
                    return
                else:
                    while current.next != self.first:
                        current = current.next
                    current.next = self.first.next
                    self.first = self.first.next
                    current = None
                    return
            elif current.data == data:
                previous.next = current.next
                current = None
                return
            else:
                if current.next == self.first:
                    break
            previous = current
            current = current.next

    #Delete the nth link starting from the Link start. Return the next link from the deleted link.
    def delete_after(self, start, n):
        current = self.find(start)
        for i in range(n-1):
            current = current.next
        self.delete(current.data)
        self.lst.append(str(current.data))
        return current.next

    #Return a string representation of a circular list
    def __str__(self):
        return '\n'.join(self.lst)

def main():

    #Open file and import intergers
    file = open('josephus.txt', 'r')
    line = file.readline()
    line = line.strip()
    num_soldiers = int(line)
    line = file.readline()
    line = line.strip()
    start_sold = int(line)
    line = file.readline()
    line = line.strip()
    increment = int(line)

    #Close the file
    file.close()

    #Initiate circular linked list
    lineup = CircularList()
    for i in range(1, num_soldiers+1):
        lineup.insert(i)
    #Determine order of soldiers killed
    new_start = lineup.delete_after(start_sold, increment)
    for i in range(num_soldiers-1):
        new_start = lineup.delete_after(new_start.data, increment)
    print(lineup)

main()
