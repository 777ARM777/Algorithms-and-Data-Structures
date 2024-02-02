def selection_sort(lst):
    for i in range(len(lst)):
        max_index = 0
        for j in range(len(lst) - i):
            if lst[max_index] < lst[j]:
                max_index = j
        lst[j], lst[max_index] = lst[max_index], lst[j]
    return lst



lst1 = [2, 5, 11, 6, 9, 8, 0]
lst2 = [9, 8, 7, 6, 5, 2, 1]
print(selection_sort(lst1))
print(selection_sort(lst2))
