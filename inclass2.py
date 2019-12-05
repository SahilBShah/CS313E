def permute (a, lo):
    hi = len(a)
    if (lo == hi):
        if 'A' != a[0] and 'B' != a[1] and 'C' != a[2] and 'D' != a[3]:
            print (a)
    else:
        for i in range (lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute (a, lo + 1)
            a[lo], a[i] = a[i], a[lo]

def mod_permute(a, lo):
    hi = len(a)
    if lo == hi:
        for i in range(len(a)):
            if a[i] == 'C' or a[i] == D and a[i+1] != 'C' or a[i+1] != 'D':
                for i in range(len(a)):
                    if a[i] == 'A' and a[i+1] == 'B' or a[i] == 'B' or a[i+1] == 'A':
                        print(a)
    else:
        for i in range (lo, hi):
            a[lo], a[i] = a[i], a[lo]
            permute (a, lo + 1)
            a[lo], a[i] = a[i], a[lo]



def main():
    a = ['A', 'B', 'C', 'D', 'E']
    permute (a, 0)
    print()
    mod_permute(a, 0)

main()
