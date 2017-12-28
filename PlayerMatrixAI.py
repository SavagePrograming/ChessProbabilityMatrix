import random

import numpy

import Functions
import TensorFuntions
from Player import Player
import ChessMatrixFunctions


class PlayerMatrixAI(Player):
    def __init__(self, board, number):
        Player.__init__(self, board)
        self.number = number

    def runTurn(self, Color):
        White, Black = self.board.makeTenors()


        Moves = []
        # print "Starting Moves "
        if Color:
            ChessMatrixFunctions.addMovesWhite(White, Black, Color, Moves, self.number)
        else:
            ChessMatrixFunctions.addMovesBlack(White, Black, Color, Moves, self.number)

        Best = [Moves[0]]
        BestScore = Moves[0][4]
        for move in Moves:
            print move
            if BestScore < move[4]:
                BestScore = move[4]
                Best = [move]
            elif BestScore == move[4]:
                Best.append(move)
        Best = Best[random.randint(0, len(Best) - 1)]
        Functions.move_(self.board, self.board.multiarray_square_Board[Best[0]][Best[1]].str_Name,
                        self.board.multiarray_square_Board[Best[2]][Best[3]].str_Name)
        print "Best",Best
        return not Color
