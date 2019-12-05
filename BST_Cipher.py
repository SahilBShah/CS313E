#  File: BST_Cipher.py
#  Description: This program uses a binary search tree to encrypt any string with a user inputted encryption key.
#  Student Name: Sahil Shah
#  Student UT EID: sbs2756
#  Course Name: CS 313E
#  Unique Number: 50205
#  Date Created: 16 November 2019
#  Date Last Modified: 18 November 2019

class Node():
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree():

  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):

    #Initialize variables
    self.root = None
    self.encry = encrypt_str
    self.encry = self.encry.lower()

    encry_string = ''
    for i in range(len(self.encry)):
      if ('a' <= self.encry[i] and self.encry[i] <= 'z') or self.encry[i] == ' ':
        encry_string += self.encry[i]
    self.encry = encry_string
    for i in range(len(self.encry)):
      self.insert(self.encry[i])

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):

    if self.find(ch) != None:
      return
    new_node = Node(ch)
    if self.root == None:
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while current != None:
        parent = current
        if ch < current.data:
            current = current.lchild
        else:
            current = current.rchild
      if ch < parent.data:
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):

    if self.root.data == ch:
      return '*'
    elif self.find(ch) == None:
      return ''
    else:
        current=self.root
        in_tree_not = ''
        while current != None and current.data != ch:
          if ch < current.data:
            in_tree_not += '<'
            current = current.lchild
          else:
            in_tree_not += '>'
            current = current.rchild
        return in_tree_not

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):

    current = self.root
    if st[0] == '*':
      return current.data
    for i in range(len(st)):
      if st[i] == '<' and current.lchild != None:
        current = current.lchild
      elif st[i] == '>' and current.rchild != None:
        current = current.rchild
      else:
        return ''
    return current.data

  # the encrypt function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):

    encrypted_str = ''
    st = st.lower()
    if st == '':
      return encrypted_str
    for i in range(len(st)):
      if st[i] in self.encry:
        encrypted_str += self.search(st[i]) + '!'
      else:
          encrypted_str = st[i] + '!'
    final_encry = encrypted_str[:len(encrypted_str)-1]
    return final_encry

  # the decrypt function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):

    decrypted_str = ''
    if st == '':
      return decrypted_str
    operators = ['<','>','*','!']
    st = st.split('!')
    for i in range(len(st)):
      bool = True
      for j in range (len(st[i])):
        if not st[i][j] in operators:
          decrypted_str += st[i][j]
          bool = False
      if bool:
        decrypted_str += self.traverse(st[i])
    return decrypted_str

  #search for value in tree
  def find (self, val):

    current = self.root
    while current != None and current.data != val:
      if val < current.data:
        current = current.lchild
      else:
        current = current.rchild
    return current

def main():

    #User inputs
    encryption_key = str(input('Enter encryption key: '))
    print()
    binary_tree = Tree(encryption_key)
    user_input = str(input('Enter string to be encrypted: '))
    encrypted_string = binary_tree.encrypt(user_input)
    print('Encrypted string: ' + encrypted_string)
    print()
    user_dec_string = str(input('Enter string to be decrypted: '))
    decrypted_string = binary_tree.decrypt(user_dec_string)
    print ('Decrypted string: ' + decrypted_string)

main()
