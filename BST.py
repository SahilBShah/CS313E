class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def __str__ (self):
      return str(self.data)

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root=None

    # creates an encryption key that only contains a-z and ' '
    self.estr=encrypt_str
    self.estr=self.estr.lower()
    fixed=''
    for i in range (len(self.estr)):
      if ('a'<=self.estr[i] and self.estr[i]<='z') or (self.estr[i]==' '):
        fixed+=self.estr[i]
    self.estr=fixed

    # creates the BST with the key
    for i in range (len(self.estr)):
      self.insert(self.estr[i])

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):

    # works like insert from test BST with the addition of this
    # first conditional that prevents duplication
    if self.find(ch)!=None:
      return

    newNode = Node (ch)

    if (self.root == None):
      self.root = newNode

    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (ch < current.data):
            current = current.lChild
        else:
            current = current.rChild

      if (ch < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # Search for a node with the key
  def find (self, key):
    current = self.root

    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild

    return current

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):

    # if the search is for the root
    if self.root.data==ch:
      return '*'

    # if the search ch is not in the tree
    elif self.find(ch)==None:
      return ''

    path=''
    current=self.root
    # creates a string that maps the path to find the seach ch
    while current!=None and current.data!=ch:
      if ch<current.data:
        path+='<'
        current=current.lChild
      else:
        path+='>'
        current=current.rChild

    return path

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current=self.root

    # if the path starts with the root then the traversal ends with the root
    if st[0]=='*':
      return current.data

    # moves through the BST turning as instructed by the path
    for i in range (len(st)):

      if st[i]=='<' and current.lChild!=None:
        current=current.lChild

      elif st[i]=='>' and current.rChild!=None:
        current=current.rChild

      else:
        # if the path is invalid returns blank str
        return ''

    return current.data

  # the encrypt function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    final=''
    if st=='':
      return final

    st=st.lower()
    # converts to lowercase

    for i in range (len(st)):
      # so long as the character is in the tree (and therefore in the key)
      # the search function will add the path to the encryption
      if st[i] in self.estr:
        final+=self.search(st[i])+'!'

      # if the character is not in the tree the encrypted string adds
      # the character with the ! delimiter
      else:
        final+=st[i]+'!'

    # based on sample output, the final delimiter is not included
    return final[:len(final)-1]

  # the decrypt function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    final=''
    if st=='':
      return final

    check=['<','>','*','!']
    # a caveat of using these 4 characters to encrypt is that they cannot
    # be decrypted, that is if these are in the original message they cannot
    # be discerned from the encryption function of those characters

    st=st.split('!')
    # splits the encrypted string at the delimiter (!)

    for i in range (len(st)):
      checkFlag=True
      # checkFlag checks that each character is a valid path director or a delimiter
      # in order for traverse function to work

      for j in range (len(st[i])):
        if not(st[i][j] in check):

          # if it is not a valid director, adds the character to the string
          # and does not traverse
          final+=st[i][j]
          checkFlag=False

      if checkFlag:
        final+=self.traverse(st[i])

    return final

def main():
    key=str(input('Enter encryption key: '))
    print ()
    tree=Tree(key)

    initial=str(input('Enter string to be encrypted: '))
    estr=tree.encrypt(initial)
    print ('Encrypted string: '+estr)
    print ()

    initial2=str(input('Enter string to be decrypted: '))
    dstr=tree.decrypt(initial2)
    print ('Decrypted string: '+dstr)

main()
