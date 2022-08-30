'''
4. (Game of Life) A life grid is used to represent and store the area in the game of Life that contains organisms. The grid contains a rectangular grouping of cells of a finite size divided into rows and columns. The individual cells, which can be alive or dead, are referenced by row and column indices, both of which start at zero.
(Python, Java, C++): Implement a class LifeGrid that has the following methods

LifeGrid( nrows, ncols ): Creates a new game grid consisting of nrows and ncols. All cells in the grid are set to dead.
numRows( ): Returns the number rows in the grid.
numCols( ): Returns the number of columns in the grid.
configure(coordList): Configures the grid for evolving the next generation. The coordList argument is a sequence of 2-tuples with each tuple representing the coordinates (r, c) of the cells to be set as alive. All remaining cells are cleared or set to dead.
clearCell( row, col ): Clears the individual cell (row, col) and sets it to dead. The cell indices must be within the valid range of the grid.
setCell( row, col ): Sets the indicated cell (row, col) to be alive. The cell indices must be within the valid range of the grid.
isLiveCell( row,col ): Returns a boolean value indicating if the given cell (row, col) contains a live organism. The cell indices must be within the valid range of the grid.
numLiveNeighbors( row, col ): Returns the number of live neighbors for the given cell (row, col). The neighbors of a cell include all of the cells immediately surrounding it in all directions. For the cells along the border of the grid, the neighbors that fall outside the grid are assumed to be dead. The cell indices must be within the valid range of the grid.
(C Language) Implement the above as functions with the LifeGrid as the first argument in each case.

For example, isLiveCell(mylifegrid, row, col),..etc.
'''


class LifeGrid:
    def __init__(self, nrows, ncols) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.defaultValue = 0
        self.grid = {}
        return

    def numnrows(self):
        return self.nrows

    def numCols(self):
        return self.ncols

    def configure(self, coordList):
        self.grid = {}
        for i, j in coordList:
            if(i >= 0 and i < self.nrows and j >= 0 and j < self.ncols):
                self.grid[(i, j)] = 1
            else:
                raise ValueError
        return

    def clearCell(self, i, j):
        if(i >= 0 and i < self.nrows and j >= 0 and j < self.ncols):
            self.grid[(i, j)] = 0
        else:
            raise ValueError
        return

    def setCell(self, i, j):
        if(i >= 0 and i < self.nrows and j >= 0 and j < self.ncols):
            self.grid[(i, j)] = 1
        else:
            raise ValueError
        return

    def isLiveCell(self, i, j):
        try:
            if(self.grid[i][j]):
                return True
            else:
                return False
        except:
            raise ValueError
        return

    def numLiveNeighbors(self, i, j):
        if(i >= 0 and i < self.nrows and j >= 0 and j < self.ncols):
            neighbours = 0
            try:
                neighbours += self.grid[(i-1, j-1)]
            except:
                neighbours = neighbours
            try:
                neighbours += self.grid[(i, j-1)]
            except:
                neighbours = neighbours
            try:
                neighbours += self.grid[(i+1, j-1)]
            except:
                neighbours = neighbours
            try:
                neighbours += self.grid[(i-1, j)]
            except:
                neighbours = neighbours
            try:
                neighbours += self.grid[(i+1, j)]
            except:
                neighbours = neighbours
            try:
                neighbours += self.grid[(i+1, j+1)]
            except:
                neighbours = neighbours
            try:
                neighbours += self.grid[(i, j+1)]
            except:
                neighbours = neighbours
            try:
                neighbours += self.grid[(i-1, j+1)]
            except:
                neighbours = neighbours

            # blunders hehe
            # if(i-1 >= 0 and j-1 >= 0):
            #     neighbours += self.grid[i-1][j-1]
            # if(i >= 0 and j-1 >= 0):
            #     neighbours += self.grid[i][j-1]
            # if(i+1 < self.nrows and j-1 >= 0):
            #     neighbours += self.grid[i+1][j-1]
            # if(i+1 < self.nrows and j >= 0):
            #     neighbours += self.grid[i+1][j]
            # if(i-1 >= 0 and j >= 0):
            #     neighbours += self.grid[i-1][j]
            # if(i-1 >= 0 and j+1 < self.ncols):
            #     neighbours += self.grid[i-1][j+1]
            # if(i+1 < self.nrows and j+1 < self.ncols):
            #     neighbours += self.grid[i][j+1]
            # if(i+1 < self.nrows and j+1 < self.ncols):
            #     neighbours += self.grid[i+1][j+1]
            return neighbours
        else:
            raise ValueError

    def printGrid(self):
        tempgrid = [[self.defaultValue for i in range(
            self.ncols)] for j in range(self.nrows)]
        for i, j in self.grid:
            tempgrid[i][j] = self.grid[(i, j)]

        for i in range(self.nrows):
            print(*tempgrid[i])
        return

# playGame = LifeGrid(3,3)
# playGame.configure([(0,0),(1,1),(2,2)])
# playGame.setCell(1,2)
# playGame.printGrid()
# print(playGame.numLiveNeighbors(0,0))
