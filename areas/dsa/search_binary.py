def binary_search(a, l, val):
    b = 0
    e = l-1
    while b <= e:
        m = (b+e)//2
        if a[m] == val:
            return m
        elif a[m] < val:
            b = m+1
        else:
            e = m-1
    return -1

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l = len(a)
targets = [1, 6, 4, -1]

for t in targets:
    res = binary_search(a, l, t)
    if res != -1:
        print("{} found at position: {}".format(t, res))
    else:
        print("Not Found")
