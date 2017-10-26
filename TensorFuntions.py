import numpy, math
def join(a,b, indent):
    return a + indent + b

def distance(x1, y1, x2, y2):
    return ((x1- x2) ** 2. + (y1-y2)**2.) ** .5

def printRecusivly(Array):
    if len(Array) > 0:
        if isinstance(Array[0], list) or isinstance(Array[0], numpy.ndarray):
            depth = []
            strings = []
            depth, strings = map(printRecusivly, Array)
            depth = max(depth) + 1
            if depth % 2 == 0:
                string = reduce(lambda joined, current: map(join, joined, current, ["  " * depth + "|"] * len(joined)), strings)
            else:
                string = reduce(lambda joined, current: joined + [""] * depth + ["_" * joined] + current, strings)

            return depth, string
        else:
            depth = 0
            string = map(str, Array)
            return depth, string


def stringofLength(string, num):
    string = str(string)
    if len(string) == num:
        return string
    elif len(string) > num:
        return string[:num]
    else:
        return string + " " * (num - len(string))


def getMaxrecursivly(Array):
    if len(Array) > 0:
        if isinstance(Array[0], list) or isinstance(Array[0], numpy.ndarray):
            return max(map(getMaxrecursivly, Array))
        else:
            return max(Array)


def getMaxSizeRecursivly(Array):
    if len(Array) > 0:
        if isinstance(Array[0], list) or isinstance(Array[0], numpy.ndarray):
            return max(map(getMaxSizeRecursivly, Array))
        else:
            # print Array
            return reduce(lambda MAX, stuff: max(MAX, len(str(stuff))), Array, 0)
    return 0


def printRecusivlySize(Array, maxStringSize):
    if len(Array) > 0:
        if isinstance(Array[0], list) or isinstance(Array[0], numpy.ndarray):
            depth = []
            strings = []
            # depth, strings = map(printRecusivlySize, Array, [maxStringSize] * len(Array))
            for sub in Array:
                d, s = printRecusivlySize(sub, maxStringSize)
                depth.append(d)
                strings.append(s)
            depth = max(depth) + 1
            if depth % 2 == 0:
                string = reduce(lambda joined, current: joined + [" " * maxStringSize] * depth + current, strings)
            else:
                string = reduce(lambda joined, current: map(join, joined, current, ["  " * depth] * len(joined)),
                                strings)

            return depth, string
        else:
            depth = 0

            string = map(stringofLength, Array, [maxStringSize] * len(Array))
            return depth, string

def multiplyOnto(Tensor1, Tensor2):
    if len(Tensor1) > 0:
        if isinstance(Tensor1[0], list) or isinstance(Tensor1[0], numpy.ndarray):

            return numpy.array(map(multiplyOntoinside, Tensor1, [Tensor2] * len(Tensor1)))
        else:
            return numpy.array(map(lambda scalar, tensor: scalar * tensor, Tensor1, [Tensor2] * len(Tensor1)))

def multiplyOntoinside(Tensor1, Tensor2):
    if len(Tensor1) > 0:
        if isinstance(Tensor1[0], list) or isinstance(Tensor1[0], numpy.ndarray):
            return map(multiplyOntoinside, Tensor1, [Tensor2] * len(Tensor1))
        else:
            return map(lambda scalar, tensor: scalar * tensor, Tensor1, [Tensor2] * len(Tensor1))

def sumDimentions(start, end, Tensor):
    if start > 0:
        return numpy.array(map(sumDimentionsInside, [start - 1] * len(Tensor), [end - 1] * len(Tensor), Tensor))
    elif end >= 0:
        return numpy.array(reduce(lambda t1, t2: t1 + t2, map(sumDimentionsInside, [start - 1] * len(Tensor), [end - 1] * len(Tensor), Tensor)))
    else:

        return Tensor


def sumDimentionsInside(start, end, Tensor):
    if start > 0:
        # print "s"
        return map(sumDimentionsInside, [start - 1] * len(Tensor), [end - 1] * len(Tensor), Tensor)
    elif end >= 0:
        # print "r"
        # print  map(sumDimentionsInside, [start - 1] * len(Tensor), [end - 1] * len(Tensor), Tensor)
        # print reduce(lambda t1, t2: t1 + t2, map(sumDimentionsInside, [start - 1] * len(Tensor), [end - 1] * len(Tensor), Tensor))
        return reduce(lambda t1, t2: t1 + t2, map(sumDimentionsInside, [start - 1] * len(Tensor), [end - 1] * len(Tensor), Tensor))
    else:
        # print "e", Tensor
        return Tensor