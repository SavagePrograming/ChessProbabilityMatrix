# +++++++++++++++++++++++
# This is a  chess playing program
# created by savagewil,and Vigil
# started: fall 2013, finished: feb 2014 Reopened:jan 2015
# Adding web compatibility
# ++++++++++++++++++++++
import pygame
import Functions
import Square
import Board

# pygame for visuals,
# func for miscellaneous functions
# Functions for chess functions
# Square for Square class
# Board for Board class
# #-----------------------------------------------------------------
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Getting Game stats
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Initializing Pygame for visuals
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
pygame.init()
Screen = pygame.display.set_mode([450, 450])
Screen.fill([255, 255, 255])
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Creates the game board
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
MainBoard = Board.Board('pictures/chess2.jpg', [0, 0], 'b1')
intNumber = 0
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Making Squares
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
index1 = 0
index2 = 0
for chrLetter in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
    for intNumber1 in range(1, 9):
        lstLocation = [intNumber, (intNumber1 - 1)]
        s = Square.Square(0, lstLocation, chrLetter + str(intNumber1))
        MainBoard.array_square_Squares.append(s)
        MainBoard.multiarray_square_Board[index1][index2] = s
        index2 += 1
    index1 += 1
    index2 = 0
    intNumber += 1
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Setting squares up for starting positions
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

for square in MainBoard.array_square_Squares:
    if square.str_Name == 'a5':
        square.surface_Image = pygame.image.load('pictures/king.png')
        square.str_Image_Location = 'pictures/king.png'
        square.str_color = 'w'
        square.int_Rule_Num = 6
    # if square.str_Name == 'a4':
    #     square.surface_Image = pygame.image.load('pictures/queen.png')
    #     square.str_Image_Location = 'pictures/queen.png'
    #     square.str_color = 'w'
    #     square.int_Rule_Num = 5
    if square.str_Name == 'a3' or square.str_Name == 'a6':
        square.surface_Image = pygame.image.load('pictures/bishop.png')
        square.str_Image_Location = 'pictures/bishop.png'
        square.str_color = 'w'
        square.int_Rule_Num = 4
    # if square.str_Name == 'a7' or square.str_Name == 'a2':
    #     square.surface_Image = pygame.image.load('pictures/knight.png')
    #     square.str_Image_Location = 'pictures/knight.png'
    #     square.str_color = 'w'
    #     square.int_Rule_Num = 3
    # if square.str_Name == 'a1' or square.str_Name == 'a8':
    #     square.surface_Image = pygame.image.load('pictures/rook.png')
    #     square.str_Image_Location = 'pictures/rook.png'
    #     square.str_color = 'w'
    #     square.int_Rule_Num = 2
    # if square.str_Name.__contains__('b'):
    #     square.surface_Image = pygame.image.load('pictures/pawn.png')
    #     square.str_Image_Location = 'pictures/pawn.png'
    #     square.str_color = 'w'
    #     square.int_Rule_Num = 1
    if square.str_Name == 'h5':
        square.surface_Image = pygame.image.load('pictures/bking.png')
        square.str_Image_Location = 'pictures/bking.png'
        square.str_color = 'b'
        square.int_Rule_Num = 6
    # if square.str_Name == 'h4':
    #     square.surface_Image = pygame.image.load('pictures/bqueen.png')
    #     square.str_Image_Location = 'pictures/bqueen.png'
    #     square.str_color = 'b'
    #     square.int_Rule_Num = 5
    # if square.str_Name == 'h3' or square.str_Name == 'h6':
    #     square.surface_Image = pygame.image.load('pictures/bbishop.png')
    #     square.str_Image_Location = 'pictures/bbishop.png'
    #     square.str_color = 'b'
    #     square.int_Rule_Num = 4
    # if square.str_Name == 'h7' or square.str_Name == 'h2':
    #     square.surface_Image = pygame.image.load('pictures/bknight.png')
    #     square.str_Image_Location = 'pictures/bknight.png'
    #     square.str_color = 'b'
    #     square.int_Rule_Num = 3
    # if square.str_Name == 'h1' or square.str_Name == 'h8':
    #     square.surface_Image = pygame.image.load('pictures/brook.png')
    #     square.str_Image_Location = 'pictures/brook.png'
    #     square.str_color = 'b'
    #     square.int_Rule_Num = 2
    # if square.str_Name.__contains__('g'):
    #     square.surface_Image = pygame.image.load('pictures/bpawn.png')
    #     square.str_Image_Location = 'pictures/bpawn.png'
    #     square.str_color = 'b'
    #     square.int_Rule_Num = 1
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# sets up starting variables
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# print 'Is Player One an AI?'
# PlayerOneAI = raw_input().lower() == "t"
# if PlayerOneAI:
#     PlayerOne = Functions.setUpAI(MainBoard)
# else:
# PlayerOne = Functions.setUpHuman("White", MainBoard)

