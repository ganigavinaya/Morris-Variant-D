# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:00:28 2017

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

def ABOpening(d,board,alpha,beta,flag):
    inp = MorrisGameBoard.outputClass()
    out = MorrisGameBoard.outputClass()
    boardPositionList = list()
    finalCount = 0
    if(d==0):
        finalCount = staticEstimateOpening(board)
        out.value = finalCount
        out.count = out.count +1
        return out
    
    if(flag==1):
        boardPositionList = MorrisGameBoard.generateMoveOpening(board)

    else:
        boardPositionList = MorrisGameBoard.generateMoveOpeningBlack(board)
       
    for bposition in boardPositionList:
        if(flag==1):
            inp = ABOpening(d-1,bposition,alpha,beta, 0)
            if (inp.value > alpha):
                alpha = inp.value
                out.boardState = bposition
            out.count = out.count + inp.count
        else:
             inp = ABOpening(d-1,bposition,alpha,beta, 1)
             if (inp.value < beta):
                beta = inp.value
                out.boardState = bposition
             out.count = out.count + inp.count
        if(alpha>=beta):
            break
    if (flag==1):
        out.value =alpha
    else:
        out.value = beta
    return out

   
board = readBoardState()
out = ABOpening(depth,board,minValue,maxValue,1)

print("Board Position:",''.join(out.boardState))
print("Positions evaluated by static estimation:",out.count)
print("AB Estimate:",out.value)
writeBoardState(out.boardState)
