# Implement Selection Sort.

def SelectionSort(l: list) -> list:
    n = len(l)
    for i in range(n):
        minj = i
        # print("debug", i, l)
        for j in range(i, n):
            if(l[j] < l[minj]):
                minj = j
        l[i], l[minj] = l[minj], l[i]
    return l


# print("sorted array is :")
# print(SelectionSort([1, 2, 5, 4, 3]))
# print("sorted array is :")
# print(SelectionSort([6, 5, 4, 3, 2, 1]))
