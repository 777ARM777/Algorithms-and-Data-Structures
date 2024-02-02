def counting_sort(array, digit):
    size = len(array)
    res = [0] * size
    count = [0] * 10

    for num in array:
        count[(num // digit) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(len(array) - 1, -1, -1):
        res[count[(array[i] // digit) % 10] - 1] = array[i]
        count[(array[i] // digit) % 10] -= 1

    return res


def radix_sort(array):
    max_element = max(array)
    digit = 1
    while max_element // digit > 0:
        array = counting_sort(array, digit)
        digit *= 10
    return array


lst = [654, 852, 845, 125, 741, 654, 951, 753, 145, 856, 325, 447]
print(radix_sort(lst))
