MOVES = [[[2, 3, 4, 4, 4, 4, 3, 2],
          [3, 4, 6, 6, 6, 6, 4, 3],
          [4, 6, 8, 8, 8, 8, 6, 4],
          [4, 6, 8, 8, 8, 8, 6, 4],
          [4, 6, 8, 8, 8, 8, 6, 4],
          [4, 6, 8, 8, 8, 8, 6, 4],
          [3, 4, 6, 6, 6, 6, 4, 3],
          [2, 3, 4, 4, 4, 4, 3, 2]],
         [[2, 3, 4, 4, 4, 4, 3, 2],
          [3, 4, 6, 6, 6, 6, 4, 3],
          [4, 6, 8, 8, 8, 8, 6, 4],
          [4, 6, 8, 8, 8, 8, 6, 4],
          [4, 6, 8, 8, 8, 8, 6, 4],
          [4, 6, 8, 8, 8, 8, 6, 4],
          [3, 4, 6, 6, 6, 6, 4, 3],
          [2, 3, 4, 4, 4, 4, 3, 2]]]

board = [[[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1.0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]]


def SUM_i(array, index):
    SUM = 0
    for row in array[index]:
        for item in row:
            SUM += item
    return SUM


def SUM(array):
    SUM = 0
    for board in array:
        for row in board:
            for item in row:
                SUM += item
    return SUM


def PRINT(array):
    for x in range(0, 8):
        for z in range(0, len(array)):
            for y in range(0, 8):
                print str(float(int(1000 * array[z][x][y])) / 1000.0) + "0" * (
                5 - len(str(float(int(1000 * array[z][x][y])) / 1000.0))),
            print "\t",
        print

def getTotalWithout(i, boards):
    return sum(map(lambda b: sum(map(sum, b)), boards)) - sum(map(sum, boards[i]))

def makeNextBoard(b):
    board2 = []

    moves = []

    total = []
    for z in range(0, len(b)):
        moves.append([[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]])
        board2.append([[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]])
    TOTAL = 0
    for z in range(0, len(b)):
        total.append(0)
        for x in range(0, 8):
            for y in range(0, 8):
                for mod in [[1, 2], [1, -2], [-1, -2], [-1, 2], [2, 1], [2, -1], [-2, -1], [-2, 1]]:
                    if 7 >= y + mod[1] >= 0 and 7 >= x + mod[0] >= 0:
                        moves[z][x + mod[0]][y + mod[1]] += b[z][x][y]
                        total[z] += b[z][x][y]
    for z in range(0, len(b)):
        for x in range(0, 8):
            for y in range(0, 8):
                board2[z][x][y] += b[z][x][y] * (getTotalWithout(z, moves)) / (MOVES[z][x][y] + getTotalWithout(z, moves))
                for mod in [[1, 2], [1, -2], [-1, -2], [-1, 2], [2, 1], [2, -1], [-2, -1], [-2, 1]]:
                    if 7 >= y + mod[1] >= 0 and 7 >= x + mod[0] >= 0:
                        board2[z][x+ mod[0]][y+ mod[1]] += b[z][x][y] / (MOVES[z][x][y] + getTotalWithout(z, moves))
    return board2

# print getTotalWithout(0, board)
# print getTotalWithout(1, board)
for i in range(0, 1000):
    print "board"
    PRINT(board)
    print "Sum:", SUM(board)
    board = makeNextBoard(board)
