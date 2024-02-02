def bubble_sort(lst):
    is_sorted = True
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_sorted = False
        if is_sorted:
            return lst
    return lst


lst1 = [2, 5, 11, 6, 9, 8, 0]
lst2 = [9, 8, 7, 6, 5, 2, 1]
print(bubble_sort(lst1))
print(bubble_sort(lst2))
