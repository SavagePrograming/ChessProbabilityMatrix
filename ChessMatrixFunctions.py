import numpy, TensorFuntions, pygame

board = pygame.image.load('pictures/chess2.jpg')
imagelocwhite = ['pictures/pawn.png', 'pictures/rook.png', 'pictures/knight.png',
                 'pictures/bishop.png', 'pictures/queen.png', 'pictures/king.png']
imagelocblack = ['pictures/bpawn.png', 'pictures/brook.png', 'pictures/bknight.png',
                 'pictures/bbishop.png', 'pictures/bqueen.png', 'pictures/bking.png']

imagesWhite = map(pygame.image.load, imagelocwhite)
imagesBlack = map(pygame.image.load, imagelocblack)

peices = ["Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Rook", "Rook", "Knight", "Knight", "Bishop",
          "Bishop", "Queen", "King"]


def MakeNextBoards(Same, Other, color):
    # print numpy.array(getPawnMoves(Same, Other, color, 0)).shape
    newSame = numpy.array([[[0.0] * 16] * 8] * 8)
    MOVES = [numpy.reshape(getPawnMoves(Same, Other, color, 0), (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 1), (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 2), (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 3), (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 4), (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 5), (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 6), (8, 8, 8, 8, 1)),
             numpy.reshape(getPawnMoves(Same, Other, color, 7), (8, 8, 8, 8, 1)),
             numpy.reshape(getRookMoves(Same, Other, color, 8), (8, 8, 8, 8, 1)),
             numpy.reshape(getRookMoves(Same, Other, color, 9), (8, 8, 8, 8, 1)),
             numpy.reshape(getKnightMoves(Same, Other, color, 10), (8, 8, 8, 8, 1)),
             numpy.reshape(getKnightMoves(Same, Other, color, 11), (8, 8, 8, 8, 1)),
             numpy.reshape(getBishopMoves(Same, Other, color, 12), (8, 8, 8, 8, 1)),
             numpy.reshape(getBishopMoves(Same, Other, color, 13), (8, 8, 8, 8, 1)),
             numpy.reshape(getQueenMoves(Same, Other, color, 14), (8, 8, 8, 8, 1)),
             numpy.reshape(getKingMoves(Same, Other, color, 15), (8, 8, 8, 8, 1))]
    # testDif(moves2dif, Same)
    MOVES = numpy.concatenate(MOVES, 4)
    # print sum(sum(sum(sum(sum(MOVES)))))
    # print "inside1\n" + "\n".join(
    #     TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(0, 1, TensorFuntions.sumDimentions(4, 4, MOVES)),
    #                                       TensorFuntions.getMaxSizeRecursivly(
    #                                           TensorFuntions.sumDimentions(0, 1,
    #                                                                        TensorFuntions.sumDimentions(4,
    #                                                                                                     4,
    #                                                                                                     MOVES))))[1])
    MOVES, newSame = condenceMoves(MOVES, Same, newSame)

    REMOVES = adjustForPawnTaking(Same, MOVES)
    # print "inside2\n" + "\n".join(
    #     TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(0, 1, TensorFuntions.sumDimentions(4, 4, MOVES)),
    #                                       TensorFuntions.getMaxSizeRecursivly(
    #                                           TensorFuntions.sumDimentions(0, 1,
    #                                                                        TensorFuntions.sumDimentions(4,
    #                                                                                                     4,
    #                                                                                                     MOVES))))[1])
    # # NEXT = [numpy.reshape(getPawnNext(Same, Other, color, MOVES, 0), (8, 8, 1)),
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



    return newSame + TensorFuntions.sumDimentions(0, 1, MOVES), Other * (1 - TensorFuntions.sumDimentions(0, 1, REMOVES)) # numpy.array(TensorFuntions.MultiplyTogether(Other, 1 - RemovedPeices))


