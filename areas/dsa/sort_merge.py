def merge(a, b, m, e):
    temp = [0 for _ in range(b, e+1)]
    i, j, k = b, m+1, 0
    while i <= m and j <= e:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1
    while i <= m:
        temp[k] = a[i]
        i += 1
        k += 1
    while j <= e:
        temp[k] = a[j]
        j += 1
        k += 1
    k = 0
    for ii in range(b, e+1):
        a[ii] = temp[ii-b]

def merge_sort(a, b, e):
    if b < e:
        m = (b+e)//2
        merge_sort(a, b, m)
        merge_sort(a, m+1, e)
        merge(a, b, m, e)

a = [2, 3, 1, 5, 4, 0, 6, 9, 8, 7]
l = len(a)

print("Before Sorting", a)
merge_sort(a, 0, l-1)
print("After Sorting", a)
