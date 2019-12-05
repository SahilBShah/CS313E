#  File: Graph.py
#  Description: This program creates and implements the Graph datastructure.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 24 November 2019
#  Date Last Modified: 24 November 2019

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (not self.has_vertex (label)):
      self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    #create the Queue
    queue = Queue ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    queue.enqueue (v)

    # visit all the other vertices according to depth
    while (not queue.is_empty()):
      del_vertex = queue.dequeue()
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (del_vertex)
      while (u != -1):
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        queue.enqueue (u)
        u = self.get_adj_unvisited_vertex (del_vertex)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  #determines if the graph is directed or undirected
  def graph_type(self):
    is_directed = False
    for i in range(len(self.adjMat)):
      row = self.adjMat[i]
      col = []
      for j in range(len(self.adjMat)):
        col.append(self.adjMat[i][j])
      if row == col:
        continue
      else:
        is_directed = True
        return is_directed
    return is_directed

  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    row = self.get_index(fromVertexLabel)
    col = self.get_index(toVertexLabel)
    if self.graph_type():
        self.adjMat[row][col] = 0
    else:
        self.adjMat[row][col] = 0
        self.adjMat[col][row] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    vert = self.get_index(vertexLabel)
    self.Vertices.pop(vert)
    self.adjMat.pop(vert)
    for i in range(len(self.adjMat)):
        self.adjMat[i].pop(vert)


def main():
  # create the Graph object
  cities = Graph()

  # oepn the file for reading
  in_file = open ("./graph.txt", "r")

  # read the number of vertices
  num_vertices = int ((in_file.readline()).strip())

  # read all the Vertices and add them the Graph
  for i in range (num_vertices):
    city = (in_file.readline()).strip()
    cities.add_vertex (city)

  # read the number of edges
  num_edges = int ((in_file.readline()).strip())

  # read the edges and add them to the adjacency matrix
  for i in range (num_edges):
    edge = (in_file.readline()).strip()
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # read the starting vertex fro dfs and bfs
  start_vertex = (in_file.readline()).strip()

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)

  #test the depth first search
  print ("Depth First Search")
  cities.dfs (start_index)
  print ()

  #test breadth first search
  print ("Breadth First Search")
  cities.bfs (start_index)
  print ()

  #test deletion of an edge
  print("Deletion of an edge")
  print()
  cities.delete_edge("Dallas", "Atlanta")

  # print the adjacency matrix
  print ("Adjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j], end = " ")
    print ()
  print ()

  #test deletion of a vertex
  print("Deletion of a vertex")
  cities.delete_vertex("Denver")
  print("\nList of Vertices")
  for i in range(len(cities.Vertices)):
      print(cities.Vertices[i])
  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (len(cities.adjMat)):
    for j in range (len(cities.adjMat)):
      print (cities.adjMat[i][j], end = " ")
    print ()

if __name__ == '__main__':
  main()
