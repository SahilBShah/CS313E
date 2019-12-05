def pairings(friends):
    pairs = []
    lst = []
    pairs.append(str(friends[friends.index('A')]) + ':' + str(friends[friends.index('Y')]))
    friends.pop(friends.index('A'))
    friends.pop(friends.index('Y'))
    permute(friends, 0, len(friends)-1, lst)
    for i in range(len(lst)):
        for j in range(0,len(friends), 2):
            pairs.append(lst[i][j] + ':' + lst[i][j+1])
    print(pairs)

def permute(a, lo, hi, lst):
    if lo == hi:
        lst.append(a)
    else:
        for i in range(lo, hi):
            a[i], a[lo] = a[lo], a[i]
            permute(a, lo+1, hi, lst)
            a[i], a[lo] = a[lo], a[i]
def main():
    f = ['A', 'E', 'I', 'O', 'U', 'Y']
    pairings(f)

main()
