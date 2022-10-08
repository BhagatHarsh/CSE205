# Python implementation QuickSort using Random Pivot
import random


def partition(array, low, high):
    cnt = 0
    mid = random.randint(low, high)
    pivot = array[mid]

    while low < high:
        while array[low] < pivot:
            low += 1
        while array[high] > pivot:
            high -= 1
        if low < high:
            array[low], array[high] = array[high], array[low]
        if mid == low:
            mid = high
        elif mid == high:
            mid = low
    return mid

# Function to perform quicksort


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


# Driver code
# temp = []
# print("sorted array is :")
# temp = [1, 2, 5, 4, 3]
# quick_sort(temp, 0, len(temp)-1)
# print(temp)
# print("sorted array is :")
# temp = [6, 5, 4, 3, 2, 1]
# quick_sort(temp, 0, len(temp)-1)
# print(temp)
