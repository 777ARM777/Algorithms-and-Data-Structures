def binary_search(lst, target, start, end):
    if start <= end:
        mid = end - (end - start) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            return binary_search(lst, target, start, mid - 1)
        else:
            return binary_search(lst, target, mid + 1, end)
    return -1


arr = [1, 3, 5, 7, 8, 9]
print(binary_search(arr, 1, 0, len(arr)  - 1))
print(binary_search(arr, 5, 0, len(arr)  - 1))
print(binary_search(arr, 9, 0, len(arr)  - 1))
print(binary_search(arr, 0, 0, len(arr)  - 1))
print(binary_search(arr, 6, 0, len(arr)  - 1))
print(binary_search(arr, 10, 0, len(arr)  - 1))


