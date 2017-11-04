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
    """

    :param Same: Tensor for current player
    :param Other: Tensor for other player
    :param color: True is white, False is black
    :return:
    """
    PAWNS, ROOKS = True, True
    pawnMoved, pawnRemoved, pawnAdded = [], [], []
    if PAWNS:
        for i in range(0, 8):
            pawnMoved_, pawnRemoved_, pawnAdded_ = getNewPawns(Same, Other, color, i)
            pawnMoved.append(numpy.reshape(pawnMoved_, (8, 8, 1)))
            pawnRemoved.append(pawnRemoved_)
            pawnAdded.append(numpy.reshape(pawnAdded_, (8, 8, 1)))
    else:
        for i in range(0, 8):
            pawnMoved.append(numpy.array([[[0.0]] * 8] * 8))
            pawnAdded.append(numpy.array([[[0.0]] * 8] * 8))
    if ROOKS:
        for i in range(8, 10):
            rookMoved_1, rookRemoved_1, rookAdded_1 = getNewRooks(Same, Other, color, i)
            pawnMoved.append(numpy.reshape(rookMoved_1, (8, 8, 1)))
            pawnRemoved.append(rookRemoved_1)
            pawnAdded.append(numpy.reshape(rookAdded_1, (8, 8, 1)))
    else:
        for i in range(8, 10):
            pawnMoved.append(numpy.array([[[0.0]] * 8] * 8))
            pawnAdded.append(numpy.array([[[0.0]] * 8] * 8))
    pawnMoved = numpy.array(pawnMoved)
    pawnAdded = numpy.array(pawnAdded)
    pawnMoved = numpy.concatenate(pawnMoved, 2)

    MovedPeices = numpy.concatenate((pawnMoved, numpy.array([[[0.0] * 6] * 8] * 8)), 2)
    if not sum(sum(sum(MovedPeices))) == 0:
        RemovedPeices = sum(pawnRemoved) / sum(sum(sum(MovedPeices)))
    else:
        RemovedPeices = sum(pawnRemoved) * 0
    pawnAdded = numpy.concatenate(pawnAdded, 2)
    AddedPeices = numpy.concatenate((pawnAdded, numpy.array([[[0.0] * 6] * 8] * 8)), 2)
    # print AddedPeices.shape
    if not sum(sum(sum(MovedPeices))) == 0:
        MovedPeices /= sum(sum(sum(MovedPeices)))

    if not sum(sum(sum(AddedPeices))) == 0:
        AddedPeices /= sum(sum(sum(AddedPeices)))

    return Same - MovedPeices + AddedPeices, Other - RemovedPeices


def getNewPawns(Same, Other, color, PawnNumber):
    MovedPeices = []
    RemovedPeices = []
    AddedPeices = []
    if color:

        movedSame = numpy.concatenate(([[0.0] * 8], Same[:-1, :, PawnNumber]), 0)
        takingSame = numpy.concatenate((movedSame[:, 1:], [[0.0]] * 8), 1) + \
                     numpy.concatenate(([[0.0]] * 8, movedSame[:, :-1]), 1)

        leftOther = numpy.concatenate((TensorFuntions.sumDimentions(2, 2, Other)[1:], [[0.0] * 8]), 0)
        leftSame = numpy.concatenate((TensorFuntions.sumDimentions(2, 2, Same)[1:], [[0.0] * 8]), 0)

        takingOther = numpy.concatenate((leftOther[:, 1:], [[0.0]] * 8), 1) + \
                      numpy.concatenate(([[0.0]] * 8, leftOther[:, :-1]), 1)
        # MovedPeices = Same[:, :, 0]
        # RemovedPeices = numpy.array(map(lambda num: Other[:, :, num] * takingSame, [0, 1, 2, 2, 4, 5])) #sum(Other) * takingSame
        # AddedPeices = TensorFuntions.sumDimentions(2,2, Other) * takingSame + \
        #               movedSame * (1 - TensorFuntions.sumDimentions(2,2,Same)) * (1 - TensorFuntions.sumDimentions(2,2, Other))
    else:

        movedSame = numpy.concatenate((Same[1:, :, PawnNumber], [[0.0] * 8]), 0)
        takingSame = numpy.concatenate((movedSame[:, 1:], [[0.0]] * 8), 1) + \
                     numpy.concatenate(([[0.0]] * 8, movedSame[:, :-1]), 1)

        leftOther = numpy.concatenate(([[0.0] * 8], TensorFuntions.sumDimentions(2, 2, Other)[:-1]), 0)
        leftSame = numpy.concatenate(([[0.0] * 8], TensorFuntions.sumDimentions(2, 2, Same)[:-1]), 0)
        takingOther = numpy.concatenate((leftOther[:, 1:], [[0.0]] * 8), 1) + \
                      numpy.concatenate(([[0.0]] * 8, leftOther[:, :-1]), 1)

    # print (1 - leftOther)
    # print (1 - leftSame)
    # print movedSame
    MovedPeices = Same[:, :, PawnNumber] * takingOther + Same[:, :, PawnNumber] * (1 - leftOther) * (1 - leftSame)

    RemovedPeices = numpy.array(
        map(map, [lambda a, b: a * b] * 8, takingSame, Other))  # sum(Other) * takingSame
    AddedPeices = TensorFuntions.sumDimentions(2, 2, Other) * takingSame + \
                  movedSame * (1 - TensorFuntions.sumDimentions(2, 2, Same)) * (
                      1 - TensorFuntions.sumDimentions(2, 2, Other))

    return MovedPeices, RemovedPeices, AddedPeices


