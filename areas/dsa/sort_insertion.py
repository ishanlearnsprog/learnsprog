def insertion_sort(a, l):
    for i in range(1, l):
        vali = a[i]
        j = i-1
        while j >= 0 and a[j] >= vali:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = vali

a = [2, 3, 1, 5, 4, 0, 6, 9, 8, 7]
l = len(a)

print("Before Sorting", a)
insertion_sort(a, l)
print("After Sorting", a)
