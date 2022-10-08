# Create best cases and worst cases for both sorts above and compare their timings
# importing the required module


# for Binary Insertion Sort

# Call the function using the name of the sorting algorithm
# and the array we just created
mysetup = "from question3 import insertionSort"
best = '''
best = [i for i in range(1, 1001)]
insertionSort(best)
'''
worst = '''
worst = [i for i in reversed(range(1, 1001))]
insertionSort(worst)
'''
# # timeit statement

# print(timeit.timeit(setup=mysetup,
#                     stmt=best,
#                     number=1000))
# print(timeit.timeit(setup=mysetup,
#                     stmt=worst,
#                     number=1000))

'''output when i ran it is
6.60541769998963
7.85618400000385
'''

# for Selection Sort

# Call the function using the name of the sorting algorithm
# and the array we just created
mysetup = "from question2 import SelectionSort"
best = '''
best = [i for i in range(1, 1001)]
SelectionSort(best)
'''
worst = '''
worst = [i for i in reversed(range(1, 1001))]
SelectionSort(worst)
'''
# # timeit statement

# print(timeit.timeit(setup=mysetup,
#                     stmt=best,
#                     number=1000))
# print(timeit.timeit(setup=mysetup,
#                     stmt=worst,
#                     number=1000))

'''output when i ran it is
24.937539299979107
23.221682800009148
'''

'''
I realized later that why is the worst case time coming so close to best
it was because of pychache feature of python
But we can clearly see that the time taken by the insertion sort is less then the selection sort
'''


# Part 2

# for insertion Sort

# Call the function using the name of the sorting algorithm
# and the array we just created
mysetup = '''
# Sorts a sequence in ascending order using the insertion sort algorithm.
def insertionSort( theSeq ):
  n = len( theSeq )

  # Starts with the first item as the only sorted entry.
  for i in range( 1, n ) :
    # Save the value to be positioned.
    value = theSeq[i]

    # Find the position where value fits in the ordered part of the list.
    pos = i

    while pos > 0 and value < theSeq[pos - 1] :
      # Shift the items to the right during the search.
      theSeq[pos] = theSeq[pos - 1]
      pos -= 1

    # Put the saved value into the open slot.
    theSeq[pos] = value
  return( theSeq )
'''
best = '''
best = [i for i in range(1, 1001)]
insertionSort(best)
'''
worst = '''
worst = [i for i in reversed(range(1, 1001))]
insertionSort(worst)
'''
# # timeit statement

# print(timeit.timeit(setup=mysetup,
#                     stmt=best,
#                     number=1000))
# print(timeit.timeit(setup=mysetup,
#                     stmt=worst,
#                     number=1000))

'''output when i ran it is
0.12210189999314025
55.90347299998393
'''

'''
clearly the binary insertion sort wins over normal insertion sort
'''