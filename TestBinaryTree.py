#  File: TestBinaryTree.py
#  Description: This program adds functionality to the binary search tree data structure.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 19 November 2019
#  Date Last Modified: 21 November 2019

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

class Node():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree():
    def __init__(self):
        self.root = None

    #Insert data into the tree
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while current != None:
                parent = current
                if data < current.data:
                    current = current.lchild
                else:
                    current = current.rchild
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    #In order traversal - left, center, right
    def in_order(self, aNode, lst):
        if aNode != None:
            self.in_order(aNode.lchild, lst)
            lst.append(aNode.data)
            self.in_order(aNode.rchild, lst)

    #Pre order traversal
    def pre_order(self, aNode, lst):
        if aNode != None:
            lst.append(aNode.data)
            self.pre_order(aNode.lchild, lst)
            self.pre_order(aNode.rchild, lst)

    #Post order traversal
    def post_order(self, aNode):
        if aNode != None:
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data)

    #Find the node with the minimum key
    def find_min(self):
        current = self.root
        parent = self.root
        while current != None:
            parent = current
            current = current.lchild
        return parent

    #Find the node with the maximum key
    def find_max(self):
        current = self.root
        parent = self.root
        while current != None:
            parent = current
            current = current.rchild
        return parent

    #Search for a node with given data
    def search(self, data):
        current = self.root
        while current != None and current.data != data:
            if data < current.data:
                current = current.lchild
            else:
                current = current.rchild
        return current

    #Delete a node with given data
    def delete(self, data):
        delete_node = self.root
        parent = self.root
        is_left = False
        #If empty tree
        if delete_node == None:
            return None
        #Find the data if it exists
        while delete_node != None and delete_node.data != data:
            parent = delete_node
            if data < delete_node.data:
                delete_node = delete_node.lchild
                is_left = True
            else:
                delete_node = delete_node.rchild
                is_left = False
        #If node is not found
        if delete_node == None:
            return None
        #Check if the delete node is a leaf node
        if delete_node.lchild == None and delete_node.rchild == None:
            if delete_node == self.root:
                self.root = None
            elif is_left:
                parent.lchild = None
            else:
                parent.rchild = None
        #Check if the delete node is a node with only one left child
        elif delete_node.rchild == None:
            if delete_node == self.root:
                self.root = delete_node.lchild
            elif is_left:
                parent.lchild = delete_node.lchild
            else:
                parent.rchild = delete_node.lchild
        #Check if a delete node is a node with only one right child
        elif delete_node.lchild == None:
            if (delete_node == self.root):
                self.root = delete_node.rchild
            elif (is_left):
                parent.lchild = delete_node.rchild
            else:
                parent.rchild = delete_node.rchild
        return delete_node

    #Returns True if two binary trees are similar
    def is_similar(self, pNode):
        if self.num_nodes() == pNode.num_nodes():
            #Initialize variables needed
            values_lst1 = []
            values_lst2 = []
            count = 0
            #Get values from tree
            self.pre_order(self.root, values_lst1)
            pNode.pre_order(pNode.root, values_lst2)
            #Check if values are equal to one another
            for i in range(len(values_lst1)):
                if values_lst1[i] == values_lst2[i]:
                    count += 1
            if count == len(values_lst1):
                return True
            else:
                return False
        else:
            return False

    #Prints out all nodes at the given level
    def print_level(self, level):
        if level < 1 or level > self.get_height():
            print ('Level '+ str(level) + ': ' + 'This level does not exist')
            return
        else:
            current = self.root
            queue = Queue()
            queue.enqueue(current.data)
            count = 0
            if level == 1:
                print ('Level ' + str(level) + ': ' + str(queue.queue)[1:-1])
                return
            count += 1
            while queue.size() != 0:
                queue.dequeue()
                if current.lchild != None:
                    queue.enqueue(current.lchild.data)
                if current.rchild != None:
                    queue.enqueue(current.rchild.data)
                order = sorted(queue.queue)
                if order == queue.queue:
                    count+=1
                if count == level:
                    print ('Level ' + str(level) + ': ' + str(queue.queue)[1:-1])
                    return
                current = self.search(queue.queue[0])


    #Returns the height of the tree
    def get_height(self):
        current = self.root
        if self.root == None:
            return 0
        elif current.lchild != None or current.rchild != None:
            val_lst = []
            left_tree = Tree()
            right_tree = Tree()
            self.pre_order(self.root, val_lst)

            for i in range(self.num_nodes()):
                if val_lst[i] < current.data:
                    left_tree.insert(val_lst[i])
                if val_lst[i] > current.data:
                    right_tree.insert(val_lst[i])

            left_lst = []
            left_tree.pre_order(left_tree.root, left_lst)
            right_lst = []
            right_tree.pre_order(right_tree.root, right_lst)

            if left_tree.get_height() > right_tree.get_height():
                return left_tree.get_height() + 1
            else:
                return right_tree.get_height() + 1
        else:
            return 0

    #Returns the number of nodes in the left subtree and the number of nodes in the right subtree and the root
    def num_nodes(self):
        if self.root == None:
            return 0
        else:
            val_lst = []
            left_tree = Tree()
            right_tree = Tree()
            self.pre_order(self.root, val_lst)
            for i in range(len(val_lst)):
                if val_lst[i] < self.root.data:
                    left_tree.insert(val_lst[i])
                if val_lst[i] > self.root.data:
                    right_tree.insert(val_lst[i])
            return left_tree.num_nodes() + right_tree.num_nodes() + 1

def main():

    #Create three trees - two are the same and the third is different
    tree1 = Tree()
    tree1.insert(50)
    tree1.insert(30)
    tree1.insert(70)
    tree1.insert(10)
    tree1.insert(40)
    tree1.insert(60)
    tree1.insert(80)
    tree1.insert(7)
    tree1.insert(25)
    tree1.insert(38)
    tree1.insert(47)
    tree1.insert(58)
    tree1.insert(65)
    tree1.insert(77)
    tree1.insert(96)
    tree2 = Tree()
    tree2.insert(50)
    tree2.insert(30)
    tree2.insert(70)
    tree2.insert(10)
    tree2.insert(40)
    tree2.insert(60)
    tree2.insert(80)
    tree2.insert(7)
    tree2.insert(25)
    tree2.insert(38)
    tree2.insert(47)
    tree2.insert(58)
    tree2.insert(65)
    tree2.insert(77)
    tree2.insert(96)
    tree3 = Tree()
    tree3.insert(60)
    tree3.insert(30)
    tree3.insert(80)
    tree3.insert(40)
    tree3.insert(20)
    tree3.insert(64)
    tree3.insert(3)
    tree3.insert(5)
    tree3.insert(10)
    tree3.insert(55)
    tree3.insert(36)
    tree3.insert(97)


    #Test method is_similar
    print(tree1.is_similar(tree2))
    print(tree1.is_similar(tree3))

    #Print the various levels of two of the three trees that are different
    tree1.print_level(5)
    tree1.print_level(3)
    tree1.print_level(1)
    tree1.print_level(0)
    tree3.print_level(5)
    tree3.print_level(4)
    tree3.print_level(3)

    #Get the height of two trees that are different
    print(tree1.get_height())
    print(tree3.get_height())

    #Get the total number of nodes in a binary search tree
    print(tree1.num_nodes())
    print(tree2.num_nodes())
    print(tree3.num_nodes())

if __name__ == '__main__':
    main()
