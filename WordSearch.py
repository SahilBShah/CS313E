#File: WordSearch.py
#Description: This program attempts to find all the words in a word search and outputs the location of the first letter of the word in the word search in a text file.
#Student's Name: Sahil Shah
#Student's UT EID: sbs2756
#Course Name: CS 313E
#Unique Number: 50205
#Date Created: 9 September 2019
#Date Last Modified: 13 September 2019

def main():

    global found_words
    found_words = {}
    parameters_list = []
    words_list = []

    #Puts word search grid into a list based on rows
    with open("hidden.txt") as f:
        for row in f:
            input_file = [list(map(str, row.split(","))) for row in f]
            parameters_list.append(tuple(map(int, row.split(" "))))
    input_file.pop()
    input_file.pop(0)
    for item in input_file:
        item[-1] = item[-1].strip()
    input_file.remove([""])
    words_list = input_file[int(parameters_list[0][0])+1:]
    word_search = input_file[0:int(parameters_list[0][0])]


    #Rows
    new_word_search = make_horizontal(word_search)
    horizontal_find_words(words_list, new_word_search)


    #Columns
    type = "vertical"
    vertical_word_search = make_vertical(new_word_search)
    find_words(words_list, vertical_word_search, type)


    #Diagonals
    upper_left_diagonal_word_search = make_diagonal(new_word_search)
    type = "upper left diagonal"
    find_words(words_list, upper_left_diagonal_word_search, type)

    bottom_left_diagonal_word_search = make_diagonal(vertical_word_search)
    type = "bottom left diagonal"
    find_words(words_list, bottom_left_diagonal_word_search, type)

    reversed_word_search = make_reverse(new_word_search)
    upper_right_diagonal_word_search = make_diagonal(reversed_word_search)
    type = "upper right diagonal"
    find_words(words_list, upper_right_diagonal_word_search, type)

    vertical_reversed_word_search = make_vertical(reversed_word_search)
    bottom_right_diagonal_word_search = make_diagonal(vertical_reversed_word_search)
    type = "bottom right diagonal"
    find_words(words_list, bottom_right_diagonal_word_search, type)

    output_words(found_words)


def horizontal_find_words(words_list, word_search):
    """
    If data is from rows of the word search then this will find any words located in the rows.
    """

    global found_words

    #Finds words in rows of wrod search
    for row in range(len(word_search)):
        current_row = word_search[row]
        for i in range(len(words_list)):
            if words_list[i][0] in current_row and words_list[i][0] not in found_words:
                row_index = row + 1
                col_index = current_row.index(words_list[i][0]) + 1
                found_words.update({words_list[i][0]: [row_index, col_index]})
            if words_list[i][0][len(words_list[i][0])::-1] in current_row and words_list[i][0] not in found_words:
                row_index = row + 1
                col_index = current_row.index(words_list[i][0][len(words_list[i][0])::-1]) + len(words_list[i][0])
                found_words.update({words_list[i][0]: [row_index, col_index]})


def find_words(words_list, word_search, type):
    """
    If data is from anything but the rows of the word search, such as columns and diagonals, then this will find any words located in them.
    """

    global found_words

    #Finds words in verticals and diagonals of word search
    for row in word_search:
        current_row = "".join(row)
        for i in range(len(words_list)):
            if words_list[i][0] in current_row and words_list[i][0] not in found_words:
                word = words_list[i][0]
                word_reversed = "no"
                indexes = get_index(type, word, row, current_row, word_search, word_reversed)
                row_index = indexes[0]
                col_index = indexes[1]
                found_words.update({words_list[i][0]: [row_index, col_index]})
            if words_list[i][0][len(words_list[i][0])::-1] in current_row and words_list[i][0] not in found_words:
                word = words_list[i][0][len(words_list[i][0])::-1]
                word_reversed = "yes"
                indexes = get_index(type, word, row, current_row, word_search, word_reversed)
                row_index = indexes[0]
                col_index = indexes[1]
                found_words.update({words_list[i][0]: [row_index, col_index]})


