class Stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        self.stack.pop()

def is_valid(push_list, pop_list):
    if len(push_list) != len(pop_list):
        return False
    theStack = Stack()
    for i in range(len(push_list)):
        theStack.push(push_list[i])
        if pop_list[0] == push_list[i]:
            theStack.pop()
            pop_list.pop(0)
    while len(theStack.stack) != 0:
        if theStack.stack[-1] == pop_list[0]:
            theStack.pop()
            pop_list.pop(0)
        else:
            return False
    return True

def main():
    push = [1,2,3,4]
    pop = [2,4,3,1]
    print(is_valid(push, pop))

main()
