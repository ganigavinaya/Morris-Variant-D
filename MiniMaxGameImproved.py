# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 00:36:16 2017

@author: Mohanakrishna
"""

import sys
import MorrisGameBoard

maxValue = sys.maxsize
minValue = -sys.maxsize
depth = int(sys.argv[3])
board = list()

def readBoardState():
    #print("Reading board state")
    board3 = open(sys.argv[1],"r")
    board = list()
    for line in board3:
        for ch in line:
            board.append(ch)
    return board

def writeBoardState(outBoardState):
    board4 = open(sys.argv[2],"w")
    for each in outBoardState:
        board4.write(each)
    board4.close()

def MiniMaxGameImproved(d,board,flag):
#   print('Min Max call')
    out = MorrisGameBoard.outputClass()
    inp = MorrisGameBoard.outputClass()
    boardList = list()
    if(d==0):
        wcount = 0
        bcount = 0
        diff = 0
        mills = 0
        staticEstimate = 0
        for pos in range(0,len(board)):
            if(board[pos]=='W'):
                wcount= wcount+1
            elif(board[pos]=='B'):
                bcount = bcount+1                
        diff = wcount-bcount
        
        for each in range(0,len(board)):
            if(board[each]=='x'):
                if(MorrisGameBoard.checkMills(each,board,'W')==True):
                    mills = mills+1
        
        staticEstimate = diff + mills
        l = MorrisGameBoard.generateMovesMidgameEndgameBlack(board)
        l_size = len(l)
        
        if(bcount<=2):
            out.value = 10000
#            print("White Won")
        elif(wcount<=2):
            out.value = -10000
#            print("Black Won")
        elif(l_size==0):
            out.value = 10000
        else:
            out.value = 1000*(staticEstimate) - l_size
        out.count +=1
        return out
    
    if(flag==1):
#        print("Flag1")
        boardList = MorrisGameBoard.generateMovesMidgameEndgame(board)
        #print(boardList)
        out.value = minValue
    else:
        boardList = MorrisGameBoard.generateMovesMidgameEndgameBlack(board)
        out.value = maxValue
        
    for b in boardList:
        if(flag==1):
            inp = MiniMaxGameImproved(d-1,b,0)
            if(inp.value>out.value):
                out.value=inp.value
                out.boardState = b
            out.count = out.count + inp.count
            
        else:
            inp = MiniMaxGameImproved(d-1,b,1)
            if(inp.value<out.value):
                out.value=inp.value
                out.boardState = b
            out.count = out.count + inp.count         
    return out

board = readBoardState()  
output = MiniMaxGameImproved(depth,board,1)
print("Board Position:", ''.join(output.boardState))
print("Position evaluated by static estimation:",output.count)
print("MINIMAX esitmate:",output.value)
writeBoardState(board)