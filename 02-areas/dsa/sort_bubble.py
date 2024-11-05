def bubble_sort(a, l):
    for i in range(l-1):
        swapped = False
        for j in range(l-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if swapped == False: break

a = [2, 3, 1, 5, 4, 0, 6, 9, 8, 7]
l = len(a)

print("Before Sorting", a)
bubble_sort(a, l)
print("After Sorting", a)
