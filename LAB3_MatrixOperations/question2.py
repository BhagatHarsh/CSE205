'''
2. A two-dimensional array consists of a collection of elements organized into rows and columns. Individual elements are referenced by specifying the specific row and column indices (r, c), both of which start at 0.
Note: Implement the 2D array (as discussed in class) -- sparse matrix version

(Python, Java, C++): Implement a class Array2D that has the following methods

Array2D( nrows, ncols ): Creates a two-dimensional array organized into rows and columns. The nrows and ncols arguments indicate the size of the table. The individual elements of the table are initialized to None.

numRows( ): Returns the number of rows in the 2-D array.

numCols( ): Returns the number of columns in the 2-D array.

clear( value ): Clears the array by setting each element to the given value.

getitem( i1, i2 ): Returns the value stored in the 2-D array element at the position indicated by the 2-tuple (i1,i2), both of which must be within the valid range.

setitem(i1, i2, value): Modifies the contents of the 2-D array element indicated by the 2-tuple (i1,i2) with the new value. Both indices must be within the valid range.


'''

'''
Implementing a sparse matrix as using a dictionary.
key will the 2 tuple coordinate (i,j) and the value the value in matrix.
'''


class Array2D:
    def __init__(self, nrows, ncols) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.defaultValue = None
        self.matrix = {}
        return

    def numnrows(self):
        return self.nrows

    def numCols(self):
        return self.ncols

    def clear(self, value):
        self.matrix = {}
        self.defaultValue = value
        return

    def getitem(self, i, j):
        try:
            return self.matrix[(i, j)]
        except:
            if(i >= 0 and i < self.nrows and j >= 0 and j < self.ncols):
                return self.defaultValue
            raise ValueError
        return

    def setitem(self, i, j, value):
        if(i >= 0 and i < self.nrows and j >= 0 and j < self.ncols):
            self.matrix[(i, j)] = value
        else:
            raise ValueError
        return

    def printMatrix(self):
        tempMatrix = [[self.defaultValue for i in range(
            self.ncols)] for j in range(self.nrows)]
        for i, j in self.matrix:
            tempMatrix[i][j] = self.matrix[(i, j)]

        for i in range(self.nrows):
            print(*tempMatrix[i])
        return


# matrix = Array2D(3, 3)
# matrix.setitem(0, 0, 1)
# matrix.setitem(1, 1, 1)
# matrix.setitem(2, 2, 1)
# matrix.setitem(2, 1, 1)
# matrix.printMatrix()
