#  File: Reducible.py
#  Description: This program tries to find the longest reducible word from a list of words.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 28 October 2019
#  Date Last Modified: 29 October 2019

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that
# string
def step_size (s, const):
    step = const - (hash_word(s, const) % const)
    return step

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):
    key = hash_word(s, len(hash_table))
    if hash_table[key] == '':
        hash_table[key] = s
    else:
        step = step_size(s, 13)
        double_key = key + step
        if double_key > len(hash_table):
            double_key = double_key % len(hash_table)
        while hash_table[double_key] != '':
            double_key += step
            if double_key >= len(hash_table):
                double_key = double_key % len(hash_table)
        hash_table[double_key] = s


# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word (s, hash_table):
    key = hash_word(s, len(hash_table))
    if hash_table[key] == s:
        return True
    else:
        step = step_size(s, 13)
        double_key = key + step
        if double_key >= len(hash_table):
            double_key = double_key % len(hash_table)
        if hash_table[double_key] == s:
            return True
        else:
            while hash_table[double_key] != '':
                double_key += step
                if double_key >= len(hash_table):
                    double_key = double_key % len(hash_table)
                if hash_table[double_key] == s:
                    return True
    return False

#recursively finds if a word is reducible, if the word is
#reducible it enters it into the hash memo and returns True
#and False otherwise
def is_reducible (s, hash_table, hash_memo):

    if s == 'a' or s == 'i' or s == 'o':
        return True
    else:
        for i in range(len(s)):
            reduced_word = s[:i] + s[i + 1:]
            if find_word(reduced_word, hash_memo):
                return True
            elif find_word(reduced_word, hash_table):
                if is_reducible(reduced_word, hash_table, hash_memo):
                    insert_word(s, hash_memo)
                    return True
                # else:
                #     return False
        return False

# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
    longest_word = ''
    long_words_list = []
    for i in range(len(string_list)):
        if len(string_list[i]) > len(longest_word):
            longest_word = string_list[i]
            long_words_list = []
            long_words_list.append(longest_word)
        elif len(string_list[i]) == len(longest_word):
            long_words_list.append(string_list[i])
    return long_words_list

def main():
  # create an empty word_list
    word_list = []

  # open the file words.txt
    file = open('./words.txt', 'r')
    file1 = open('./words.txt', 'r')

  # read words from words.txt and append to word_list
    count = len(file1.readlines())
    for i in range(count):
        line = file.readline()
        line = line.strip()
        word_list.append(line)

  # close file words.txt
    file.close()
    file1.close()

  # find length of word_list
    list_length = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
    N = 2 * list_length
    while is_prime(N) == False:
        N+=1

  # create an empty hash_list
    hash_list = []

  # populate the hash_list with N blank strings
    for i in range(N):
        hash_list.append('')

  # hash each word in word_list into hash_list
  # for collisions use double hashing
    for i in range(count):
        insert_word(word_list[i], hash_list)

  # create an empty hash_memo
    hash_memo = []

  # populate the hash_memo with M blank strings
    M = 27011
    while is_prime(M) == False:
        M+=1
    for i in range(M):
        hash_memo.append('')
    insert_word('a', hash_memo)
    insert_word('i', hash_memo)
    insert_word('o', hash_memo)

  # create and empty list reducible_words
    reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
    for i in range(len(word_list)):
        if is_reducible(word_list[i], hash_list, hash_memo):
            reducible_words.append(word_list[i])


  # find words of the maximum length in reducible_words
    long_words_list = get_longest_words(reducible_words)

  # print the words of maximum length in alphabetical order
  # one word per line
    long_words_list.sort()
    for i in range(len(long_words_list)):
        print(long_words_list[i])


# This line above main is for grading purposes. It will not
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
