import numpy, TensorFuntions, pygame

board = pygame.image.load('pictures/chess2.jpg')
imagelocwhite = ['pictures/pawn.png', 'pictures/rook.png', 'pictures/knight.png',
                 'pictures/bishup.png', 'pictures/queen.png', 'pictures/king.png']
imagelocblack = ['pictures/bpawn.png', 'pictures/brook.png', 'pictures/bknight.png',
                 'pictures/bbishup.png', 'pictures/bqueen.png', 'pictures/bking.png']

imagesWhite = map(pygame.image.load, imagelocwhite)
imagesBlack = map(pygame.image.load, imagelocblack)

peices = ["Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Rook", "Rook", "Knight", "Knight", "Bishop",
          "Bishop", "Queen", "King"]


def MakeNextBoards(Same, Other, color):
    print numpy.array(getPawnMoves(Same, Other, color, 0)).shape
    MOVES = [numpy.reshape(getPawnMoves(Same, Other, color, 0),  (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 1),  (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 2),  (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 3),  (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 4),  (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 5),  (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 6),  (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 7),  (8, 8, 8, 8, 1)),
             numpy.reshape(getRookMoves(Same, Other, color, 8),  (8, 8, 8, 8, 1)),
             numpy.reshape(getRookMoves(Same, Other, color, 9),  (8, 8, 8, 8, 1)),
             numpy.reshape(getKnightMoves(Same, Other, color, 10),  (8, 8, 8, 8, 1)),
             numpy.reshape(getKnightMoves(Same, Other, color, 11),  (8, 8, 8, 8, 1)),
             numpy.reshape(getBishopMoves(Same, Other, color, 12),  (8, 8, 8, 8, 1)),
             numpy.reshape(getBishopMoves(Same, Other, color, 13),  (8, 8, 8, 8, 1)),
             numpy.reshape(getQueenMoves(Same, Other, color, 14),  (8, 8, 8, 8, 1)),
             numpy.reshape(getKingMoves(Same, Other, color, 15),  (8, 8, 8, 8, 1))]
    MOVES = numpy.concatenate(MOVES, 4)

    # NEXT = [numpy.reshape(getPawnNext(Same, Other, color, MOVES, 0), (8, 8, 1)),
    #          numpy.reshape(getPawnNext(Same, Other, color, MOVES, 1), (8, 8, 1)),
    #          numpy.reshape(getPawnNext(Same, Other, color, MOVES, 2), (8, 8, 1)),
    #          numpy.reshape(getPawnNext(Same, Other, color, MOVES, 3), (8, 8, 1)),
    #          numpy.reshape(getPawnNext(Same, Other, color, MOVES, 4), (8, 8, 1)),
    #          numpy.reshape(getPawnNext(Same, Other, color, MOVES, 5), (8, 8, 1)),
    #          numpy.reshape(getPawnNext(Same, Other, color, MOVES, 6), (8, 8, 1)),
    #          numpy.reshape(getPawnNext(Same, Other, color, MOVES, 7), (8, 8, 1)),
    #          numpy.reshape(getRookNext(Same, Other, color, MOVES, 8), (8, 8, 1)),
    #          numpy.reshape(getRookNext(Same, Other, color, MOVES, 9), (8, 8, 1)),
    #          numpy.reshape(getKnightNext(Same, Other, color, MOVES, 10), (8, 8, 1)),
    #          numpy.reshape(getKnightNext(Same, Other, color, MOVES, 11), (8, 8, 1)),
    #          numpy.reshape(getBishopNext(Same, Other, color, MOVES, 12), (8, 8, 1)),
    #          numpy.reshape(getBishopNext(Same, Other, color, MOVES, 13), (8, 8, 1)),
    #          numpy.reshape(getQueenNext(Same, Other, color, MOVES, 14), (8, 8, 1)),
    #          numpy.reshape(getKingNext(Same, Other, color, MOVES, 15), (8, 8, 1))]
    # NEXT = numpy.concatenate(NEXT, 2)
    # Same = NEXT
    print "inside\n" + "\n".join(TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(0, 1, TensorFuntions.sumDimentions(4, 4, MOVES)),
                                                      TensorFuntions.getMaxSizeRecursivly(
                                                          TensorFuntions.sumDimentions(0, 1,
                                                                                       TensorFuntions.sumDimentions(4,
                                                                                                                    4,
                                                                                                                    MOVES))))[1])


    return Same , Other  # numpy.array(TensorFuntions.MultiplyTogether(Other, 1 - RemovedPeices))

