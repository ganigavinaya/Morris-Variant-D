# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 15:26:11 2017

@author: Mohanakrishna
"""

from copy import deepcopy

#Defining the output class
class outputClass(object):
    count = 0
    value = 0
    boardState = list()
    
    def __init__(self,value=0,count=0,boardState=list()):
        self.count = count
        self.value = value
        self.boardState = boardState
    

#Flip the board for Black Opening Move
def flipBoard(boardtoflip):
    b = list(range(0,23))
    for position in range(0,len(boardtoflip)):
        if(boardtoflip[position]=='B'):
            b[position]='W'
        elif(boardtoflip[position]=='W'):
            b[position]='B'
        else:
            b[position]='x'
    return b
    
def generateMoveOpening(boardPostion):
    listOfBoardPosition = list()
    listOfBoardPosition = generateAdd(boardPostion)
    return listOfBoardPosition

def generateMoveOpeningBlack(b):
    tempb = flipBoard(b)
    blackMoves = list()
    blackMoves = generateAdd(tempb)
    moves = list()
    
    for each in range(0,len(blackMoves)):
        b = blackMoves[each]
        moves.insert(each,flipBoard(b))
    return moves 

#checjs close mill
def closeMill(position,b):
    C = b[position]
    if(C=='x'):
        return False
    else:
        return checkMills(position,b,C)

#White Mill case
def checkMills(position,b,C):
    if(C=='x'):
#        print("Mill not formed!!!")
        return False;
    
    if(position==0):
        if((b[1]==C and b[2]==C) or (b[3]==C and b[6]==C) or (b[8]==C and b[20]==C)):
            return True
        return False
    
    elif(position==1):
        if(b[0]==C and b[2]==C):
            return True
        return False
    
    elif(position==2):
        if((b[0]==C and b[1]==C) or (b[5]==C and b[7]==C) or (b[13]==C and b[22]==C)):
            return True
        return False
    
    elif(position==3):
        if((b[0]==C and b[6]==C) or (b[4]==C and b[5]==C) or (b[9]==C and b[17]==C)):
            return True
        return False
    
    elif(position==4):
        if(b[3]==C and b[5]==C):
            return True
        return False

    elif(position==5):
        if((b[3]==C and b[4]==C) or (b[2]==C and b[7]==C) or (b[12]==C and b[19]==C)):
            return True
        return False    
    
    elif(position==6):
        if((b[0]==C and b[3]==C) or (b[10]==C and b[14]==C)):
            return True
        return False 
    
    elif(position==7):
        if((b[2]==C and b[5]==C) or (b[11]==C and b[16]==C)):
            return True
        return False
    
    elif(position==8):
        if((b[0]==C and b[20]==C) or (b[9]==C and b[10]==C)):
            return True
        return False
    
    elif(position==9):
        if((b[8]==C and b[10]==C) or (b[3]==C and b[17]==C)):
            return True
        return False

    elif(position==10):
        if((b[8]==C and b[9]==C) or (b[6]==C and b[14]==C)):
            return True
        return False 
    
    elif(position==11):
        if((b[7]==C and b[16]==C) or (b[12]==C and b[13]==C)):
            return True
        return False
    
    elif(position==12):
        if((b[11]==C and b[13]==C) or (b[5]==C and b[19]==C)):
            return True
        return False
    
    elif(position==13):
        if((b[11]==C and b[12]==C) or (b[2]==C and b[22]==C)):
            return True
        return False    
    
    elif(position==14):
        if((b[17]==C and b[20]==C) or (b[15]==C and b[16]==C) or (b[6]==C and b[10]==C)):
            return True
        return False 
    
    elif(position==15):
        if((b[14]==C and b[16]==C) or (b[18]==C and b[21]==C)):
            return True
        return False
    
    elif(position==16):
        if((b[14]==C and b[15]==C) or (b[19]==C and b[22]==C) or (b[7]==C and b[11]==C)):
            return True
        return False

    elif(position==17):
        if((b[3]==C and b[9]==C) or (b[14]==C and b[20]==C) or (b[18]==C and b[19]==C)):
            return True
        return False

    elif(position==18):
        if((b[17]==C and b[19]==C) or (b[15]==C and b[21]==C)):
            return True
        return False
    
    elif(position==19):
        if((b[17]==C and b[18]==C) or (b[16]==C and b[22]==C) or (b[5]==C and b[12]==C)):
            return True
        return False    
    
    elif(position==20):
        if((b[0]==C and b[8]==C) or (b[14]==C and b[17]==C) or (b[21]==C and b[22]==C)):
            return True
        return False
    
    elif(position==21):
        if((b[20]==C and b[22]==C) or (b[15]==C and b[18]==C)):
            return True
        return False
    
    elif(position==22):
        if((b[2]==C and b[13]==C) or (b[16]==C and b[19]==C) or (b[20]==C and b[21]==C)):
            return True
        return False
    
    else:
        return False
    
#To remove the black poisition in case of a mill    
def generateRemove(boardPos,L):
    for i in range(0,len(boardPos)):
        if boardPos[i]=='B':
            if(closeMill(i,boardPos)==False):
                b_updated = deepcopy(boardPos)   
                b_updated[i]='x'
                L.append(b_updated)
    return L

#Adding new white piece
def generateAdd(boardPosition):
    listOfPositions = list()
    for pos in range(0,len(boardPosition)):
        if(boardPosition[pos]=='x'):
            b = deepcopy(boardPosition)
            b[pos]='W'
            if (closeMill(pos,b)):
                listOfPositions = generateRemove(b,listOfPositions)
            else:
                listOfPositions.append(b)
    return listOfPositions

#Returns the nearest neighbors' position
def neighbors(position):
    neighborList = list()
    
    if(position==0):
        neighborList.append(1)
        neighborList.append(3)
        neighborList.append(8)
        
    elif(position==1):
        neighborList.append(0)
        neighborList.append(2)
        neighborList.append(4)
        
    elif(position==2):
        neighborList.append(1)
        neighborList.append(5)
        neighborList.append(13)
        
    elif(position==3):
        neighborList.append(0)
        neighborList.append(4)
        neighborList.append(6)
        neighborList.append(9)
        
    elif(position==4):
        neighborList.append(1)
        neighborList.append(3)
        neighborList.append(5)
        
    elif(position==5):
        neighborList.append(2)
        neighborList.append(4)
        neighborList.append(7)
        neighborList.append(12)

    elif(position==6):
        neighborList.append(3)
        neighborList.append(7)
        neighborList.append(10)
    
    elif(position==7):
        neighborList.append(5)
        neighborList.append(6)
        neighborList.append(11)
    
    elif(position==8):
        neighborList.append(0)
        neighborList.append(9)
        neighborList.append(20)
        
    elif(position==9):
        neighborList.append(3)
        neighborList.append(8)
        neighborList.append(10)
        neighborList.append(17)
        
    elif(position==10):
        neighborList.append(6)
        neighborList.append(9)
        neighborList.append(14)
        
    elif(position==11):
        neighborList.append(7)
        neighborList.append(12)
        neighborList.append(16)
        
    elif(position==12):
        neighborList.append(5)
        neighborList.append(11)
        neighborList.append(13)
        neighborList.append(19)
       
    elif(position==13):
        neighborList.append(2)
        neighborList.append(12)
        neighborList.append(22)    
     
    elif(position==14):
        neighborList.append(10)
        neighborList.append(15)
        neighborList.append(17)
        
    elif(position==15):
        neighborList.append(14)
        neighborList.append(16)
        neighborList.append(18)
        
    elif(position==16):
        neighborList.append(11)
        neighborList.append(15)
        neighborList.append(19)
        
    elif(position==17):
        neighborList.append(9)
        neighborList.append(14)
        neighborList.append(18)
        neighborList.append(20)
    
     
    elif(position==18):
        neighborList.append(15)
        neighborList.append(17)
        neighborList.append(19)
        neighborList.append(21)
        
    elif(position==19):
        neighborList.append(12)
        neighborList.append(16)
        neighborList.append(18)
        neighborList.append(22)
        
    elif(position==20):
        neighborList.append(8)
        neighborList.append(17)
        neighborList.append(21)
        
    elif(position==21):
        neighborList.append(18)
        neighborList.append(20)
        neighborList.append(22)
        
    elif(position==22):
        neighborList.append(13)
        neighborList.append(19)
        neighborList.append(21)
    
    else:
        return neighborList
        
    return neighborList

def generateMove(boardPosition):
    listOfPositions = list()

    for pos in range(0,len(boardPosition)):
        if(boardPosition[pos]=='W'):
            n = neighbors(pos)
            for j in n:
                if(boardPosition[j]=='x'):
                    b = deepcopy(boardPosition)
                    b[pos]='x'
                    b[j]='W'
                    if(closeMill(j,b)):
                        listOfPositions = generateRemove(b,listOfPositions)
                    else:
                        listOfPositions.append(b)
    return listOfPositions
                     

def generateMovesMidgameEndgame(boardPosition):
    wcount = 0
    l = list()
    for position in range(0,len(boardPosition)):
        if(boardPosition[position]=='W'):
            wcount = wcount+1
    
    if(wcount==3):
        l = generateHopping(boardPosition)
    else:
        l = generateMove(boardPosition)
    return l

def generateMovesMidgameEndgameBlack(boardPosition):
    temp = flipBoard(boardPosition)
    l = list()
    listofPositions = generateMovesMidgameEndgame(temp)
    for pos in range(0,len(listofPositions)):
        b = listofPositions[pos]
        l.insert(pos,flipBoard(b))
    return l
    
def generateHopping(boardPosition):
    listofPositions = list()
    for alpha in range(0,len(boardPosition)):
        if(boardPosition[alpha]=='W'):
            for beta in range(0,len(boardPosition)):
                if (boardPosition[beta]=='x'):
                    b = deepcopy(boardPosition)
                    b[alpha]='x'
                    b[beta]='W'
                    if(closeMill(beta,b)):
                        listofPositions = generateRemove(b,listofPositions)
                    else:
                        listofPositions.append(b)
    return listofPositions