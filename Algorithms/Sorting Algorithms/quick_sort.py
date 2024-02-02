import random


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition_random_pivot(arr, start, end)
        # pivot = partition_start_pivot(arr, start, end)
        # pivot = partition_end_pivot(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)


def partition_end_pivot(arr, start, end):
    index = start
    pivot = end
    for i in range(start, end):
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    arr[index], arr[pivot] = arr[pivot], arr[index]
    return index


def partition_start_pivot(arr, start, end):
    index = end
    pivot = start
    for i in range(end, start, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index -= 1
    arr[index], arr[pivot] = arr[pivot], arr[index]
    return index


def partition_random_pivot(arr, start, end):
    pivot = random.randint(start, end)
    arr[pivot], arr[end] = arr[end], arr[pivot]
    index = start - 1
    for i in range(start, end):
        if arr[i] < arr[end]:
            index += 1
            arr[i], arr[index] = arr[index], arr[i]
    arr[index + 1], arr[end] = arr[end], arr[index + 1]
    return index + 1


lst = [5, 8, 9, 7, 4, 6, 5, 10, 0, 8, 45, 15, 31, 9]
for i in range(50):
    quick_sort(lst, 0, len(lst) - 1)
    print(lst)
