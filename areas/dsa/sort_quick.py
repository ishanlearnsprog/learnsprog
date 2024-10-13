def partition(a, b, e):
    pivot, i, j = a[b], b, e
    while i < j:
        while a[i] <= pivot and i <= e-1:
            i += 1
        while a[j] > pivot and j >= i+1:
            j -= 1
        if i < j: a[i], a[j] = a[j], a[i]
    a[b], a[j] = a[j], a[b]
    return j

def quick_sort(a, b, e):
    if b < e:
        p = partition(a, b, e)
        quick_sort(a, b, p-1)
        quick_sort(a, p+1, e)

a = [2, 3, 1, 5, 4, 0, 6, 9, 8, 7]
l = len(a)

print("Before Sorting", a)
quick_sort(a, 0, l-1)
print("After Sorting", a)
