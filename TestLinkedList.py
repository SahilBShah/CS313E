#  File: TestLinkedList.py
#  Description: This program creates the Linked Lists data structure.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 30 October 2019
#  Date Last Modified: 1 November 2019

class Link():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.first = None

    #get number of links
    def get_num_links(self):
        num_links = 0
        if self.first == None:
            return 0
        else:
            current = self.first
            while current != None:
                num_links+=1
                current = current.next
            return num_links

    #add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    #add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)
        current = self.first
        if current == None:
            self.first = new_link
            return
        while current.next != None:
            current = current.next
        current.next = new_link

    #add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        new_link = Link(data)
        lead = self.first.next
        follow = self.first
        if lead == None:
            if follow.data < new_link.data:
                self.insert_last(data)
            elif follow.data >= new_link.data:
                self.insert_first(data)
        elif follow == None:
            self.insert_first(data)
        elif new_link.data <= self.first.data:
            self.insert_first(data)
        else:
            while lead.data <= new_link.data:
                lead = lead.next
                follow = follow.next
                if lead == None:
                    self.insert_last(data)
                    break
            follow.next = new_link
            new_link.next = lead

    #search in an unordered list, return None if not found
    def find_unordered(self, data):
        new_link = Link(data)
        if self.get_num_links() == 0:
            return None
        current = self.first
        if current.data == new_link.data:
            return new_link
        else:
            while current.data != new_link.data:
                current = current.next
                if current == None:
                    return None
                elif current.data == new_link.data:
                    return new_link

    #search in an ordered list, return None if not found
    def find_ordered(self, data):
        new_link = Link(data)
        if self.get_num_links() == 0:
            return None
        current = self.first
        if current.data == new_link.data:
            return new_link
        else:
            while current.data != new_link.data and current.data < new_link.data:
                current = current.next
                if current == None or current.data > new_link.data:
                    return None
                elif current.data == new_link.data:
                    return new_link

    #delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next
        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return current

    #string representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        out = []
        start = 1
        count = self.get_num_links()
        num_lines = count % 10
        current = self.first
        out.append(str(current.data) + '  ')
        for i in range(1, count):
            start+=1
            if current.next != None:
                current = current.next
                out.append(str(current.data) + '  ')
                if start % 10 == 0:
                    out.append('\n')
        return ''.join(out)

    #copy the contents of a list and return new list
    def copy_list(self):
        new_list = LinkedList()
        if self.get_num_links() == 0:
            return new_list
        count = self.get_num_links()
        current = self.first
        new_list.insert_first(current.data)
        for i in range(1, count):
            current = current.next
            new_list.insert_last(current.data)
        return new_list

    #reverse the contents of a list and return new list
    def reverse_list(self):
        new_list = LinkedList()
        if self.get_num_links() == 0:
            return new_list
        count = self.get_num_links()
        current = self.first
        new_list.insert_first(current.data)
        for i in range(1, count):
            if current.next != None:
                current = current.next
                new_list.insert_first(current.data)
        return new_list

    #sort the contents of the list in ascending order and return new list
    def sort_list(self):
        new_list = LinkedList()
        if self.get_num_links() == 0:
            return new_list
        count = self.get_num_links()
        current = self.first
        new_list.insert_first(current.data)
        for i in range(1, count):
            if current.next != None:
                current = current.next
                new_list.insert_in_order(current.data)
        return new_list

    #return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        if self.get_num_links() == 1:
            return True
        lead = self.first.next
        follow = self.first
        if lead.data < follow.data:
            return False
        else:
            while lead != None:
                lead = lead.next
                follow = follow.next
                if lead != None:
                    if lead.data < follow.data:
                        return False
            return True

    #return True if a list is empty or False otherwise
    def is_empty(self):
        if self.first == None:
            return True
        return False

    #merge two sorted lists and retrun new list in ascending order
    def merge_list(self, other):
        if self.get_num_links() == 0:
            return other.sort_list()
        elif other.get_num_links() == 0:
            return self.sort_list()
        merge_list = LinkedList()
        if self.get_num_links() == 0 and other.get_num_links() == 0:
            return merge_list
        count1 = self.get_num_links()
        count2 = other.get_num_links()
        current1 = self.first
        current2 = other.first
        merge_list.insert_first(current1.data)
        merge_list.insert_in_order(current2.data)
        for i in range(1, count1):
            if current1.next != None:
                current1 = current1.next
                merge_list.insert_in_order(current1.data)
        for j in range(1, count2):
            if current2.next != None:
                current2 = current2.next
                merge_list.insert_in_order(current2.data)
        return merge_list

    #test if two lists are equal, item by item and return True
    def is_equal(self, other):
        current1 = self.first
        current2 = other.first
        if self.get_num_links() == 0 and other.get_num_links() > 0 or self.get_num_links() > 0 and other.get_num_links() == 0:
            return False
        elif self.get_num_links() == 1 and other.get_num_links() == 1 and self.data == other.data:
            return True
        elif current1.data != current2.data:
            return False
        else:
            while current1 != None or current2 != None:
                current1 = current1.next
                current2 = current2.next
                if current1 != None and current2 != None:
                    if current1.data != current2.data:
                        return False
            return True

    #return a new list, keeping only the first occurence of an element and removing all duplicates. Do not change the order of the elements
    def remove_duplicates(self):
        new_list = LinkedList()
        if self.get_num_links() == 0:
            return new_list
        tmp_list = []
        count = self.get_num_links()
        current = self.first
        tmp_list.append(current.data)
        if current.next != None:
            for i in range(1, count):
                if current.next != None:
                    current = current.next
                    if current.data not in tmp_list:
                        tmp_list.append(current.data)
            new_list.insert_first(tmp_list[0])
            for j in range(1, len(tmp_list)):
                new_list.insert_last(tmp_list[j])
        else:
            new_list.insert_first(tmp_list[0])
        return new_list


