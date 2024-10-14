def linear_search(a, l, val):
    for i in range(l):
        if a[i] == val: return i
    return -1

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l = len(a)
targets = [1, 6, 4, -1]

for t in targets:
    res = linear_search(a, l, t)
    if res != -1:
        print("{} found at position: {}".format(t, res))
    else:
        print("Not Found")