def getPawnMoves(Same, Other, color, Number):
    array = numpy.array([[[[0.0] * 8] * 8] * 8] * 8)
    # moved = numpy.concatenate(([[0.0] * 8], Same[:-1, :, Number]), 0)
    # taking = numpy.concatenate((moved[:, 1:], [[0.0]] * 8), 1) + \
    #          numpy.concatenate(([[0.0]] * 8, moved[:, :-1]), 1)
    OtherSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Other)
    SameSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Same)
    if color:
        for x in range(0, 8):
            for y in range(0, 8):
                if x + 1 < 8 and Same[x][y][Number] > 0:
                    array[x][y][x + 1][y] += OtherSumed[x + 1][y] * SameSumed[x + 1][y] * Same[x][y][Number]
                    if y + 1 < 8:
                        array[x][y][x + 1][y] += (1 - OtherSumed[x + 1][y + 1]) * Same[x][y][Number]
                    if y - 1 >= 0:
                        array[x][y][x + 1][y] += (1 - OtherSumed[x + 1][y - 1]) * Same[x][y][Number]
        return array
    else:
        for x in range(0, 8):
            for y in range(0, 8):
                if x - 1 >= 0 and Same[x][y][Number] > 0:
                    array[x][y][x - 1][y] += OtherSumed[x - 1][y] * SameSumed[x - 1][y] * Same[x][y][Number]
                    if y + 1 < 8:
                        array[x][y][x - 1][y + 1] += (1 - OtherSumed[x - 1][y + 1]) * Same[x][y][Number]
                    if y - 1 >= 0:
                        array[x][y][x - 1][y - 1] += (1 - OtherSumed[x - 1][y - 1]) * Same[x][y][Number]
        return array

def getKnightMoves(Same, Other, color, Number):
    array = numpy.array([[[[0.0] * 8] * 8] * 8] * 8)
    SameSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Same)
    for x in range(0, 8):
        for y in range(0, 8):
            for mod in [[1, 2], [1, -2], [-1, -2], [-1, 2], [2, 1], [2, -1], [-2, -1], [-2, 1]]:
                if 7 >= y + mod[1] >= 0 and 7 >= x + mod[0] >= 0:
                    array[x][y][x + mod[0]][y + mod[1]] += SameSumed[x + mod[0]][y + mod[1]] * Same[x][y][Number]
    return array

def getRookMoves(Same, Other, color, Number):
    array = numpy.array([[[[0.0] * 8] * 8] * 8] * 8)
    OtherSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Other)
    SameSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Same)
    for x in range(0, 8):
        for y in range(0, 8):
            x_shift = 1
            total = 1
            while x_shift + x < 8:
                total *= (SameSumed[x + x_shift][y])
                array[x][y][x + x_shift][y] += total * Same[x][y][Number]
                total *= (OtherSumed[x + x_shift][y])
                x_shift += 1
            x_shift = 1
            total = 1
            while x - x_shift >= 0:
                total *= (SameSumed[x - x_shift][y])
                array[x][y][x - x_shift][y] += total * Same[x][y][Number]
                total *= (OtherSumed[x - x_shift][y])
                x_shift += 1


            y_shift = 1
            total = 1
            while y_shift + y < 8:
                total *= (SameSumed[x][y + y_shift])
                array[x][y][x][y + y_shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x][y + y_shift])
                y_shift += 1
            y_shift = 1
            total = 1
            while y - y_shift >= 0:
                total *= (SameSumed[x][y - y_shift ])
                array[x][y][x][y - y_shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x][y - y_shift ])
                y_shift += 1
    return array