def getOutArray(x, y, xprime, yprime, Same, Other, rookNumber):
    if abs(y - yprime) > 1:
        intheway = sum(Same[x, min(y, yprime) + 1:max(y, yprime), :])
        inthewayOther = sum(Other[x, min(y, yprime) + 1:max(y, yprime), :])

        return TensorFuntions.NegateSum(intheway) * TensorFuntions.NegateSum(inthewayOther) * Same[
            x, y, rookNumber] * TensorFuntions.NegateSum(Same[x, yprime, :])

    else:
        if abs(xprime - x) > 1:

            inthewayself = sum(Same[min(x, xprime) + 1:max(x, xprime), y])
            inthewayOther = sum(Other[min(x, xprime) + 1:max(x, xprime), y])

            return TensorFuntions.NegateSum(inthewayself) * TensorFuntions.NegateSum(inthewayOther) * Same[
                x, y, rookNumber] * TensorFuntions.NegateSum(Same[xprime, y])
        else:
            if abs(xprime - x) == 1:
                return Same[x, y, rookNumber] * TensorFuntions.NegateSum(Same[xprime, y, :])
            else:
                return Same[x, y, rookNumber] * TensorFuntions.NegateSum(Same[x, yprime, :])


def RookHelper(x, y, primeLoc, Same, Other, rookNumber, MovedPeices, AddedPeices, RemovedPeices):
    out = getOutArray(x, y, primeLoc[0], primeLoc[1], Same, Other, rookNumber)
    MovedPeices[x][y] += out
    AddedPeices[primeLoc[0]][primeLoc[1]] += out
    RemovedPeices[x][y] = map(lambda other: out * other, Other[primeLoc[0]][primeLoc[1]])


def getNewRooks(Same, Other, color, rookNumber):
    MovedPeices = map(lambda count: map(lambda count: 0.0, xrange(0, 8)), xrange(0, 8))
    RemovedPeices = map(lambda count: map(lambda count: map(lambda count: 0.0, xrange(0, 16)), xrange(0, 8)),
                        xrange(0, 8))
    AddedPeices = map(lambda count: map(lambda count: 0.0, xrange(0, 8)), xrange(0, 8))

    map(lambda x: map(
        lambda y: map(lambda primeLoc: RookHelper(x, y, primeLoc, Same, Other, rookNumber, MovedPeices, AddedPeices,
                                                  RemovedPeices),
                      map(lambda x, yprime: [x, yprime], [x] * 7,
                          filter(lambda yprime: y != yprime, [0, 1, 2, 3, 4, 5, 6, 7])) +
                      map(lambda y, xprime: [xprime, y], [y] * 7,
                          filter(lambda xprime: x != xprime, [0, 1, 2, 3, 4, 5, 6, 7]))), [0, 1, 2, 3, 4, 5, 6, 7]),
        [0, 1, 2, 3, 4, 5, 6, 7])

        # for yprime in range(0, len(Same[x])):
        #     if yprime != y:
        #         out = getOutArray(x, y, x, yprime, Same, Other, rookNumber)
        #         MovedPeices[x][y] += out
        #         AddedPeices[x][yprime] += out
        #         RemovedPeices[x][y] = map(lambda other: out * other, Other[x][yprime])
        #         # for i in range(0, 16):
        #         #     RemovedPeices[x][y][i] = out * Other[x][yprime][i]
        #
        # for xprime in range(0, len(Same)):
        #     if x != xprime:
        #         out = getOutArray(x, y, xprime, y, Same, Other, rookNumber)
        #         MovedPeices[x][y] += out
        #         AddedPeices[xprime][y] += out
        #         RemovedPeices[x][y] = map(lambda other: out * other, Other[xprime][y])

    return numpy.array(MovedPeices), numpy.array(RemovedPeices), numpy.array(AddedPeices)


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
    if COLOR:
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
    print "Pawns"
    print "\n".join(TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, b[:, :, :8]),
                                                      TensorFuntions.getMaxSizeRecursivly(
                                                          TensorFuntions.sumDimentions(2, 2, b[:, :, :8])))[1])
    print "Rooks"
    print "\n".join(TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, b[:, :, 8:10]),
                                                      TensorFuntions.getMaxSizeRecursivly(
                                                          TensorFuntions.sumDimentions(2, 2, b[:, :, 8:10])))[1])

    print sum(sum(sum(b)))


def printTurnStats(a, b, Color):
    if Color:
        print "--------------- White----------------------"
        printBoardStats(a)
        print "------------------Black------------------"
        printBoardStats(b)
    else:
        print "--------------- White----------------------"
        printBoardStats(b)
        print "------------------Black------------------"
        printBoardStats(a)
