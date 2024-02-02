def counting_sort(array):
    max_element, min_element = max(array), min(array)
    size = max_element - min_element + 1
    count = [0] * size
    res = [0] * len(array)

    for num in array:
        count[num - min_element] += 1
    for i in range(1, size):
        count[i] += count[i - 1]
    for i in range(len(array) - 1, -1, -1):
        res[count[array[i] - min_element] - 1] = array[i]
        count[array[i] - min_element] -= 1

    return res


ls = [5, 9, 8, 7, 5, 4, 4, 1, 2, 0]
print(counting_sort(ls))