def getBishopMoves(Same, Other, color, Number):
    array = numpy.array([[[[0.0] * 8] * 8] * 8] * 8)
    OtherSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Other)
    SameSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Same)
    for x in range(0, 8):
        for y in range(0, 8):
            shift = 1
            total = 1
            while shift + x < 8 and shift + y < 8:
                total *= (SameSumed[x + shift][y + shift])
                array[x][y][x + shift][y + shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x + shift][y + shift])
                shift += 1
            shift = 1
            total = 1
            while x - shift >= 0 and shift + y < 8:
                total *= (SameSumed[x - shift][y + shift])
                array[x][y][x - shift][y + shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x - shift][y + shift])
                shift += 1

            shift = 1
            total = 1
            while y - shift >= 0 and shift + x < 8:
                total *= (SameSumed[x + shift][y - shift])
                array[x][y][x + shift][y - shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x + shift][y - shift])
                shift += 1
            shift = 1
            total = 1
            while y - shift >= 0  and x - shift >= 0:
                total *= (SameSumed[x- shift][y - shift])
                array[x][y][x - shift][y - shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x - shift][y - shift])
                shift += 1
    return array

def getKingMoves(Same, Other, color, Number):
    array = numpy.array([[[[0.0] * 8] * 8] * 8] * 8)
    SameSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Same)
    for x in range(0, 8):
        for y in range(0, 8):
            for mod in [[1, 1], [1, -1], [-1, -1], [-1, 1], [1, 1], [1, -1], [-1, -1], [-1, 1]]:
                if 7 >= y + mod[1] >= 0 and 7 >= x + mod[0] >= 0:
                    array[x][y][x + mod[0]][y + mod[1]] += SameSumed[x + mod[0]][y + mod[1]] * Same[x][y][Number]
    return array

def getQueenMoves(Same, Other, color, Number):
    array = numpy.array([[[[0.0] * 8] * 8] * 8] * 8)
    OtherSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Other)
    SameSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Same)
    for x in range(0, 8):
        for y in range(0, 8):
            x_shift = 1
            total = 1
            while x_shift + x < 8:
                total *= (SameSumed[x + x_shift][y])
                array[x][y][x + x_shift][y] += total * Same[x][y][Number]
                total *= (OtherSumed[x + x_shift][y])
                x_shift += 1
            x_shift = 1
            total = 1
            while x - x_shift >= 0:
                total *= (SameSumed[x - x_shift][y])
                array[x][y][x - x_shift][y] += total * Same[x][y][Number]
                total *= (OtherSumed[x - x_shift][y])
                x_shift += 1

            y_shift = 1
            total = 1
            while y_shift + y < 8:
                total *= (SameSumed[x][y + y_shift])
                array[x][y][x][y + y_shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x][y + y_shift])
                y_shift += 1
            y_shift = 1
            total = 1
            while y - y_shift >= 0:
                total *= (SameSumed[x][y - y_shift])
                array[x][y][x][y - y_shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x][y - y_shift])
                y_shift += 1
            shift = 1
            total = 1
            while shift + x < 8 and shift + y < 8:
                total *= (SameSumed[x + shift][y + shift])
                array[x][y][x + shift][y + shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x + shift][y + shift])
                shift += 1
            shift = 1
            total = 1
            while x - shift >= 0 and shift + y < 8:
                total *= (SameSumed[x - shift][y + shift])
                array[x][y][x - shift][y + shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x - shift][y + shift])
                shift += 1

            shift = 1
            total = 1
            while y - shift >= 0 and shift + x < 8:
                total *= (SameSumed[x + shift][y - shift])
                array[x][y][x + shift][y - shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x + shift][y - shift])
                shift += 1
            shift = 1
            total = 1
            while y - shift >= 0 and x - shift >= 0:
                total *= (SameSumed[x - shift][y - shift])
                array[x][y][x - shift][y - shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x - shift][y - shift])
                shift += 1
    return array

def getPawnNext(Same, Other, color, MOVES, Number):
    if color:
        moved = numpy.concatenate(([[0.0] * 8], Same[:-1, :, Number]), 0)
        taking = numpy.concatenate((moved[:, 1:], [[0.0]] * 8), 1) + \
                     numpy.concatenate(([[0.0]] * 8, moved[:, :-1]), 1)
        OtherSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Other)
        SameSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Same)
        return moved * OtherSumed * SameSumed + taking * (1 - OtherSumed)
    else:
        moved = numpy.concatenate((Same[1:, :, Number], [[0.0] * 8]), 0)
        taking = numpy.concatenate((moved[:, 1:], [[0.0]] * 8), 1) + \
                 numpy.concatenate(([[0.0]] * 8, moved[:, :-1]), 1)
        OtherSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Other)
        SameSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Same)
        return Same[:,:, Number]

