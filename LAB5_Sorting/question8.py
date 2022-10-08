# Implementing Radixsort

def countSort(array, ind):
    n = len(array)
    temp = [0] * len(array)
    bin = [0] * 10
    for i in range(0, n):
        index = array[i] // ind
        bin[index % 10] += 1
    for i in range(1, 10):
        bin[i] += bin[i - 1]
    i = n - 1
    while i >= 0:
        index = array[i] // ind
        temp[bin[index % 10] - 1] = array[i]
        bin[index % 10] -= 1
        i -= 1
    for i in range(0, n):
        array[i] = temp[i]
    return


def radixSort(array):
    ind = 1
    while max(array) // ind > 0:
        countSort(array, ind)
        ind *= 10
    return array

# print("sorted array is :")
# print(radixSort([1, 2, 5, 4, 3]))
# print("sorted array is :")
# print(radixSort([6, 5, 4, 3, 2, 1]))
