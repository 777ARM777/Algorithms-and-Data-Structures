def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


lst1 = [2, 5, 11, 6, 9, 8, 0]
lst2 = [9, 8, 7, 6, 5, 2, 1]
print(insertion_sort(lst1))
print(insertion_sort(lst2))

