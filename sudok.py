#  collection of functions to solve sudoku 
#  background reading http://www.math.kent.edu/~malexand/Latex/Examples/Article%20Example/YSU_Sudoku.pdf  
from itertools import product
#  function to creat list of possibities from entered info
def createPoss(test):
    poss = [[
        list(range(1, 10)) if test[i][j] == 0 else test[i][j] for j in range(9)
    ] for i in range(9)]
    return poss

# function to check rows , columns and 3x3 cells and eliminate duplicates when a known value occurs within them

def removeDupes(test, poss):
    for (i,j) in product(range(0,9), repeat  = 2):
        if test[i][j] != 0:
            for k in range(9):
                if isinstance(poss[i][k],
                              list) and test[i][j] in poss[i][k]:
                    poss[i][k].remove(test[i][j])

                if isinstance(poss[k][j],
                              list) and test[i][j] in poss[k][j]:
                    poss[k][j].remove(test[i][j])

        if not (isinstance(poss[i][j], list)) or len(poss[i][j])==1:
            for k in range(9):
                if isinstance(poss[i][k],
                              list) and poss[i][j] in poss[i][k]:
                    poss[i][k].remove(poss[i][j])

                if isinstance(poss[k][j],
                              list) and poss[i][j] in poss[k][j]:
                    poss[k][j].remove(poss[i][j])        
    return poss


# function to identify where only one occurrance of a number in row col or cell implies that's correct location for it

def findUnique(poss):
    for i in range(9):
        rowcount = colcount = [0 for _ in range(9)]
        for j in range(9):
            # if list iterate through and count value of each member
            if isinstance(poss[i][j], list):
                for k in range(len(poss[i][j])):
                    rowcount[poss[i][j][k] - 1] += 1
            else:
                rowcount[poss[i][j]-1] += 1
                
            # if list iterate through and count value of each member
            if isinstance(poss[j][i], list):
                for k in range(len(poss[j][i])):
                    colcount[poss[j][i][k] - 1] += 1
            else:
                rowcount[poss[j][i]-1] += 1
#  if unique in row it must be it
        for x in range(9):
            if isinstance(poss[i][x], list):
                for y in range(9):
                    if rowcount[y] == 1 and y + 1 in poss[i][x]: 
                            poss[i][x] = y + 1
                            break   

                        #  if unique in column it must be it
            if isinstance(poss[x][i], list):
                for y in range(9):
                    if colcount[y] == 1 and y + 1 in poss[x][i]:
                            poss[x][i] = y + 1
                            break
                                
    return poss

def lockinsingles(poss):
    for (i,j) in product(range(0,9), repeat  = 2):
        if isinstance(poss[i][j],list):
            if len(poss[i][j])==1:
                poss[i][j] = poss[i][j][0]
    return poss

def testThirdNestList(list_to_test):
    res = any(isinstance(j, list) for sub in list_to_test for j in sub)
    return res


def checkCellUniques(poss):
    # Check if the unique number occurs only once in the 3x3 square.
    for (i,j) in product(range(0,9), repeat  = 2):
        if isinstance(poss[i][j], list):
            for k in range(len(poss[i][j])):    
                        square_x = (i // 3) * 3
                        square_y = (j // 3) * 3
                        unique = poss[i][j][k]
                        count = 0
                        for m in range(square_x, square_x + 3):
                            for n in range(square_y, square_y + 3):
                                if isinstance(poss[m][n], list) and unique in poss[m][n]:
                                    count += 1
                                elif poss[m][n] == unique:
                                    count += 1

                        if count == 1:
                            poss[i][j] = poss[i][j][k]
                            break
    return poss

#  rewritten function based on watching video
def solveSudoku(incompleteSudoku):
    for (row, col) in product(range(0,9), repeat=2):
        if incompleteSudoku[row][col] == 0:
            for candidate in range(1,10):
                permitted = True #  set to true firstly and change if not
                for i in range(0,9):
                    #  if candidates occur in row or column it is not permitted
                    if (incompleteSudoku[i][col] == candidate) or (incompleteSudoku[row][i] == candidate):
                        permitted = False; break
                for (i, j) in product(range(0,3), repeat=2):    
                    if incompleteSudoku[row-row%3+i][col-col%3+j] == candidate:
                        permitted = False; break # not allowed in box
                if permitted:
                    incompleteSudoku[row][col] = candidate
                    if attempt := solveSudoku(incompleteSudoku):
                        return attempt
                    else:
                        incompleteSudoku[row][col] = 0
            return False
    return incompleteSudoku




def solve_sudoku(puzzle):
    for (row, col) in product(range(0,9), repeat=2):
        if puzzle[row][col] == 0: # find an unassigned cell
            for num in range(1,10):
                allowed = True # check if num is allowed in row/col/box
                for i in range(0,9):
                    if (puzzle[i][col ] == num) or (puzzle[row][i] == num):
                        allowed = False; break # not allowed in row or col
                for (i, j) in product(range(0,3), repeat=2):    
                    if puzzle[row-row%3+i][col-col%3+j] == num:
                        allowed = False; break # not allowed in box
                if allowed:       
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False # could not place a number in this cell

            
    return puzzle