import numpy, TensorFuntions, pygame

board = pygame.image.load('pictures/chess2.jpg')
imagelocwhite = ['pictures/pawn.png', 'pictures/rook.png', 'pictures/knight.png',
                 'pictures/bishup.png', 'pictures/queen.png', 'pictures/king.png']
imagelocblack = ['pictures/bpawn.png', 'pictures/brook.png', 'pictures/bknight.png',
                 'pictures/bbishup.png', 'pictures/bqueen.png', 'pictures/bking.png']

imagesWhite = map(pygame.image.load, imagelocwhite)
imagesBlack = map(pygame.image.load, imagelocblack)

peices = ["Pawn","Pawn","Pawn","Pawn","Pawn","Pawn","Pawn","Pawn","Rook","Rook","Knight","Knight","Bishop","Bishop","Queen","King"]
def MakeStartBoards():
    """
    Matrix Format
            Second index
          0 1 2 3 4 5 6 7
    F   0 X O X O X O X O
    i   1 O X O X O X O X
    r   2 X O X O X O X O
    s   3 O X O X O X O X
    t   4 X O X O X O X O
        5 O X O X O X O X
        6 X O X O X O X O
        7 O X O X O X O X

    then each Square has
    [Pawn,Pawn,Pawn,Pawn,Pawn,Pawn,Pawn,Pawn,Rook,Rook,Knight,Knight,Bishop,Bishop,Queen,King]

    P = Pawn
    R = Rook
    N = Knight
    B = Bishop
    Q = Queen
    K = King

    Initial Setup


      0 1 2 3 4 5 6 7
    0 R N B K Q B N R
    1 P P P P P P P P
    2 X O X O X O X O
    3 O X O X O X O X
    4 X O X O X O X O
    5 O X O X O X O X
    6 P P P P P P P P
    7 R N B K Q B N R


    :return:
    """

    return numpy.array([[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]]), \
           numpy.array([[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],

                        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]])


def MakeNextBoards(Same, Other, color):
    """

    :param Same: Tensor for current player
    :param Other: Tensor for other player
    :param color: True is white, False is black
    :return:
    """
    pawnMoved, pawnRemoved, pawnAdded =[],[],[]
    for i in range(0,8):
        pawnMoved_, pawnRemoved_, pawnAdded_ = getNewPawns(Same, Other, color, i)
        pawnMoved.append(numpy.reshape(pawnMoved_, (8,8,1)))
        pawnRemoved.append(pawnRemoved_)
        pawnAdded.append(numpy.reshape(pawnAdded_, (8,8,1)))
    # pawnMoved = numpy.array(pawnMoved)
    # pawnAdded = numpy.array(pawnAdded)

    # print pawnMoved
    # print Same[:, :, 0]
    # print (numpy.concatenate(pawnMoved, 2))[:, :, 0]
    pawnMoved = numpy.concatenate(pawnMoved, 2)

    MovedPeices = numpy.concatenate((pawnMoved, numpy.array([[[0.0] * 8] * 8] * 8)), 2)
    # print " =================================== "
    # print "\n".join(TensorFuntions.printRecusivlySize(MovedPeices, 5)[1])
    # # print "\n".join(TensorFuntions.printRecusivlySize(MovedPeices[:,:,0], 5)[1])
    # print sum(sum(MovedPeices[:, :, 0]))
    RemovedPeices = sum(pawnRemoved) / sum(sum(sum(MovedPeices)))
    pawnAdded = numpy.concatenate(pawnAdded, 2)
    AddedPeices = numpy.concatenate((pawnAdded, numpy.array([[[0.0] * 8] * 8] * 8)), 2)
    # print AddedPeices.shape
    MovedPeices /= sum(sum(sum(MovedPeices)))
    AddedPeices /= sum(sum(sum(AddedPeices)))
    # AddedPeices *= 8. - sum(sum((Same * (1 - MovedPeices))[:, :, 0]))
    # AddedPeices *= sum(sum(sum((1 - Same * (MovedPeices)))))
    # print " =================================== "
    # print "\n".join(TensorFuntions.printRecusivlySize(MovedPeices[:, :, 0], 5)[1])
    # print sum(sum(MovedPeices[:, :, 0]))
    # print " =================================== "
    # print "\n".join(TensorFuntions.printRecusivlySize(RemovedPeices[:, :, 0], 3)[1])
    # print sum(sum(RemovedPeices[:, :, 0]))
    # print " =================================== "
    # print "\n".join(TensorFuntions.printRecusivlySize(AddedPeices[:,:,0], 5)[1])
    # print sum(sum(AddedPeices[:, :, 0]))
    # print " =================================== "
    # print "\n".join(TensorFuntions.printRecusivlySize((Same * (1 - MovedPeices))[:, :, 0], 5)[1])
    # print sum(sum((Same * (1 - MovedPeices))[:, :, 0]))
    # print " =================================== "
    # print (Same * (1 - MovedPeices)).sh

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
        # RemovedPeices = numpy.array(map(lambda num: Other[:, :, num] * takingSame, [0, 1, 2, 3, 4, 5])) #sum(Other) * takingSame
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

