# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:07:03 2017

@author: Mohanakrishna
"""

import sys
import MorrisGameBoard

maxValue = sys.maxsize
minValue = -sys.maxsize
depth = int(sys.argv[3])
boardState = list()

#Reading board input state
def readBoardState():
    #print("Reading board state")
    board1 = open(sys.argv[1],"r")
    board = list()
    for line in board1:
        for ch in line:
            board.append(ch)
    return board

#Writing board output state
def writeBoardState(outBoardState):
    board2 = open(sys.argv[2],"w")
    for each in outBoardState:
        board2.write(each)
    board2.close()

#Static estimate at the Opening position - White
def staticEstimateOpening(boardSt):
    wcount = 0
    bcount = 0
    staticEstimate = 0
    for posi in range(0,len(boardSt)):
        if(boardSt[posi]=='W'):
            wcount= wcount+1

        elif(boardSt[posi]=='B'):
            bcount = bcount+1

    staticEstimate = wcount-bcount 
    return staticEstimate

def ABGame(d,board,alpha,beta,flag):
    inp = MorrisGameBoard.outputClass()
    out = MorrisGameBoard.outputClass()
    
    if(d==0):
        wcount = 0
        bcount = 0
        finalCount = 0
        for position in range(0,len(board)):
            if(board[position]=="W"):
                wcount = wcount+1
            if(board[position]=="B"):
                bcount = bcount+1
        finalCount = wcount-bcount
        l = MorrisGameBoard.generateMovesMidgameEndgameBlack(board)
        listsize = len(l)
        if(bcount<=2):
            out.value = 10000
        elif(wcount<=2):
            out.value = -10000
        elif(listsize==0):
            out.value = 10000
        else:
            out.value = 1000*(finalCount)-listsize
        out.count = out.count+1
        out.boardState = board 
        return out
    
    listofMoves = list()
    if(flag==1):    
        listofMoves = MorrisGameBoard.generateMovesMidgameEndgame(board)
        
    else:
        listofMoves = MorrisGameBoard.generateMovesMidgameEndgameBlack(board)
            
    for b in listofMoves:
        if(flag==1):
            inp = ABGame(d-1,b,alpha,beta,0)
            if(inp.value> alpha):
                alpha = inp.value
                out.boardState = b
            out.count = out.count + inp.count
        else:
            inp = ABGame(d-1,b,alpha,beta,1)
            if(inp.value< beta):
                beta = inp.value
                out.boardState = b
            out.count = out.count + inp.count
        if(alpha>=beta):
            break
        
    if (flag==1):
        out.value = alpha
    else:
        out.value = beta
    return out

board = readBoardState()
out = ABGame(depth,board,minValue,maxValue,1)
print("Board Position:",''.join(out.boardState))
print("Positions evaluated by static estimation:",out.count)
print("AB estimate:",out.value)
writeBoardState(out.boardState)