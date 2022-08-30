'''
1. A two-dimensional array consists of a collection of elements organized into rows and columns. Individual elements are referenced by specifying the specific row and column indices (r, c), both of which start at 0.

Array2D( nrows, ncols ): Creates a two-dimensional array organized into rows and columns. The nrows and ncols arguments indicate the size of the table. The individual elements of the table are initialized to None.

numRows( ): Returns the number of rows in the 2-D array.

numCols( ): Returns the number of columns in the 2-D array.

clear( value ): Clears the array by setting each element to the given value.

getitem( i1, i2 ): Returns the value stored in the 2-D array element at the position indicated by the 2-tuple (i1,i2), both of which must be within the valid range.

setitem(i1, i2, value): Modifies the contents of the 2-D array element indicated by the 2-tuple (i1,i2) with the new value. Both indices must be within the valid range.

'''


class Array2D:
    def __init__(self, nrows, ncols) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.matrix = [[None for i in range(ncols)] for j in range(nrows)]
        return

    def numnrows(self):
        return self.nrows

    def numCols(self):
        return self.ncols

    def clear(self, value):
        for i in range(self.nrows):
            for j in range(self.ncols):
                self.matrix[i][j] = value
        return

    def getitem(self, i, j):
        try:
            return self.matrix[i][j]
        except:
            raise ValueError
        return

    def setitem(self, i, j, value):
        try:
            self.matrix[i][j] = value
        except:
            raise ValueError
        return

    def printMatrix(self):
        for i in range(self.nrows):
            for j in range(self.ncols):
                print(self.matrix[i][j], end=' ')
            print()
        return


# matrix = Array2D(3, 3)
# matrix.clear(00)
# matrix.setitem(0, 0, 1)
# matrix.setitem(1, 1, 1)
# matrix.setitem(2, 2, 1)
# matrix.printMatrix()
