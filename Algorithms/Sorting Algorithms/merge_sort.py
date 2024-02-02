def merge_sort(lst, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(lst, start, mid)
        merge_sort(lst, mid + 1, end)
        merge(lst, start, mid, end)
    return lst

def merge(lst, start, mid, end):
    tmp = lst[:]
    s1 = start
    e1 = mid
    s2 = mid + 1
    e2 = end
    index = start
    while s1 <= e1 and s2 <= e2:
        if tmp[s1] < tmp[s2]:
            lst[index] = tmp[s1]
            index += 1
            s1 += 1
        else:
            lst[index] = tmp[s2]
            index += 1
            s2 += 1

    while s1 <= e1:
        lst[index] = tmp[s1]
        index += 1
        s1 += 1

    while s2 <= e2:
        lst[index] = tmp[s2]
        index += 1
        s2 += 1


lst1 = [2, 5, 11, 6, 9, 8, 0]
lst2 = [9, 8, 7, 6, 5, 2, 1]
print(merge_sort(lst1, 0, len(lst1) - 1))
print(merge_sort(lst2, 0, len(lst2) - 1))