PlayerOne = Functions.setUpAI(MainBoard)
# print 'Is Player Two an AI?'
# PlayerTwoAI = raw_input().lower() == "t"
# if PlayerTwoAI:
#     PlayerTwo = Functions.setUpAI(MainBoard)
# else:
PlayerTwo = Functions.setUpAI(MainBoard)
# PlayerTwo = Functions.setUpHuman("White", MainBoard)

true = False
selected = False
turn = True  # White
win = 'yes'

# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Main game loop
# #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
while not true:
    # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Prints the board
    # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    MainBoard.show(Screen)
    # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Sorts squares
    # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    MainBoard.check()
    # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Runs the Ai if it is it's turn
    # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # if turn == strColorAI:
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #gets moves, (longest part)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     moves = Functions.check(MainBoard, MainBoard, strColorAI, intLevel, strColorAI, [0, 0],
    #                             bolFast, intLevel, Screen, bolFast)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Detects a stalemate
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     if not moves:
    #         true = True
    #         win = 'stalemate'
    #         break
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #clears king
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     king = 0
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #detects if its king is still alive
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     for i in MainBoard.array_square_Squares:
    #         if i.color == strColorAI:
    #             if i.rule_num == 6:
    #                 king = i
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #if it is not then it knows you won
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     if king == 0:
    #         true = True
    #         win = 'you win'
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Clears "your king"
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     yking = 0
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Detects if your king is still alive
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     for i in MainBoard.array_square_Squares:
    #         if not i.color == strColorAI:
    #             if i.rule_num == 6:
    #                 yking = i
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #if it is not then it knows it won
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     if yking == 0:
    #         true = True
    #         win = 'I win'
    #         #print 'm',func.length(moves)
    #
    #     # #        for move in moves:
    #     # #            #print move.min_
    #     # #            pass
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Creates List of moves to delet because king is in check
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     testl = []
    #     for move in moves:
    #         #print 'move',move.score
    #         if move.min_ == -1000:
    #             testl.append(moves.index(move))
    #     testl.sort()
    #     testl.reverse()
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #removes those moves
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     for z in testl:
    #         moves.__delitem__(z)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #If There are no moves left it calls it Check mate
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     if not moves:
    #         true = True
    #         win = 'Check mate\nYou win'
    #         break
    #         #for move in moves:
    #         #print move.av_
    #     #    pass
    #     #print 'm',func.length(moves)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Calculating best move
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Caluclating ranks of average
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     s_av = []
    #     for move in moves:
    #         t = False
    #         for move_s in s_av:
    #             if move_s.av < move.av:
    #                 s_av.insert(s_av.index(move_s), move)
    #                 t = True
    #                 break
    #         if not t:
    #             s_av.append(move)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #setting those ranks
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     for move in s_av:
    #         if move.av == s_av[(s_av.index(move) - 1)].av:
    #             move.s_avg = s_av[(s_av.index(move) - 1)].s_avg
    #         else:
    #             move.s_avg = s_av.index(move)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Calulating  ranks of minimum
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     s_min = []
    #     for move in moves:
    #         t = False
    #         for move_s in s_min:
    #             if move_s.min < move.min:
    #                 s_min.insert(s_min.index(move_s), move)
    #                 t = True
    #                 break
    #         if not t:
    #             s_min.append(move)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Setting ranks of minimum
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     for move in s_min:
    #         if move.min == s_min[(s_min.index(move) - 1)].min:
    #             move.s_min = s_min[(s_min.index(move) - 1)].s_min
    #         else:
    #             move.s_min = s_min.index(move)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Calulating ranks Of Maximum
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     s_max = []
    #     for move in moves:
    #         t = False
    #         for move_s in s_max:
    #             if move_s.max > move.max:
    #                 continue
    #             s_max.insert(s_max.index(move_s), move)
    #             t = True
    #             break
    #         if not t:
    #             s_max.append(move)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Setting ranks of maximum
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     for move in s_max:
    #         if move.max == s_max[(s_max.index(move) - 1)].max:
    #             move.s_max = s_max[(s_max.index(move) - 1)].s_max
    #         else:
    #             move.s_max = s_max.index(move)
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Calulating total rank
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     for move in moves:
    #         move.s_total = move.s_avg + (move.s_min * 2) + move.s_max
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Calulating best move
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     best1 = moves[0]
    #     for move in moves:
    #         if move.s_total < best1.s_total:
    #             best1 = move
    #             #print best1
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Prints info about all moves
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     for move in moves:
    #         move.PrintStats()
    #         print move.s_avg, move.s_min, move.s_max, move.s_total
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Prints info about the best move
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     print "Best"
    #     # #        print "Max:" + str(best1.max) ,"Min:" + str(best1.min) ,"Avg:" + str(best1.max) ,
    #     best1.PrintStats()
    #     print "Average Score:", best1.s_avg, "Minimum Score:", best1.s_min, "Maximum Score:",\
    #         best1.s_max, 'Total Score:', best1.s_total
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     #Moves the best move
    #     # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #     best1.MOVE(MainBoard)
    # #        best=moves[0]
    # #        for move in moves:
    # #            if move.min>best.min:
    # #                best=move
    # #            if not move.min==best.min:
    # #                test1=False
    # #        if test1:
    # #            best=random.choice(moves)
    # #        test2=True
    # #        best2=moves[0]
    # #        for move in moves:
    # #            if move.max>best2.max:
    # #                best2=move
    # #            if not move.max==best2.max:
    # #                test2=False
    # #        if test2:
    # #            best2=random.choice(moves)
    # #        if test2 and test1 and test:
    # #            best1.MOVE(board)
    # #        elif test2 and not test1 and test:
    # #            best1.MOVE(board)
    # #        elif test and not test2 and test1:
    # #            best2.MOVE(board)
    # #        elif not test and test2 and test1:
    # #            best.MOVE(board)
    # #        elif not test and not test1 and test2:
    # #            bests=[]
    # #            for move in moves:
    # #                if move.av<best1.av and move.av>test.av:
    # #                    bests.append(move)
    # #            if func.length(bests)==0:
    # #                bests[0].MOVE(board)
    # #            else:
    # #                Best=bests[0]
    # #                for move in bests:
    # #                    if move.av>=Best.av and move.min>=Best.av:
    # #                        Best=move
    # #
    # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Change turns
    # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # if turn == 'w':
    #     turn = 'b'
    # elif turn == 'b':
    #     turn = 'w'

    if turn:
        turn = PlayerOne.runTurn(turn)
        if not turn:
            print "Black's Turn"
    else:
        turn = PlayerTwo.runTurn(turn)
        if turn:
            print "White's Turn"
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Event handler
    # #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Events = pygame.event.get()
    if turn:
        turn = PlayerOne.handleEvents(Events, turn)
    else:
        turn = PlayerTwo.handleEvents(Events, turn)

print win
print 'Done?'
done = raw_input()
while done == 'done':
    done = raw_input()
blah = True
if blah:
    pass

pygame.quit()