def main():

    #Test methods insert_first() and __str__() by adding more than 10 items to a list and printing it.
    nums = LinkedList()
    edge = LinkedList()
    edge.insert_first(0)
    nums.insert_first(11)
    nums.insert_first(10)
    nums.insert_first(9)
    nums.insert_first(8)
    nums.insert_first(7)
    nums.insert_first(6)
    nums.insert_first(5)
    nums.insert_first(4)
    nums.insert_first(3)
    nums.insert_first(2)
    nums.insert_first(1)
    print(nums)

    #Test method insert_last()
    nums.insert_last(20)
    print(nums)

    #Test method insert_in_order()
    nums.insert_in_order(10)
    nums.insert_in_order(21)
    nums.insert_in_order(0)
    edge.insert_in_order(1)
    print(nums)
    print(edge)

    #Test method get_num_links()
    print(nums.get_num_links())

    #Test method find_unordered() - Consider two cases: data is there and data is not there
    unordered = LinkedList()
    unordered.insert_first(5)
    unordered.insert_last(3)
    unordered.insert_last(7)
    unordered.insert_last(1)
    print(unordered.find_unordered(3))
    print(unordered.find_unordered(4))

    #Test method find_ordered() - Consider two cases: data is there and data is not there
    print(nums.find_ordered(3))
    print(nums.find_ordered(23))

    #Test method delete_link() - Consider two cases: data is there and data is not there
    nums.delete_link(21)
    nums.delete_link(50)
    print(nums)

    #Test method copy_list
    copied = nums.copy_list()
    print(copied)

    #Test method reverse_list()
    rev = copied.reverse_list()
    print(rev)

    #Test method sort_list()
    in_order = unordered.sort_list()
    print(in_order)


    #Test method is_sorted() - Consider two cases: list is sorted and list is not sorted
    print(in_order.is_sorted())
    print(unordered.is_sorted())
    single = LinkedList()
    single.insert_last(5)
    print(single.is_sorted())

    #Test method is_empty()
    empty = LinkedList()
    print(empty.is_empty())
    print(single.is_empty())
    print(nums.is_empty())

    #Test method merge_list()
    merged = nums.merge_list(unordered)
    print(merged)

    #Test method is_equal() - Consider two cases: lists are equal and lists are not equal
    print(nums.is_equal(copied))
    print(nums.is_equal(unordered))
    print(nums.is_equal(empty))

    #Test remove_duplicates()
    no_duplicates = merged.remove_duplicates()
    print(no_duplicates)

if __name__ == '__main__':
    main()
