import pygame

import Functions
from Player import Player


class PlayerHumanGui(Player):
    def __init__(self, name, board):
        Player.__init__(self, board)
        self.name = name

    # def runTurn(self, Color):
    #     # print self.name + "'s Turn"
    #     # if Color:
    #     #     print "Color is White"
    #     # else:
    #     #     print "Color is Black"
    #     return Color

    def handleEvents(self, Events, turn):
        turn = Player.handleEvents(self, Events, turn)
        for event in Events:
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # A key is pressed
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if event.type == pygame.KEYDOWN:
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # if space pressed moves a piece
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if event.key == pygame.K_SPACE:
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Gets input
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    print '>From where'
                    From = raw_input('>')
                    print '>To where'
                    To = raw_input('>')
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Moves piece
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    Functions.move_(self.board, From, To)
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Prints piece moved
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if turn:
                        print 'White:', From, ">", To
                    else:
                        print 'Black:', From, ">", To

                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Changes turn
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    turn = not turn
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # If the mouse is pressed
            ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = 'a'
                y = 0
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # if a piece has already been selected
                ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                if Functions.hasSelected(self.board):
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Sets variables to location of mouse
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    mousex, mousey = event.pos
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # Determins squares name based on location
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if mousex < 50:
                        x = 'a'
                    elif mousex < 100:
                        x = 'b'
                    elif mousex < 150:
                        x = 'c'
                    elif mousex < 200:
                        x = 'd'
                    elif mousex < 250:
                        x = 'e'
                    elif mousex < 300:
                        x = 'f'
                    elif mousex < 350:
                        x = 'g'
                    elif mousex < 400:
                        x = 'h'
                    y = int(mousey / 50) + 1
                    name2 = x + str(y)

                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #
                    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if not Functions.hasSelected(self.board) == name2:
                        name1 = Functions.getSelected(self.board).str_Name
                        Functions.move_(self.board, name1, name2)
                        if turn:
                            print 'White:', name1, ">", name2
                        else:
                            print 'Black:', name1, ">", name2
                        for sq in self.board.array_square_Squares:
                            if sq.bol_Selected:
                                sq.bol_Selected = False
                        turn = not turn
                        continue
                    else:
                        for sq in self.board.array_square_Squares:
                            if sq.bol_Selected:
                                sq.bol_Selected = False
                else:
                    mousex, mousey = event.pos
                    if mousex < 50:
                        x = 'a'
                    elif mousex < 100:
                        x = 'b'
                    elif mousex < 150:
                        x = 'c'
                    elif mousex < 200:
                        x = 'd'
                    elif mousex < 250:
                        x = 'e'
                    elif mousex < 300:
                        x = 'f'
                    elif mousex < 350:
                        x = 'g'
                    elif mousex < 400:
                        x = 'h'
                    y = int(mousey / 50) + 1
                    name1 = x + str(y)
                    for sq in self.board.array_square_Squares:
                        if sq.str_Name == name1:
                            sq.bol_Selected = True
        return turn