import numpy, ChessMatrixFunctions, TensorFuntions
screen = ChessMatrixFunctions.makeScreen()
a, b = ChessMatrixFunctions.MakeStartBoards()

# a[1][0][0] = 0.0
# a[2][0][0] = 1.0


# print a
# print b
#
# print "\n".join(TensorFuntions.printRecusivlySize(a, 3)[1])
# print
# c = numpy.concatenate(([[[0.0]*6] * 8], a[:-1]), 0)

# a = numpy.array([[[1, 2, 3], [1, 2, 3]],
#      [[3, 2, 1], [3, 2, 1]]])
# print TensorFuntions.sumDimentions(2,2,a)

IN = 26
delay = 0
rate = 4
print rate

COLOR = True
count = 0

COLOR = not COLOR
BestSum = None
BestIndex = 0
# b[6][4][0] = 0.0
# b[3][4][0] = 1.0
for i in range(0, 8):

    a_ = numpy.array(a)
    a_[1][i][0] = 0.0
    a_[2][i][0] = 1.0
    a_, b_ =  b, a_
    # if COLOR:
    #     print "--------------- White----------------------"
    #     print "\n".join(
    #         TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, a_[:, :, :8]), TensorFuntions.getMaxSizeRecursivly(TensorFuntions.sumDimentions(2, 2, a_[:, :, :8])))[1])
    #     print sum(sum(sum(a_)))
    #     print "------------------Black------------------"
    #     print "\n".join(
    #         TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, b_[:, :, :8]), TensorFuntions.getMaxSizeRecursivly(TensorFuntions.sumDimentions(2, 2, b_[:, :, :8])))[1])
    #     print sum(sum(sum(b_)))
    # else:
    #     print "--------------- White----------------------"
    #     print "\n".join(
    #         TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, b_[:, :, :8]), TensorFuntions.getMaxSizeRecursivly(TensorFuntions.sumDimentions(2, 2, b_[:, :, :8])))[1])
    #     print sum(sum(sum(b_)))
    #     print "------------------Black------------------"
    #     print "\n".join(
    #         TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, a_[:, :, :8]), TensorFuntions.getMaxSizeRecursivly(TensorFuntions.sumDimentions(2, 2, a_[:, :, :8])))[1])
    #     print sum(sum(sum(a_)))
    out1, out2, outCOLOR = ChessMatrixFunctions.goNGenerationsVisual( a_, b_, COLOR, IN, delay, screen, rate)
    if outCOLOR:
        print "--------------- White----------------------"
        print "\n".join(
            TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, out1[:, :, :8]), TensorFuntions.getMaxSizeRecursivly(TensorFuntions.sumDimentions(2, 2, out1[:, :, :8])))[1])
        o1 = [ChessMatrixFunctions.peices, sum(sum(out1))]
        print "\n".join(TensorFuntions.printRecusivlySize(o1, TensorFuntions.getMaxSizeRecursivly(o1))[1])
        print "Total:",sum(sum(sum(out1)))
        print "------------------Black------------------"
        print "\n".join(
            TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, out2[:, :, :8]), TensorFuntions.getMaxSizeRecursivly(TensorFuntions.sumDimentions(2, 2, out2[:, :, :8])))[1])

        o2 = [ChessMatrixFunctions.peices, sum(sum(out2))]
        print "\n".join(TensorFuntions.printRecusivlySize(o2, TensorFuntions.getMaxSizeRecursivly(o2))[1])
        print "Total:", sum(sum(sum(out2)))

        if BestSum is None:
            BestSum = sum(sum(sum(out1))) - sum(sum(sum(out2)))
            BestIndex = i
        elif sum(sum(sum(out1))) - sum(sum(sum(out2)))> BestSum:
            BestSum = sum(sum(sum(out1))) - sum(sum(sum(out2)))
            BestIndex = i
    else:
        print "--------------- White----------------------"
        print "\n".join(
            TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, out2[:, :, :8]), TensorFuntions.getMaxSizeRecursivly(TensorFuntions.sumDimentions(2, 2, out2[:, :, :8])))[1])
        # print sum(sum(out2))
        o2 = [ChessMatrixFunctions.peices, sum(sum(out2))]
        print "\n".join(TensorFuntions.printRecusivlySize(o2, TensorFuntions.getMaxSizeRecursivly(o2))[1])
        print "Total:", sum(sum(sum(out2)))
        print "------------------Black------------------"
        print "\n".join(
            TensorFuntions.printRecusivlySize(TensorFuntions.sumDimentions(2, 2, out1[:, :, :8]), TensorFuntions.getMaxSizeRecursivly(TensorFuntions.sumDimentions(2, 2, out1[:, :, :8])))[1])
        # print sum(sum(out1))
        o1 = [ChessMatrixFunctions.peices, sum(sum(out1))]
        print "\n".join(TensorFuntions.printRecusivlySize(o1, TensorFuntions.getMaxSizeRecursivly(o1))[1])
        print "Total:", sum(sum(sum(out1)))
        if BestSum is None:
            BestSum = sum(sum(sum(out2))) - sum(sum(sum(out1)))
            BestIndex = i
        elif sum(sum(sum(out2))) - sum(sum(sum(out1))) > BestSum:
            BestSum = sum(sum(sum(out2))) - sum(sum(sum(out1)))
            BestIndex = i

print "BEST SUM: " + str(BestSum)
print "BEST MOVE: Pawn at 1, " + str(i)