#  input: sudoku as 2d list of numbers
#  output: solved sudoku
testindex = 2
test = [[0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0], [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3], [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]]

#list of all possible values of blanks before starting solve process
poss = [[
    list(range(1, 10)) if test[i][j] == 0 else test[i][j] for j in range(9)
] for i in range(9)]
# print(poss)

# check rows , columns

for i in range(len(test)):
    for j in range(len(test[i])):
        if test[i][j] != 0:
            for k in range(9):
                if isinstance(poss[i][k], list) and test[i][j] in poss[i][k]:
                    poss[i][k].remove(test[i][j])

                if isinstance(poss[k][j], list) and test[i][j] in poss[k][j]:
                    poss[k][j].remove(test[i][j])

            # do 3x3 cells here if i < 3 i > 3 and i < 6 etc
            if i < 3:
                for x in range(3):
                    if j < 3:
                        for y in range(3):
                            if isinstance(poss[x][y],
                                          list) and test[i][j] in poss[x][y]:
                                poss[x][y].remove(test[i][j])
                    elif j < 6:
                        for y in range(3, 6):
                            if isinstance(poss[x][y],
                                          list) and test[i][j] in poss[x][y]:
                                poss[x][y].remove(test[i][j])

                    elif j < 9:
                        for y in range(6, 9):
                            if isinstance(poss[x][y],
                                          list) and test[i][j] in poss[x][y]:
                                poss[x][y].remove(test[i][j])
            elif i < 6:
                for x in range(3, 6):
                    if j < 3:
                        for y in range(3):
                            if isinstance(poss[x][y],
                                          list) and test[i][j] in poss[x][y]:
                                poss[x][y].remove(test[i][j])
                    elif j < 6:
                        for y in range(3, 6):
                            if isinstance(poss[x][y],
                                          list) and test[i][j] in poss[x][y]:
                                poss[x][y].remove(test[i][j])

                    elif j < 9:
                        for y in range(6, 9):
                            if isinstance(poss[x][y],
                                          list) and test[i][j] in poss[x][y]:
                                poss[x][y].remove(test[i][j])
            elif i < 9:
                for x in range(6, 9):
                    if j < 3:
                        for y in range(3):
                            if isinstance(poss[x][y],
                                          list) and test[i][j] in poss[x][y]:
                                poss[x][y].remove(test[i][j])
                    elif j < 6:
                        for y in range(3, 6):
                            if isinstance(poss[x][y],
                                          list) and test[i][j] in poss[x][y]:
                                poss[x][y].remove(test[i][j])

                    elif j < 9:
                        for y in range(6, 9):
                            if isinstance(poss[x][y],
                                          list) and test[i][j] in poss[x][y]:
                                poss[x][y].remove(test[i][j])

print("\n\n")
for i in range(9):
    print(poss[i][testindex], "\n")

# find where numbers can only occur in each row and col
for i in range(9):
    rowcount = [0 for _ in range(9)]
    colcount = [0 for _ in range(9)]
    for j in range(9):
        if isinstance(poss[i][j], list):
            for k in range(len(poss[i][j])):
                rowcount[poss[i][j][k] - 1] += 1
                
        if isinstance(poss[j][i], list):
            for k in range(len(poss[j][i])):
                colcount[poss[j][i][k] - 1] += 1

#  if number occurs only once for each row of possibilities it must occur there
    for x in range(9):
        if isinstance(poss[i][x], list):
            for y in range(9):
                if rowcount[y] == 1 and y + 1 in poss[i][x]: 
                    poss[i][x] = y + 1
                    # print("y=", y + 1)
                    
        if isinstance(poss[x][i], list):
            for y in range(9):
                if colcount[y] == 1 and y + 1 in poss[x][i]: 
                    poss[x][i] = y + 1


    # print(rowcount)

for i in range(9):
    print(poss[i][testindex], "\n")
