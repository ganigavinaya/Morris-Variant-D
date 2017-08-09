# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 00:02:39 2017

@author: Mohanakrishna
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:33:11 2017

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
    board1.close()
    return board

#Writing board output state
def writeBoardState(outBoardState):
    board2 = open(sys.argv[2],"w")
    for each in outBoardState:
        board2.write(each)
    board2.close()

#Static estimate at the Opening position - White
def staticEstimateOpeningImproved(boardSt):
    wcount = 0
    bcount = 0
    mills = 0
    diff = 0
    staticEstimate = 0
    for posi in range(0,len(boardSt)):
        if(boardSt[posi]=='W'):
            wcount= wcount+1
        
        elif(boardSt[posi]=='B'):
            bcount = bcount+1

    diff = wcount-bcount 
    for each in range(0,len(boardSt)):
        if(boardSt[each]=='x'):
            if(MorrisGameBoard.checkMills(each,boardSt,"W")==True):
                mills = mills+1
    staticEstimate = mills+diff
    return staticEstimate

#Improved MiniMaxOpening   
def MiniMaxImproved(d,gameBoard,flag):
#   print('Min Max call')
    out = MorrisGameBoard.outputClass()
    inp = MorrisGameBoard.outputClass()
    boardList = list()
    if(d==0):
        finalCount = staticEstimateOpeningImproved(gameBoard)
        out = MorrisGameBoard.outputClass(finalCount,out.count+1,gameBoard)
        return out
    
    if(flag==1):
        boardList = MorrisGameBoard.generateMoveOpening(gameBoard)
        out.value = minValue
    
    else:
        boardList = MorrisGameBoard.generateMoveOpeningBlack(gameBoard)
        out.value = maxValue
        
    for bposition in boardList:
        if(flag==1):
            inp = MiniMaxImproved(d-1,bposition,0)
            if(inp.value>out.value):
                out.value=inp.value
                out.boardState = bposition
            out.count = out.count + inp.count
            
        else:
            inp = MiniMaxImproved(d-1,bposition,1)
            if(inp.value<out.value):
                out.value=inp.value
                out.boardState = bposition
            out.count = out.count + inp.count
            
    return out
            
board = readBoardState()  
out = MiniMaxImproved(depth,board,1)
print("Board Position:", ''.join(out.boardState))
print("Position evaluated by static estimation:",out.count)
print("MINIMAX esitmate:",out.value)
writeBoardState(out.boardState)
  