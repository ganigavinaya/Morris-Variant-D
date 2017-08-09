# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:28:51 2017

@author: Mohanakrishna
"""

import sys
import MorrisGameBoard

maxValue = sys.maxsize
minValue = -sys.maxsize
depth = int(sys.argv[3])
boardState = list()

def readBoardState():
    #print("Reading board state")
    board3 = open(sys.argv[1],"r")
    board = list()
    for line in board3:
        for ch in line:
            board.append(ch)
    board3.close()
    return board

def writeBoardState(outBoardState):
    board4 = open(sys.argv[2],"w")
    for each in outBoardState:
        board4.write(each)
    board4.close()
    
def MiniMaxGameBlack(d,gameBoard,flag):
#   print('Min Max call')
    out = MorrisGameBoard.outputClass()
    inp = MorrisGameBoard.outputClass()
    boardList = list()
    if(d==0):
        wcount = 0
        bcount = 0
        for pos in range(0,len(gameBoard)):
            if(gameBoard[pos]=='W'):
                wcount+=1
            elif(gameBoard[pos]=='B'):
                bcount+=1
                
        finalCount = bcount-wcount
        l = MorrisGameBoard.generateMovesMidgameEndgame(gameBoard)
        l_size = len(l)
        if(bcount<=2):
            out.value = 10000
        elif(wcount<=2):
            out.value = -10000
        elif(l_size==0):
            out.value = 10000
        else:
            out.value = 1000*(finalCount) - l_size
        out.count +=1
        return out
    
    if(flag==1):
#        print("Flag1")
        boardList = MorrisGameBoard.generateMovesMidgameEndgameBlack(gameBoard)
        #print(boardList)
        out.value = minValue
    else:
        boardList = MorrisGameBoard.generateMovesMidgameEndgame(gameBoard)
        out.value = maxValue
        
    for bposition in boardList:
        if(flag==1):
            inp = MiniMaxGameBlack(d-1,bposition,0)
            if(inp.value>out.value):
                out.value=inp.value
                out.boardState = bposition
            out.count = out.count + inp.count
            
        else:
            inp = MiniMaxGameBlack(d-1,bposition,1)
            if(inp.value<out.value):
                out.value=inp.value
                out.boardState = bposition
            out.count = out.count + inp.count
            
    return out

board = readBoardState()  
out = MiniMaxGameBlack(depth,board,1)
print("Board Position:", ''.join(out.boardState))
print("Position evaluated by static estimation:",out.count)
print("MINIMAX esitmate:",out.value)
writeBoardState(out.boardState)