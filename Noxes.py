#  File: Boxes.py
#  Description:
#  Student Name: Sahil Shah
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 16 October 2019
#  Date Last Modified: 16 October 2019



def does_fit (box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

def main():
  # open file for reading
  in_file = open ('boxes.txt', 'r')

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create empty list of boxes
  box_list = []

  # read the list of boxes from file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for i in range (len(box)):
      box[i] = int (box[i])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  # sort the box list
  box_list.sort()

  # create a list that will hold the nested boxes
  nested_boxes = []
  # create a variable for the size of the nested boxes
  size_of_nested = 0
  # get all subsets of boxes
  def subsets(a,b,lo):
    hi = len(a)
    if (lo == hi):
      #Set Conditions
      flag_ = True
      # for each subset check if they all fit
      for i in range(len(b) - 1):
        flag_ = does_fit(b[i], b[i+1])
        if (flag_ == False):
          break

      # add to list
      if flag_:
        nested_boxes.append(b)
      return
    else:
      c = b[:]
      b.append (a[lo])
      subsets (a, c, lo + 1)
      subsets (a, b, lo + 1)

  a = box_list
  b = []
  subsets(a, b, 0)

  #Formatting The nested_boxes
  for i in nested_boxes:
      if (size_of_nested < len(i)):
        size_of_nested = len(i)

  if (size_of_nested == 1):
    print("No nested boxes")
  else:

    _final = []
    for i in nested_boxes:
        if len(i) == size_of_nested:
          _final.append(i)

    _final.sort()
    for i in _final:
      for j in i:
        print(j)
      #print()

main()