def getKnightNext(Same, Other, color, MOVES, Number):
    movedh = numpy.concatenate(([[0.0] * 8], Same[:-1, :, Number]), 0) + numpy.concatenate((Same[1:, :, Number], [[0.0] * 8]), 0)
    movedv = numpy.concatenate((Same[:, 1:, Number], [[0.0]] * 8), 1) + \
                 numpy.concatenate(([[0.0]] * 8, Same[:, :-1, Number]), 1)
    moved = numpy.concatenate((movedh[:, 2:], [[0.0] * 2] * 8), 1) + \
            numpy.concatenate(([[0.0] * 2] * 8, movedh[:, :-2]), 1) + \
            numpy.concatenate(([[0.0] * 8]* 2, movedv[:-2, :]), 0) + \
            numpy.concatenate((movedv[2:, :], [[0.0] * 8]* 2), 0)
    SameSumed = TensorFuntions.multiplyDimentions(2, 2, 1 - Same)
    return Same[:,:, Number]

def getRookNext(Same, Other, color, MOVES, Number):
    moved = numpy.concatenate(([[0.0] * 8], Same[:-1, :, Number]), 0)
    return Same[:,:, Number]

def getBishopNext(Same, Other, color, MOVES, Number):
    moved = numpy.concatenate(([[0.0] * 8], Same[:-1, :, Number]), 0)
    return Same[:,:, Number]

def getKingNext(Same, Other, color, MOVES, Number):
    moved = numpy.concatenate(([[0.0] * 8], Same[:-1, :, Number]), 0)
    return Same[:,:, Number]

def getQueenNext(Same, Other, color, MOVES, Number):
    moved = numpy.concatenate(([[0.0] * 8], Same[:-1, :, Number]), 0)
    return Same[:,:, Number]

def getOutArray(x, y, xprime, yprime, Same, Other, rookNumber):
    if abs(y - yprime) > 1:
        intheway = sum(Same[x, min(y, yprime) + 1:max(y, yprime), :])
        inthewayOther = sum(Other[x, min(y, yprime) + 1:max(y, yprime), :])

        return TensorFuntions.NegateProduct(intheway) * TensorFuntions.NegateProduct(inthewayOther) * Same[
            x, y, rookNumber] * TensorFuntions.NegateProduct(Same[x, yprime, :])

    else:
        if abs(xprime - x) > 1:

            inthewayself = sum(Same[min(x, xprime) + 1:max(x, xprime), y])
            inthewayOther = sum(Other[min(x, xprime) + 1:max(x, xprime), y])

            return TensorFuntions.NegateProduct(inthewayself) * TensorFuntions.NegateProduct(inthewayOther) * Same[
                x, y, rookNumber] * TensorFuntions.NegateProduct(Same[xprime, y])
        else:
            if abs(xprime - x) == 1:
                return Same[x, y, rookNumber] * TensorFuntions.NegateProduct(Same[xprime, y, :])
            else:
                return Same[x, y, rookNumber] * TensorFuntions.NegateProduct(Same[x, yprime, :])



def goNGenerations(a, b, COLOR, N):
    count = 1
    while N > count:
        count += 1
        b, a = MakeNextBoards(a, b, COLOR)
        COLOR = not COLOR
    return a, b, COLOR


