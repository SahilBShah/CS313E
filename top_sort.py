from collections import defaultdict

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

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

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []
    self.graph = defaultdict(list)

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)

      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)
    # the stack is empty let us reset the falgs
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

     # determine if a directed graph has a cycle
  def hasCycle (self):
       # create a Stack
      theStack = Stack()

      for i in range(len(self.Vertices)):
        # mark vertex v as visited and push on the stack
        (self.Vertices[i]).visited = True
        theStack.push (i)

        # vist other vertices according to depth
        while (not theStack.isEmpty()):
          # get an adjacent unvisited vertex
          u = self.getAdjUnvisitedVertex (theStack.peek())
          if (u == -1):
            u = theStack.pop()
          elif (self.adjMat[u][i] == 1):
              return True
          else:
            (self.Vertices[u]).visited = True
            theStack.push(u)
        # the stack is empty let us reset the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
          (self.Vertices[i]).visited = False

      return False

  def topologicalSortUtil(self,v,visited,stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        # Push current vertex to stack which stores result
        stack.insert(0,v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
  def topologicalSort(self):
    # Mark all the vertices as not visited
    visited = [False]*len(self.Vertices)
    stack =[]

    # Call the recursive helper function to store Topological
    # Sort starting from all vertices one by one
    for i in range(len(self.Vertices)):
        if visited[i] == False:
            self.topologicalSortUtil(i,visited,stack)

    # Print contents of the stack
    print(stack)
def main():
  # create a Graph object
  letters = Graph()

  # open file for reading
  inFile = open ("./topo.txt", "r")

  letter_dict = {}

  num_vertices = int(inFile.readline().strip())
  for i in range(num_vertices):
    letter = inFile.readline().strip()
    letters.addVertex(letter)
    letter_dict[letter] = i
    print(letter)

  num_edges = int(inFile.readline().strip())


  for i in range(num_edges):
    edges = inFile.readline().strip()
    print(edges)
    edges = edges.split()
    letters.addDirectedEdge(letter_dict[edges[0]],letter_dict[edges[1]], 1)

    # print the adjacency matrix
  print ("\nAdjacency Matric")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (letters.adjMat[i][j], end = ' ')
    print ()
  print ()

  # test if a directed graph has a cycle
  print(letters.hasCycle())

  letters.topologicalSort()
  # test topological sort

main()
