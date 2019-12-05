#  File: Boxes.py
#  Description: This program provides the largest boxes that contain nested boxes within them.
#  Student Name: Sahil Shah
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 16 October 2019
#  Date Last Modified: 17 October 2019



def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


# get all subsets of boxes
def subsets(a, b, idx):
    """
    Finds all combinations of boxes.
    """

    global boxes

    hi = len(a)
    if idx == hi:
        box_fits = True
        for i in range(len(b)-1):
            # check if all the boxes in a given subset fit
            box_fits = does_fit(b[i], b[i+1])
            if box_fits == False:
                break
        # keep track of it
        if box_fits == True:
            boxes.append(b)
        return
    else:
        c = b[:]
        b.append(a[idx])
        idx+=1
        subsets(a, b, idx)
        subsets(a, c, idx)


def main():

    global boxes
    boxes = []

    # open the file for reading
    in_file = open ("./boxes.txt", "r")

    # read the number of boxes
    line = in_file.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list of boxes
    box_list = []

    # read the list of boxes from the file
    for i in range (num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for j in range (len(box)):
            box[j] = int (box[j])
        box.sort ()
        box_list.append (box)

    # close the file
    in_file.close()

    # sort the box list
    box_list.sort()

    a = box_list
    b = []
    subsets(a, b, 0)

    # print all the largest subset of boxes
    #Finds length of boxes list
    num_boxes = 0
    for i in boxes:
        if num_boxes < len(i):
            num_boxes = len(i)

    #If there are no boxes that nest in another then print
    if num_boxes == 1:
        print('No nesting boxes')
    else:
        #If there are nested boxes then add to list with largest boxes
        nested_boxes = []
        for j in boxes:
            if len(j) == num_boxes:
                nested_boxes.append(j)
    #Print list of boxes
    print('Largest Subset of Nesting Boxes')
    nested_boxes.sort()
    for box in nested_boxes:
        for nest_box in box:
            print(tuple(nest_box))
        print()


main()
