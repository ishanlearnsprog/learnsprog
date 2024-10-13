def heapify(a, l, i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < l and a[left] > a[largest]:
        largest = left

    if right < l and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, l, largest)

def heap_sort(a, l):
    for i in range(l//2-1, -1, -1):
        heapify(a, l, i)

    for i in range(l-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

a = [2, 3, 1, 5, 4, 0, 6, 9, 8, 7]
l = len(a)

print("Before Sorting", a)
heap_sort(a, l)
print("After Sorting", a)
