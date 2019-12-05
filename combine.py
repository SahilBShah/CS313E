def combine (a, b, idxA):
  print(idxA)
  if (idxA == len(a)):
    if (len(b) > 0):
      print (b)
      return
  else:
    c = b[:]
    b.append (a[idxA])
    idxA = idxA + 1
    print('hi')
    combine (a, b, idxA)
    print('yo')
    combine (a, c, idxA)
    print('yo2')
def main():
  print ("Test combine")
  a = [1, 2, 3]
  b = []
  combine (a, b, 0)
  print ()

main()
