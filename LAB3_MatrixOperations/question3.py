'''
3. A matrix is a collection of scalar values arranged in rows and columns as a rectangular grid of a fixed size. The elements of the matrix can be accessed by specifying a given row and column index with indices starting at 0.
Note: Implement the 2D array (as discussed in class) -- sparse matrix version

(Python, Java, C++): Implement a class Matrix that has the following methods

Matrix( rows, ncols ): Creates a new matrix containing nrows and ncols with each element initialized to 0.
numRows( ): Returns the number of rows in the matrix.
numCols( ): Returns the number of columns in the matrix.
getitem ( row, col ): Returns the value stored in the given matrix element. Both row and col must be within the valid range.
setitem ( row, col, scalar ): Sets the matrix element at the given row and col to scalar. The element indices must be within the valid range.
scaleBy( scalar ): Multiplies each element of the matrix by the given scalar value. The matrix is modified by this operation.
transpose( ): Returns a new matrix that is the transpose of this matrix.
add ( rhsMatrix ): Creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix. The size of the two matrices must be the same.
subtract ( rhsMatrix ): The same as the add() operation but subtracts the two matrices.
multiply ( rhsMatrix ): Creates and returns a new matrix that is the result of multiplying this matrix to the given rhsMatrix. The two matrices must be of appropriate sizes as defined for matrix multiplication.
(C Language) Implement the above as functions with the matrix as the first argument in each case.

For example, transpose(mymatrix), subtract(mymatrix, rhsmatrix),..etc.
'''

'''
Implementing a sparse matrix as using a dictionary.
key will the 2 tuple coordinate (i,j) and the value the value in matrix.
'''


class Matrix:
    def __init__(self, nrows, ncols) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.defaultValue = 0
        self.matrix = {}
        return

    def createMatrixFromSparseMatrix(self, matrix):

        tempMatrix = [[self.defaultValue for i in range(
            self.ncols)] for j in range(self.nrows)]
        for i, j in matrix:
            tempMatrix[i][j] = matrix[(i, j)]
        return tempMatrix

    def checkValidSize(self, row, col):
        if(row == self.nrows and col == self.ncols):
            return
        raise ValueError

    def numnrows(self):
        return self.nrows

    def numCols(self):
        return self.ncols

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

    def scaleBy(self, scalar):
        for matrixElement in self.matrix:
            self.matrix[matrixElement] *= scalar
        self.defaultValue *= scalar

    def transpose(self):
        transposedMatrix = {}
        for i, j in self.matrix:
            transposedMatrix[(j, i)] = self.matrix[(i, j)]
        return self.createMatrixFromSparseMatrix(transposedMatrix)

    def add(self, rhsMatrix):
        self.checkValidSize(len(rhsMatrix), len(rhsMatrix[0]))
        sumMatrix = {}
        for i in range(self.nrows):
            for j in range(self.ncols):
                try:
                    sumMatrix[(i, j)] = self.matrix[(i, j)] + rhsMatrix[i][j]
                except:
                    sumMatrix[(i, j)] = self.defaultValue + rhsMatrix[i][j]
        return self.createMatrixFromSparseMatrix(sumMatrix)

    def subtract(self, rhsMatrix):
        self.checkValidSize(len(rhsMatrix), len(rhsMatrix[0]))
        subMatrix = {}
        for i in range(self.nrows):
            for j in range(self.ncols):
                try:
                    subMatrix[(i, j)] = self.matrix[(i, j)] - rhsMatrix[i][j]
                except:
                    subMatrix[(i, j)] = self.defaultValue - rhsMatrix[i][j]
        return self.createMatrixFromSparseMatrix(subMatrix)

    def multiply(self, rhsMatrix):
        self.checkValidSize(len(rhsMatrix), len(rhsMatrix[0]))
        myMatrix = self.createMatrixFromSparseMatrix(self.matrix)
        mulmatrix = [[0 for i in range(
            self.ncols)] for j in range(self.nrows)]
        for i in range(self.nrows):
            for j in range(self.ncols):
                for k in range(self.nrows):
                    mulmatrix[i][j] += myMatrix[i][k]*rhsMatrix[k][j]
        return mulmatrix

    def printMatrix(self):
        tempMatrix = [[self.defaultValue for i in range(
            self.ncols)] for j in range(self.nrows)]
        for i, j in self.matrix:
            tempMatrix[i][j] = self.matrix[(i, j)]

        for i in range(self.nrows):
            print(*tempMatrix[i])
        return


# matrix = Matrix(3, 3)
# matrix.setitem(0, 0, 1)
# matrix.setitem(1, 1, 1)
# matrix.setitem(2, 2, 1)
# matrix.scaleBy(3)
# matrix.printMatrix()
# print(matrix.transpose())
# print(matrix.add([[1, 0, 0], [0, 1, 1], [0, 0, 1]]))
# print(matrix.subtract([[1, 0, 0], [0, 1, 1], [0, 0, 1]]))
# print(matrix.multiply([[1, 2, 1], [1, 1, 1], [1, 1, 1]]))
