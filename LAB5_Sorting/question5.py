# Implement Mergesort Algorithm.

def mergeSortedSubseq(theSeq, left, right, end, tmpArray):
    a = left
    b = right
    m = 0
    while a < right and b < end:
        if theSeq[a] < theSeq[b]:
            tmpArray[m] = theSeq[a]
            a += 1
        else:
            tmpArray[m] = theSeq[b]
            b += 1

        m += 1

    while a < right:
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1

    while b < end:
        tmpArray[m] = theSeq[b]
        b += 1
        m += 1

    for i in range(end-left):
        theSeq[i+left] = tmpArray[i]


def recMergeSort(theSeq, first, last, tmpArray):
    if first == last:
        return
    else:
        mid = (first + last) // 2
    recMergeSort(theSeq, first, mid, tmpArray)
    recMergeSort(theSeq, mid+1, last, tmpArray)
    mergeSortedSubseq(theSeq, first, mid+1, last+1, tmpArray)


def MergeSort(theSeq: list) -> list:
    n = len(theSeq)
    tmpArray = [-1]*n
    recMergeSort(theSeq, 0, n-1, tmpArray)
    return (tmpArray)


# print("sorted array is :")
# print(MergeSort([1, 2, 5, 4, 3]))
# print("sorted array is :")
# print(MergeSort([6, 5, 4, 3, 2, 1]))
