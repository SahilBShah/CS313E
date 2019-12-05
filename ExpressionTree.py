#  File: ExpressionTree.py
#  Description: This program evaluates and expression and converts the infix notation to post and prefix notations using a binary search tree.
#  Student's Name: Sahil Shah
#  Student's UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 13 November 2019
#  Date Last Modified: 14 November 2019

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def peek(self):
        return self.stack[-1]

class Node():
    def __init__(self, data=''):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree():
    def __init__(self):
        self.root = Node()
        self.current = self.root
        self.expr_stack = Stack()

    def create_tree(self, expr):
        for token in expr:
            if token == '(':
                self.current.lchild = Node()
                self.expr_stack.push(self.current)
                self.current = self.current.lchild
            elif token in ['+', '-', '*', '/', '//', '%', '**']:
                self.current.data = token
                self.expr_stack.push(self.current)
                self.current.rchild = Node()
                self.current = self.current.rchild
            elif token not in ['+', '-', '*', '/', '//', '%', '**', '(', ')']:
                self.current.data = token
                self.current = self.expr_stack.pop()
            elif token == ')':
                if self.expr_stack.size() != 0:
                    self.current = self.expr_stack.pop()

    #Evaluates the expression and ouputs the answer in int or float format
    def evaluate(self, aNode):
        stack = Stack()
        expr_list = []
        self.eval_post_fix(aNode, expr_list)
        for i in range(len(expr_list)):
            if expr_list[i] == '':
                expr_list.pop(i)
        for token in expr_list:
            if token in ['+', '-', '*', '/', '//', '%', '**']:
                oper2 = stack.pop()
                oper1 = stack.pop()
                stack.push(self.operate(oper1, oper2, token))
            else:
                stack.push(float(token))
        return float(stack.peek())

    #Operations that can be performed
    def operate(self, oper1, oper2, token):
        if token == '+':
            return oper1 + oper2
        elif token == '-':
            return oper1 - oper2
        elif token == '*':
            return oper1 * oper2
        elif token == '/':
            return oper1 / oper2
        elif token == '//':
            return oper1 // oper2
        elif token == '%':
            return oper1 % oper2
        elif token == '**':
            return oper1 ** oper2

    #Convert expression to post fix so that it ie easier to evaluate
    def eval_post_fix(self, aNode, post_list):
        if aNode != None:
            self.eval_post_fix(aNode.lchild, post_list)
            self.eval_post_fix(aNode.rchild, post_list)
            post_list.append(aNode.data)

    #Traverses the tree in pre order: Goes to the root, then left, then right
    def pre_order(self, aNode):
        if aNode != None:
            print(aNode.data, end=' ')
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    #Traverses the tree in post order: Goes to the left, then right, then root
    def post_order(self, aNode):
        if aNode != None:
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data, end=' ')


def main():

    #Open file
    file = open('expression.txt', 'r')
    #Read in lines
    line = file.readline()
    line = line.strip()
    expression = line
    line = line.split()
    #Close file
    file.close()
    #Create tree
    tree = Tree()
    tree.create_tree(line)
    #Evaluate the expression
    print(str(expression) + str(' = '), end='')
    print(tree.evaluate(tree.root))
    print()
    #Convert infix to prefix notation
    print('Prefix Expression: ', end='')
    tree.pre_order(tree.root)
    print()
    print()
    #Convert infix to postfix notation
    print('Postfix Expression:', end=' ')
    tree.post_order(tree.root)
    print()

main()
