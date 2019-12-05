class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

  def __str__ (self):
    s=''
    for i in range (self.size()):
      s+=str(self.queue[i])+' '
    return s

class Node (object):
    def __init__ (self, data):
        self.data=data
        self.lChild=None
        self.rChild=None

    def __str__ (self):
      return str(self.data)

class Tree (object):
  def __init__ (self):
    self.root = None

  # Search for a node with the key
  def find (self, key):
    current = self.root

    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode

    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
            current = current.lChild
        else:
            current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # In order traversal - left, center, right
  def inOrder (self, aNode, data):
    if (aNode != None):
      self.inOrder (aNode.lChild, data)
      data.append(aNode.data)
      self.inOrder (aNode.rChild, data)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode, data):
    if (aNode != None):
      data.append(aNode.data)
      self.preOrder (aNode.lChild, data)
      self.preOrder (aNode.rChild, data)

  # Post order traversal - left, right, center
  def postOrder (self, aNode, data):
    if (aNode != None):
      self.postOrder (aNode.lChild, data)
      self.postOrder (aNode.rChild, data)
      data.append(aNode.data)

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent

  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
          deleteNode = deleteNode.lChild
          isLeft = True
      else:
          deleteNode = deleteNode.rChild
          isLeft = False

    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None):
        successorParent = successor
        successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
        successor.rChild = deleteNode.rChild

  # Returns true if two binary trees are similar
  def isSimilar (self, other):

    if self.numNodes()==other.numNodes():

        data1=[]
        data2=[]
        count=0
        self.preOrder(self.root, data1)
        other.preOrder(other.root, data2)

        for i in range (self.numNodes()):
          if data1[i]==data2[i]:
            count+=1

        return count==self.numNodes()

    else:
      return False

  # Prints out all nodes at the given level
  def printLevel (self, level):

    if level>self.getHeight() or level<1:
      print ('level '+str(level)+': ')
      return

    que=Queue()
    current=self.root
    que.enqueue(current.data)

    if level==1:
      print ('level '+str(level)+': '+str(que))
      return

    count=1

    while que.isEmpty()==False:

      que.dequeue()

      if current.lChild!=None:
        que.enqueue(current.lChild.data)

      if current.rChild!=None:
        que.enqueue(current.rChild.data)

      queOrd=que.queue

      queOrd=sorted (queOrd)

      if queOrd==que.queue:
        count+=1

      if count==level:
        print ('level '+str(level)+': '+str(que))
        return

      current=self.find(que.queue[0])

  # Returns the height of the tree
  def getHeight (self):

    if self.numNodes()==0:
      return -1

    current=self.root

    if current.lChild!=None or current.rChild!=None:

      data=[]
      self.preOrder(self.root, data)

      treeL=Tree()
      treeR=Tree()

      for i in range (self.numNodes()):
        if data[i]<current.data:
          treeL.insert(data[i])

        if data[i]>current.data:
          treeR.insert(data[i])

      data1=[]
      data2=[]
      treeL.preOrder(treeL.root, data1)
      treeR.preOrder(treeR.root, data2)

      if treeL.getHeight()>treeR.getHeight():

        return treeL.getHeight()+1

      return treeR.getHeight()+1

    return 0

  # Returns the number of nodes in the tree
  # (left subtree and the number of nodes in the right subtree)
  def numNodes (self):

    if self.root==None:
      return 0

    else:
      data=[]
      self.preOrder(self.root, data)

      treeL=Tree()
      treeR=Tree()

      for i in range (len(data)):
        if data[i]<self.root.data:
          treeL.insert(data[i])

        if data[i]>self.root.data:
          treeR.insert(data[i])

      return treeL.numNodes()+treeR.numNodes()+1

def main():
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
  print(tree1.isSimilar(tree2))
  #Print the various levels of two of the three trees that are different
  tree1.printLevel(5)
  tree1.printLevel(3)
  tree3.printLevel(5)
  tree3.printLevel(3)

  #Get the height of two trees that are different
  print(tree1.getHeight())
  print(tree3.getHeight())

  #Get the total number of nodes in a binary search tree
  print(tree1.numNodes())
  print(tree2.numNodes())
  print(tree3.numNodes())

main()
