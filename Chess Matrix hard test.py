


class rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.infinite = False
        self.simplify()

    def simplify(self):
        if self.denominator == 0:
            self.infinite = True
        elif self.numerator == 0:
            self.denominator = 1
        else:
            while self.denominator % 1 > 0 or self.numerator % 1 > 0:
                self.denominator *= 10
                self.numerator *= 10
            ##            print self.denominator, self.numerator
            self.denominator = int(self.denominator)
            self.numerator = int(self.numerator)
            num = gcd(self.denominator, self.numerator)
            self.denominator /= num
            self.numerator /= num

    def __str__(self):
        if self.infinite:
            return "infinite"
        elif self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        if isinstance(other, rational):
            gc = gcd(self.denominator, other.denominator)
            return rational(self.numerator * other.denominator / gc + other.numerator * self.denominator / gc,
                            lcm(self.denominator, other.denominator))
        elif isinstance(other, float) or isinstance(other, int):
            return rational(self.numerator + other * self.denominator, self.denominator)
        else:
            raise TypeError(self, other)

    def __radd__(self, other):
        if isinstance(other, rational):
            gc = gcd(self.denominator, other.denominator)
            return rational(self.numerator * other.denominator / gc + other.numerator * self.denominator / gc,
                            lcm(self.denominator, other.denominator))
        elif isinstance(other, float) or isinstance(other, int):
            return rational(self.numerator + other * self.denominator, self.denominator)
        else:
            raise TypeError(self, other)

    def toFloat(self):
        return float(self.numerator) / float(self.denominator)


def gcd(a, b):
    if max(a, b) % min(a, b) == 0:
        return min(a, b)
    ##    print a, b
    return gcd(min(a, b), max(a, b) % min(a, b))


def lcm(a, b):
    return a * b / gcd(a, b)


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
                print str(array[z][x][y]) + " " * (5 - len(str(array[z][x][y]))),
                # print str(float(int(1000*array[z][x][y].toFloat())) / 1000.0) + "0" * (5 - len(str(float(int(1000*array[z][x][y].toFloat())) / 1000.0))),
            print "\t",
        print


def lcm2(a, b):
    if a > 0 and b > 0:
        return lcm(b.denominator, a)
    else:
        if a > 0:
            return a
        elif b > 0:
            return b
        else:
            return 1


def getDenom(board):
    return reduce(lcm, map(lambda b: reduce(lcm, map(lambda r: reduce(lcm2, r, 1), b)), board))


def makeNextBoard(b):
    board2 = []

    total = []

    for z in range(0, len(b)):
        board2.append([[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]])
    TOTAL = getDenom(b)

    for z in range(0, len(b)):
        total.append(sum(map(sum, b[z])).toFloat())
    for z in range(0, len(b)):
        for x in range(0, 8):
            for y in range(0, 8):
                b[z][x][y] = b[z][x][y].numerator * TOTAL / b[z][x][y].denominator

    for z in range(0, len(b)):
        for x in range(0, 8):
            for y in range(0, 8):
                for mod in [[1, 2], [1, -2], [-1, -2], [-1, 2], [2, 1], [2, -1], [-2, -1], [-2, 1]]:
                    if 7 >= y + mod[1] >= 0 and 7 >= x + mod[0] >= 0 and b[z][x][y] > 0:
                        board2[z][x + mod[0]][y + mod[1]] += b[z][x][y]
                        for z_ in range(0, len(b)):
                            for x_ in range(0, 8):
                                for y_ in range(0, 8):
                                    if z != z_:  # or x != x_ or y != y_:
                                        board2[z_][x_][y_] += b[z_][x_][y_]

    for z in range(0, len(b)):
        TOTAL = sum(map(sum, board2[z]))
        if TOTAL == 0:
            TOTAL = 1
        for x in range(0, 8):
            for y in range(0, 8):
                board2[z][x][y] = rational(board2[z][x][y] * total[z], TOTAL)
            ##    for z in range(0,len(b)):
            ##        for x in range(0,8):
            ##            for y in range(0,8):
            ####                print  (1.0 - (total[z]) / TOTAL)
            ##                board2[z][x][y] = b[z][x][y] * (1.0 - ( total[z]/ TOTAL))  + float(add[z][x][y]) / float(TOTAL) #b[z][x][y] * (1.0 - (total[z]) / (TOTAL)  + float(add[z][x][y]) / float(TOTAL) # * (1.0 - (remove[z][x][y]/total[z]))
            ##            if (board2[x][y] < 0):
            ##                print b[x][y] , float(add[x][y]) / float(total) , -float(remove[x][y]) / float(total)
    return board2


board = [[[1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
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
for z in range(0, len(board)):
    for x in range(0, 8):
        for y in range(0, 8):
            ##                print  (1.0 - (total[z]) / TOTAL)
            board[z][x][y] = rational(board[z][x][y], 1)
print getDenom(board)
PRINT(board)
print sum(map(sum, board[0]))
for i in range(0, 5):
    print "board"
    PRINT(board)
    print "Sum:", SUM(board)
    board = makeNextBoard(board)