# def testDif(moves2dif, Same):
#     moves2dif_ = TensorFuntions.sumDimentions(2, 2, Same)
#     for x in range(0, 8):
#         for y in range(0, 8):
#             # print moves2dif_[x][y],moves2dif[x][y]
#             if moves2dif_[x][y] != moves2dif[x][y]:
#                 print "MISS"
def condenceMoves(MOVES, Same, newSame):
    TOTAL = sum(sum(sum(sum(sum(MOVES)))))
    MOVES2 = 0 * MOVES
    moves2dif = 0
    if TOTAL > 0:
        for Number in range(0, 16):
            OTHERS = TOTAL - sum(sum(sum(sum(MOVES[:, :, :, :, Number]))))
            for x in range(0, 8):
                for y in range(0, 8):
                    if (Same[x][y][Number] > 0):
                        if sum(sum(MOVES[x, y, :, :, Number])) > 0:
                            MOVES2[x, y, :, :, Number] = MOVES[x, y, :, :, Number] / (
                            sum(sum(MOVES[x, y, :, :, Number])) / Same[x][y][Number] + OTHERS)
                            # print "inside2\n" + "\n".join(
                            #     TensorFuntions.printRecusivlySize(MOVES[x, y, :, :, Number],
                            #                                       TensorFuntions.getMaxSizeRecursivly(MOVES[x, y, :, :, Number]))[1])
                            # print "divide", (sum(sum(MOVES[x, y, :, :, Number])) / Same[x][y][Number] + OTHERS)
                            newSame[x][y][Number] += (Same[x][y][Number]) * (OTHERS) / (
                                sum(sum(MOVES[x, y, :, :, Number])) / Same[x][y][Number] + OTHERS)
                        else:
                            newSame[x][y][Number] += Same[x][y][Number]
        # print "Compare", SUM, TOTAL
        return MOVES2, newSame
    else:
        return MOVES, Same


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
                    # print x + 1, y
                    array[x][y][x + 1][y] += OtherSumed[x + 1][y] * SameSumed[x + 1][y] * Same[x][y][Number]
                    if y + 1 < 8:
                        # print x + 1, y + 1
                        array[x][y][x + 1][y] += (1 - OtherSumed[x + 1][y + 1]) * Same[x][y][Number]
                    if y - 1 >= 0:
                        # print x + 1, y - 1
                        array[x][y][x + 1][y] += (1 - OtherSumed[x + 1][y - 1]) * Same[x][y][Number]
                if x == 1:
                    array[x][y][x + 2][y] += OtherSumed[x + 2][y] * SameSumed[x + 2][y] * Same[x][y][Number]
        return array
    else:
        for x in range(0, 8):
            for y in range(0, 8):
                if x - 1 >= 0 and Same[x][y][Number] > 0:
                    # print x - 1, y
                    array[x][y][x - 1][y] += OtherSumed[x - 1][y] * SameSumed[x - 1][y] * Same[x][y][Number]
                    if y + 1 < 8:
                        # print x - 1, y + 1
                        array[x][y][x - 1][y + 1] += (1 - OtherSumed[x - 1][y + 1]) * Same[x][y][Number]
                    if y - 1 >= 0:
                        # print x - 1, y - 1
                        array[x][y][x - 1][y - 1] += (1 - OtherSumed[x - 1][y - 1]) * Same[x][y][Number]
                if x == 6:
                    array[x][y][x - 2][y] += OtherSumed[x - 2][y] * SameSumed[x - 2][y] * Same[x][y][Number]
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
                total *= (SameSumed[x][y - y_shift])
                array[x][y][x][y - y_shift] += total * Same[x][y][Number]
                total *= (OtherSumed[x][y - y_shift])
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
            while y - shift >= 0 and x - shift >= 0:
                total *= (SameSumed[x - shift][y - shift])
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


def adjustForPawnTaking(Same, MOVES):
    MOVES2 = MOVES.copy()
    for x in range(0, 8):
        for y in range(0, 8):
            for Number in range(0, 8):
                if Same[x][y][Number] > 0:
                    MOVES2[x][y][x][y][Number] = 0.0
    return MOVES2


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
    # printTurnStats(a, b, COLOR)
    while N > count:
        count += 1
        b, a = MakeNextBoards(a, b, COLOR)

        if count % rate == 0:
            if delay != 0:
                pygame.time.delay(delay)
            # printTurnStats(a, b, COLOR)
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
    print "Board"
    print "\n".join(TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, b[:, :, :]),
                                                      TensorFuntions.getMaxSizeRecursivly(
                                                          TensorFuntions.sumDimentions(2, 2, b[:, :, :])))[1])

    print "Total Peices:", sum(sum(sum(b)))
    print "Pawns", sum(sum(sum(b[:, :, 0:8])))
    print "Rooks", sum(sum(sum(b[:, :, 8:10])))
    print "Knights", sum(sum(sum(b[:, :, 10:12])))
    print "Bishops", sum(sum(sum(b[:, :, 12:14])))
    print "Queens", sum(sum(b[:, :, 14]))
    print "Kings", sum(sum(b[:, :, 15]))


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


def calcStats(Same, Other, Color):
    pass