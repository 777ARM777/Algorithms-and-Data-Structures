def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = end - (end - start) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


arr = [1, 3, 5, 7, 8, 9]
print(binary_search(arr, 1))
print(binary_search(arr, 5))
print(binary_search(arr, 9))
print(binary_search(arr, 0))
print(binary_search(arr, 6))
print(binary_search(arr, 10))