# def getNewRooks(Same, Other, color, rookNumber):
#     MovedPeices = []
#     RemovedPeices = []
#     AddedPeices = [[[1.0] * 8]*8]
#     movedForward = map(lambda num: numpy.concatenate(([[0.0] * 8] * num, Same[:-num, :, rookNumber]), 0), xrange(1, 7))
#     movedBack = map(lambda num: numpy.concatenate((Same[num:, :, rookNumber], [[0.0] * 8] * num), 0), xrange(1, 7))
#     InwayForward = []
#     for f in range(2,8):
#         InwayForward.append([])
#         for x in range(0,8):
#             InwayForward[f-1].append([])
#
#             for y in range(0,8):
#                 InwayForward[f-1][x]
#                 for jump in range(1,f)
#                     InwayForward[f - 1][x]
#
#     InwayForward = map(lambda num: numpy.concatenate((Same[num:], [[0.0] * 8] * num), 0), xrange(1, 7))
#     movedSame = numpy.concatenate(([[0.0] * 8], Same[:-1, :, rookNumber]), 0)
#     takingSame = numpy.concatenate((movedSame[:, 1:], [[0.0]] * 8), 1) + \
#                  numpy.concatenate(([[0.0]] * 8, movedSame[:, :-1]), 1)
#
#     leftOther = numpy.concatenate((TensorFuntions.sumDimentions(2, 2, Other)[1:], [[0.0] * 8]), 0)
#     leftSame = numpy.concatenate((TensorFuntions.sumDimentions(2, 2, Same)[1:], [[0.0] * 8]), 0)
#
#     takingOther = numpy.concatenate((leftOther[:, 1:], [[0.0]] * 8), 1) + \
#                  numpy.concatenate(([[0.0]] * 8, leftOther[:, :-1]), 1)
#
#     MovedPeices = Same[:, :, rookNumber] * takingOther + Same[:, :, rookNumber] * (1 - leftOther) * (1 - leftSame)
#
#
#     RemovedPeices = numpy.array(
#         map(map, [lambda a, b: a * b] * 8, takingSame, Other))  # sum(Other) * takingSame
#     AddedPeices = TensorFuntions.sumDimentions(2, 2, Other) * takingSame + \
#                   movedSame * (1 - TensorFuntions.sumDimentions(2, 2, Same)) * (
#                       1 - TensorFuntions.sumDimentions(2, 2, Other))
#
#     return MovedPeices, RemovedPeices, AddedPeices

def goNGenerations(a, b, COLOR, N):
    count = 1
    while N > count:
        count += 1
        b, a = MakeNextBoards(a, b, COLOR)
        COLOR = not COLOR
    return a, b, COLOR


def goNGenerationsVisual(a, b, COLOR, N, delay, Screen, rate):
    count = 1
    while N > count:
        count += 1
        b, a = MakeNextBoards(a, b, COLOR)

        if count % rate == 0:
            if delay != 0:
                pygame.time.delay(delay)
            # if COLOR:
            #     print "--------------- White----------------------"
            #     print "\n".join(
            #         TensorFuntions.printRecusivlySize(a[:, :, 0],
            #                                           TensorFuntions.getMaxSizeRecursivly(a[:, :, 0]))[1])
            #     print sum(sum(sum(a)))
            #     print "------------------Black------------------"
            #     print "\n".join(
            #         TensorFuntions.printRecusivlySize(b[:, :, 0],
            #                                           TensorFuntions.getMaxSizeRecursivly(b[:, :, 0]))[1])
            #     print sum(sum(sum(b)))
            # else:
            #     print "--------------- White----------------------"
            #     print "\n".join(
            #         TensorFuntions.printRecusivlySize(b[:, :, 0],
            #                                           TensorFuntions.getMaxSizeRecursivly(b[:, :, 0]))[1])
            #     print sum(sum(sum(b)))
            #     print "------------------Black------------------"
            #     print "\n".join(
            #         TensorFuntions.printRecusivlySize(a[:, :, 0],
            #                                           TensorFuntions.getMaxSizeRecursivly(a[:, :, 0]))[1])
            #     print sum(sum(sum(a)))
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
    #     [[[0, 1, 2, 3, 4, 5]] * 8] * 8, Same, [[[COLOR] * 6] * 8] * 8, [[[Screen] * 6] * 8] * 8)
    #
    # map(map, [map] * 8, [[map] * 8] * 8, [[[drawSquare] * 6] * 8] * 8,
    #     [[[0] * 6] * 8, [[1] * 6] * 8, [[2] * 6] * 8, [[3] * 6] * 8, [[4] * 6] * 8, [[5] * 6] * 8, [[6] * 6] * 8,
    #      [[7] * 6] * 8],
    #     [[[0] * 6, [1] * 6, [2] * 6, [3] * 6, [4] * 6, [5] * 6, [6] * 6, [7] * 6]] * 8,
    #     [[[0, 1, 2, 3, 4, 5]] * 8] * 8, Other, [[[not COLOR] * 6] * 8] * 8, [[[Screen] * 6] * 8] * 8)


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
