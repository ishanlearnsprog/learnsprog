def selection_sort(a, l):
    for i in range(l-1):
        mini = i
        for j in range(i+1, l):
            if a[mini] > a[j]:
                mini = j
        a[i], a[mini] = a[mini], a[i]

a = [2, 3, 1, 5, 4, 0, 6, 9, 8, 7]
l = len(a)

print("Before Sorting", a)
selection_sort(a, l)
print("After Sorting", a)
