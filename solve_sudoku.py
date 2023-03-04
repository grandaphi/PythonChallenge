import sudok, pandas as pd

test = [[0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0], [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3], [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]]

# test = [[0, 4, 0, 0, 2, 0, 8, 6, 5], [7, 0, 0, 6, 0, 8, 0, 0, 0],
#         [1, 0, 0, 0, 0, 4, 7, 0, 2], [0, 1, 8, 7, 4, 0, 0, 0, 0],
#         [0, 0, 5, 2, 0, 9, 6, 0, 0], [0, 0, 0, 0, 8, 6, 1, 5, 0],
#         [9, 0, 1, 5, 0, 0, 0, 0, 6], [0, 0, 0, 8, 0, 2, 0, 0, 7],
#         [8, 7, 3, 0, 6, 0, 0, 2, 0]]

# count = 0
# while (sudok.testThirdNestList(poss) and count < 100):
#     poss = sudok.removeDupes(test, poss)
#     poss = sudok.lockinsingles(poss)
#     poss = sudok.checkCellUniques(poss)
#     poss = sudok.findUnique(poss)
#     count += 1
print(test)
poss = sudok.solve_sudoku(test)
df = pd.DataFrame(poss)
print(df)