def make_horizontal(word_search):
    """
    Extracts rows from word search.
    """

    new_word_search = []

    #Converts word search into a list of rows
    for i in range(len(word_search)):
        for row in word_search[i]:
            current_row = "".join(map(str, row.split(" ")))
            new_word_search.append(current_row)
    return new_word_search


def make_vertical(new_word_search):
    """
    Transposes the columns into rows and the rows into columns.
    """

    vertical_word_search = []

    #Converts word search into a list of rows by columns
    for col in range(len(new_word_search)):
        temp_list = []
        for i in range(len(new_word_search)):
            current_col = new_word_search[i][col]
            temp_list.append(current_col)
        vertical_word_search.append(temp_list)
    return vertical_word_search


def make_diagonal(new_word_search):
    """
    Creates a list of the diagonal elements in the word search.
    """

    temp_diag_list = []
    diagonal_word_search = []

    #Converts word search into a list of rows by diagonals
    for i in range(len(new_word_search)):
        current_diag = new_word_search[i][i]
        temp_diag_list.append(current_diag)
    diagonal_word_search.append(temp_diag_list)

    for i in range(1, len(new_word_search)):
        temp_diag_list = []
        for j in range(len(new_word_search)-i):
            current_diag = new_word_search[j][j+i]
            temp_diag_list.append(current_diag)
        diagonal_word_search.append(temp_diag_list)
    return diagonal_word_search


def make_reverse(new_word_search):
    """
    Reverses the word search where the right-most column becomes the left-most.
    """

    reversed_word_search = []

    #Reverses the word search
    for i in range(len(new_word_search)):
        reversed_line = new_word_search[i][len(new_word_search[i])::-1]
        reversed_word_search.append(reversed_line)
    return reversed_word_search


def get_index(type, word, row, current_row, word_search, word_reversed):
    """
    Locates indeces for found words
    """

    #Locates indeces for columns and upper triangular diagonals
    if type == "vertical":
        if word_reversed == "no":
            row_index = current_row.index(word) + 1
            col_index = word_search.index(row) + 1
        if word_reversed == "yes":
            row_index = current_row.index(word) + len(word)
            col_index = word_search.index(row) + 1

    if type == "upper left diagonal":
        if word_reversed == "no":
            row_index = current_row.index(word) + 1
            col_index = current_row.index(word) + word_search.index(row) + 1
        if word_reversed == "yes":
            row_index = current_row.index(word) + len(word)
            col_index = current_row.index(word) + word_search.index(row) + len(word)

    if type == "bottom left diagonal":
        if word_reversed == "no":
            row_index = word_search.index(row) + current_row.index(word) + 1
            col_index = current_row.index(word) + 1
        if word_reversed == "yes":
            row_index = current_row.index(word) + word_search.index(row) + len(word)
            col_index = current_row.index(word) + len(word)

    if type == "upper right diagonal":
        if word_reversed == "no":
            row_index = current_row.index(word) + 1
            col_index = len(word_search) - (word_search.index(row) + current_row.index(word))
        if word_reversed == "yes":
            row_index = current_row.index(word) + len(word)
            col_index = len(word_search) - (word_search.index(row) + len(word))

    if type == "bottom right diagonal":
        if word_reversed == "no":
            row_index = current_row.index(word) + word_search.index(row) + 1
            col_index = len(word_search) - current_row.index(word)
        if word_reversed == "yes":
            row_index = current_row.index(word) + word_search.index(row) + len(word)
            col_index = len(word_search) - (current_row.index(word) + len(word) - 1)

    return [row_index, col_index]

def output_words(words):
    """
    Outputs the words that were found and the indeces for the location of the first letter of the word in a text file
    """

    longest_word = "a"
    #Determines longest word in list of found words
    for key in sorted(words.items()):
        if len(key[0]) > len(longest_word):
            longest_word = key[0]
    #Outputs file with all of the found words and their coordinates
    output_file = open("found.txt", "w+")
    print(words)
    for i in sorted(words):
        indeces = words[i]
        print(i)
        spaces_needed = len(longest_word) - len(key[0])
        output_file.write(str(i) + spaces_needed * " " + 2 * " " + str(indeces[0]) + " " + str(indeces[1]) + "\n")
    output_file.close()



if __name__ == "__main__":
    main()