def goNGenerationsVisual(a, b, COLOR, N, delay, Screen, rate):
    count = 1
    printTurnStats(a, b, COLOR)
    while N > count:
        count += 1
        b, a = MakeNextBoards(a, b, COLOR)

        if count % rate == 0:
            if delay != 0:
                pygame.time.delay(delay)
            printTurnStats(a, b, COLOR)
            Draw(a, b, COLOR, Screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    count = N
        COLOR = not COLOR
    return a, b, COLOR


def Draw(Same, Other, COLOR, Screen):
    Screen.blit(board, [0, 0])
    for y in range(0, 8):
        for x in range(0, 8):
            for p in range(0, 6):
                if p == 0:
                    drawSquare(x, y, 0, sum(Same[y, x, :8]), not COLOR, Screen)
                    drawSquare(x, y, 0, sum(Other[y, x, :8]), COLOR, Screen)
                elif 0 < p < 4:
                    drawSquare(x, y, p, sum(Same[y, x, 6 + 2 * p:8 + 2 * p]), not COLOR, Screen)
                    drawSquare(x, y, p, sum(Other[y, x, 6 + 2 * p:8 + 2 * p]), COLOR, Screen)
                else:
                    drawSquare(x, y, p, Same[y][x][10 + p], not COLOR, Screen)
                    drawSquare(x, y, p, Other[y][x][10 + p], COLOR, Screen)
                    # map(map, [map] * 8, [[map] * 8] * 8, [[[drawSquare] * 6] * 8] * 8,
                    #     [[[0] * 6] * 8, [[1] * 6] * 8, [[2] * 6] * 8, [[3] * 6] * 8, [[4] * 6] * 8, [[5] * 6] * 8, [[6] * 6] * 8,
                    #      [[7] * 6] * 8],
                    #     [[[0] * 6, [1] * 6, [2] * 6, [3] * 6, [4] * 6, [5] * 6, [6] * 6, [7] * 6]] * 8,
                    #     [[[0, 1, 2, 2, 4, 5]] * 8] * 8, Same, [[[COLOR] * 6] * 8] * 8, [[[Screen] * 6] * 8] * 8)
                    #
                    # map(map, [map] * 8, [[map] * 8] * 8, [[[drawSquare] * 6] * 8] * 8,
                    #     [[[0] * 6] * 8, [[1] * 6] * 8, [[2] * 6] * 8, [[3] * 6] * 8, [[4] * 6] * 8, [[5] * 6] * 8, [[6] * 6] * 8,
                    #      [[7] * 6] * 8],
                    #     [[[0] * 6, [1] * 6, [2] * 6, [3] * 6, [4] * 6, [5] * 6, [6] * 6, [7] * 6]] * 8,
                    #     [[[0, 1, 2, 2, 4, 5]] * 8] * 8, Other, [[[not COLOR] * 6] * 8] * 8, [[[Screen] * 6] * 8] * 8)


def drawSquare(x, y, p, opacity, COLOR, Screen):
    if not COLOR:
        Screen2 = Screen.copy()
        Screen.blit(imagesWhite[p], [50 * x, 50 * y])
        # print opacity
        Screen2.set_alpha(255 - 255 * opacity)
        Screen.blit(Screen2, [0, 0])
    else:
        Screen2 = Screen.copy()
        Screen.blit(imagesBlack[p], [50 * x, 50 * y])
        Screen2.set_alpha(255 - 255 * opacity)
        Screen.blit(Screen2, [0, 0])


def makeScreen():
    pygame.init()
    Screen = pygame.display.set_mode([450, 450])
    Screen.fill([255, 255, 255])
    return Screen


def printBoardStats(b):
    # print "Pawns"
    # print "\n".join(TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, b[:, :, :8]),
    #                                                   TensorFuntions.getMaxSizeRecursivly(
    #                                                       TensorFuntions.sumDimentions(2, 2, b[:, :, :8])))[1])
    # print "Rooks"
    # print "\n".join(TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, b[:, :, 8:10]),
    #                                                   TensorFuntions.getMaxSizeRecursivly(
    #                                                       TensorFuntions.sumDimentions(2, 2, b[:, :, 8:10])))[1])
    print "Knights"
    print "\n".join(TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, b[:, :, :]),
                                                      TensorFuntions.getMaxSizeRecursivly(
                                                          TensorFuntions.sumDimentions(2, 2, b[:, :, :])))[1])

    print sum(sum(sum(b)))


def printTurnStats(a, b, Color):
    if Color:
        print "--------------- White----------------------"
        printBoardStats(a)
        # print "------------------Black------------------"
        # printBoardStats(b)
    else:
        # print "--------------- White----------------------"
        # printBoardStats(b)
        print "------------------Black------------------"
        printBoardStats(a)
