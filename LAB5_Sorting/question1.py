# Implement Bubble Sort with the idea that if there are no exchanges in a particular pass (round), then the sort terminates.

def BubbleSort(l: list) -> list:
    n = len(l)
    for i in range(1, n):
        exchanges = 0
        # print("debug",i,l)
        for j in range(n-i):
            if(l[j] > l[j+1]):
                exchanges += 1
                l[j+1], l[j] = l[j], l[j+1]
        if(exchanges == 0):
            break

    return l


# print("sorted array is :")
# print(BubbleSort([1,2,5,4,3]))
# print("sorted array is :")
# print(BubbleSort([6,5,4,3,2,1]))
