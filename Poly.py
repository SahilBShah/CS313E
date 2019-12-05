#  File: Poly.py
#  Description: This program uses linked lists to add and multiply two polynomials together.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 11 November 2019
#  Date Last Modified: 11 November 2019

class Link():
    def __init__(self, coeff=1, exp=1, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next
    def __str__(self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

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

    #insert element in the first index
    def insert_first(self, coeff, exp):
        new_link = Link(coeff, exp)
        new_link.next = self.first
        self.first = new_link

    #insert element in the second index
    def insert_last(self, coeff, exp):
        new_link = Link(coeff, exp)
        current = self.first
        if current == None:
            self.first = new_link
            return
        while current.next != None:
            current = current.next
        current.next = new_link

    #keep links in descending order of exponents
    def insert_in_order(self, coeff, exp):
        new_link = Link(coeff, exp)
        if self.first == None:
            new_link.next = self.first
            self.first = new_link
        elif self.first.exp <= new_link.exp:
            new_link.next = self.first
            self.first = new_link
        else:
            current = self.first
            while current.next != None and current.next.exp > new_link.exp:
                current = current.next
            new_link.next = current.next
            current.next = new_link

    #add polynomial p to this polynomial and return the sum
    def add(self, p):
        sum_list = LinkedList()
        current = self.first
        p_current = p.first
        if current == None:
            return p
        elif p_current == None:
            return self
        #Uses the smallest list to find sum of polynomials
        if self.get_num_links() <= p.get_num_links():
            while current != None and p_current != None:
                if current.exp == p_current.exp:
                    if current.coeff+p_current.coeff != 0:
                        sum_list.insert_in_order((current.coeff+p_current.coeff), current.exp)
                    current = current.next
                    p_current = p_current.next
                elif current.exp > p_current.exp:
                    if current.coeff != 0:
                        sum_list.insert_in_order(current.coeff, current.exp)
                    current = current.next
                elif current.exp < p_current.exp:
                    if p_current.coeff != 0:
                        sum_list.insert_in_order(p_current.coeff, p_current.exp)
                    p_current = p_current.next
        elif self.get_num_links() > p.get_num_links():
            while p_current != None and current != None:
                if current.exp == p_current.exp:
                    if current.coeff+p_current.coeff != 0:
                        sum_list.insert_in_order((current.coeff+p_current.coeff), current.exp)
                    current = current.next
                    p_current = p_current.next
                elif current.exp > p_current.exp:
                    if current.coeff != 0:
                        sum_list.insert_in_order(current.coeff, current.exp)
                    current = current.next
                elif current.exp < p_current.exp:
                    if p_current.coeff != 0:
                        sum_list.insert_in_order(p_current.coeff, p_current.exp)
                    p_current = p_current.next
        #If values aren't used from larger list, insert them into the sum list
        while current != None:
            if current.coeff != 0:
                sum_list.insert_in_order(current.coeff, current.exp)
            current = current.next
        while p_current != None:
            if p_current.coeff != 0:
                sum_list.insert_in_order(p_current.coeff, p_current.exp)
            p_current = p_current.next
        return sum_list

    #multiply polynomial p to this polynomial and return the product
    def mult(self, p):
        product_list = LinkedList()
        current = self.first
        p_current = p.first
        #Multiplying each integer by the others
        for first in range(p.get_num_links()):
            coef = current.coeff * p_current.coeff
            exponent = current.exp + p_current.exp
            product_list.insert_in_order(coef, exponent)
            p_current = p_current.next
        for i in range(self.get_num_links()-1):
            current = current.next
            p_current = p.first
            for j in range(p.get_num_links()):
                coef = current.coeff * p_current.coeff
                exponent = current.exp + p_current.exp
                product_list.insert_in_order(coef, exponent)
                p_current = p_current.next
        #Adding integers that contain the same exponent
        fin_prod_list = LinkedList()
        follow = product_list.first
        if follow.next != None:
            lead = product_list.first.next
        else:
            return product_list
        tmp_list = []
        while lead != None:
            if follow.exp == lead.exp:
                if tmp_list == []:
                    tmp_list.append([follow.coeff+lead.coeff, follow.exp])
                elif tmp_list[-1][1] == lead.exp:
                    tmp_list.append([tmp_list[-1][0]+lead.coeff, lead.exp])
                if lead.next == None:
                    if tmp_list[-1][0] != 0:
                        fin_prod_list.insert_in_order(tmp_list[-1][0], tmp_list[-1][1])
            else:
                if tmp_list == []:
                    if follow.coeff != 0:
                        fin_prod_list.insert_in_order(follow.coeff, follow.exp)
                else:
                    if tmp_list[-1][0] != 0:
                        fin_prod_list.insert_in_order(tmp_list[-1][0], tmp_list[-1][1])
                    tmp_list = []
                if lead.next == None:
                    if lead.coeff != 0:
                        fin_prod_list.insert_in_order(lead.coeff, lead.exp)
            follow = follow.next
            lead = lead.next
        return fin_prod_list

    #create a string representation of the polynomial
    def __str__(self):
        out = []
        count = self.get_num_links()
        num_lines = count % 10
        current = self.first
        out.append('(' + str(current.coeff) + ', ' + str(current.exp) + ')')
        for i in range(1, count):
            if current.next != None:
                current = current.next
                out.append('(' + str(current.coeff) + ', ' + str(current.exp) + ')')
        return ' + '.join(out)

def main():
    #open file poly.txt for reading
    file = open('poly.txt', 'r')

    #create polynomial p
    p = LinkedList()
    line = int(file.readline())
    for i in range(line):
        line = file.readline()
        line = line.strip()
        line = line.split()
        p.insert_in_order(int(line[0]), int(line[1]))

    #create polynomial q
    q = LinkedList()
    line = file.readline()
    line = int(file.readline())
    for i in range(line):
        line = file.readline()
        line = line.strip()
        line = line.split()
        q.insert_in_order(int(line[0]), int(line[1]))

    #get sum of p and q and print sum
    print('Sum:', p.add(q))
    print()

    #get product of p and q and print product
    print('Product:', p.mult(q))


if __name__ == '__main__':
    main()
