import pygame
import sys

import Functions


class Player:
    def __init__(self, board):
        self.board = board

    def runTurn(self, Color):
        return Color

    def handleEvents(self, Events, turn):
        for event in Events:
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # A key is pressed
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if event.type == pygame.KEYDOWN:
                ##            if event.key==pygame.K_b:
                ##                for sq in board.sq:
                ##                    if sq.rule_num==5:
                ##                        sq.self_create(board)
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # If that key is 'x'
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_x:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Deselect the selected piece
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.board.selected = False
                    for square in self.board.array_square_Squares:
                        square.selected = False
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # If the key is 's' saves the board
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_s:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Save to inputed location
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print "What File:"
                    FileLoc = raw_input()
                    File = open(FileLoc, 'w')
                    SquareString = self.board.ToString()
                    File.write(SquareString)
                    File.write('\n' + turn)
                    File.close()
                    print "Done"
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # If the key is o loads a save
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_o:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Load a save from inputed location
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print "What File:"
                    FileLoc = raw_input()
                    File = open(FileLoc, 'r')
                    SquareString = File.readline()
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Loads Board from string
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    self.board.FromString(SquareString)
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Sets the turn to saved turn
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    turn = File.readline() == "True"
                    print "Done"
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # if / pressed creates a new piece
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_SLASH:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Gets data
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print '>Where'
                    loc = raw_input('>')
                    print '>What peice'
                    Type = raw_input('>')
                    print '>What color'
                    color = raw_input('>')
                    print '>What number'
                    intNumber2 = int(raw_input('>'))
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Creates piece
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    Functions.create(self.board, loc, color, Type, intNumber2)
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # If exit was hit then stop
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if event.type == pygame.QUIT:
                sys.exit(0)
        return turn