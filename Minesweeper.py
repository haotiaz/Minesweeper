#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:42:40 2018

@author: apple
"""

from Square import Square
from random import choice

class Minesweeper():
    def __init__(self,a,b,bomb):
        self.height=a
        self.length=b
        self.board=[]
        self.bombNum=bomb
        self.status='In progress'
        for y in range(a):
            self.board.append([])
            for x in range(b):
                self.board[y].append(Square())
        #randomly assign bombs
        for n in range(bomb):
           chosenSquare=choice(choice(self.board))
           while chosenSquare.getBomb():
               chosenSquare=choice(choice(self.board))
           chosenSquare.setBomb(True)
            
    def printBoard(self):
        firstLine='  '
        for a in range(1,self.length+1):
            firstLine=firstLine+str(a)+' '
        print(firstLine[0:-1])
        lineNum=1
        for line in self.board:
            lineText=str(lineNum)+' '
            for square in line:
                lineText=lineText+square.getText()+' '
            print(lineText[0:-1])
            lineNum=lineNum+1
            
    def checkValid(self,y,x):
        if y>self.height or x>self.length or x<1 or y<1:
            return False
        if self.board[y-1][x-1].isSelected():
            return False
        return True
                      
    def select(self,y,x):
        if self.checkValid(y,x) and not(self.board[y-1][x-1].isFlagged()):
            square=self.board[y-1][x-1]
            square.beSelected()
            square.changeText(self.surrounding(y-1,x-1))
            if self.surrounding(y-1,x-1)=='0':
                self.autoSelect(y,x)
        else:
            print('Invalid Input')
            
    def getStatus(self):
        return self.status
    
    def setStatus(self,status):
        self.status=status
    
    def flag(self,y,x):
        if self.checkValid(y,x):
            if not  self.board[y-1][x-1].isFlagged():
                self.board[y-1][x-1].beFlagged()
                self.board[y-1][x-1].changeText('F')
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
        
    def unflag(self,y,x):
        if self.checkValid(y,x):
             if self.board[y-1][x-1].isFlagged():
                self.board[y-1][x-1].beUnflagged()
                self.board[y-1][x-1].changeText('-')
             else:
                print('Invalid Input')
        else:
            print('Invalid Input')
        
    def _getSolution(self):
        for a in range(len(self.board)):
            for b in range(len(self.board[0])):
                if self.board[a][b].getBomb():
                    self.board[a][b].changeText('B')
                else:
                    self.board[a][b].changeText(self.surrounding(a,b))
                    
    def surrounding(self,y,x):
        '''y,x start from 0'''
        bombNum=0
        try:
            if self.board[y+1][x].getBomb():
                if y+1==len(self.board):
                    raise IndexError
                bombNum=bombNum+1
        except IndexError:
            pass
        try:
            if self.board[y+1][x+1].getBomb():
                bombNum=bombNum+1
        except IndexError:
            pass
        try:
            if self.board[y+1][x-1].getBomb():
                if x-1<0:
                    raise IndexError
                bombNum=bombNum+1
        except IndexError:
            pass
        try:
            if self.board[y][x+1].getBomb():
                bombNum=bombNum+1
        except IndexError:
            pass
        try:
            if self.board[y][x-1].getBomb():
                if x-1<0:
                    raise IndexError
                bombNum=bombNum+1
        except IndexError:
            pass
        try:
            if self.board[y-1][x].getBomb():
                if y-1<0:
                    raise IndexError
                bombNum=bombNum+1
        except IndexError:
            pass
        try:
            if self.board[y-1][x+1].getBomb():
                if y-1<0:
                    raise IndexError
                bombNum=bombNum+1
        except IndexError:
            pass
        try:
            if self.board[y-1][x-1].getBomb():
                if y-1<0 or x-1<0:
                    raise IndexError
                bombNum=bombNum+1
        except IndexError:
            pass
        return str(bombNum)
    
    def selectFirst(self,y,x):
        if self.board[y-1][x-1].getBomb():
            newSquare=choice(choice(self.board))
            while newSquare.getBomb():
                newSquare=choice(choice(self.board))
            self.board[y-1][x-1].setBomb(False)
            newSquare.setBomb(True)
        self.select(y,x)
    
    def autoSelect(self,y,x):
        b=y-1
        a=x
        if self.checkValid(b,a) and not(self.board[b-1][a-1].getBomb()):
            self.select(b,a)
        b=y-1
        a=x-1
        if self.checkValid(b,a) and not(self.board[b-1][a-1].getBomb()):
            self.select(b,a)
        b=y-1
        a=x+1
        if self.checkValid(b,a) and not(self.board[b-1][a-1].getBomb()):
            self.select(b,a)
        b=y
        a=x-1
        if self.checkValid(b,a) and not(self.board[b-1][a-1].getBomb()):
            self.select(b,a)
        b=y
        a=x+1
        if self.checkValid(b,a) and not(self.board[b-1][a-1].getBomb()):
            self.select(b,a)
        b=y+1
        a=x-1
        if self.checkValid(b,a) and not(self.board[b-1][a-1].getBomb()):
            self.select(b,a)
        b=y+1
        a=x
        if self.checkValid(b,a) and not(self.board[b-1][a-1].getBomb()):
            self.select(b,a)
        b=y+1
        a=x+1
        if self.checkValid(b,a) and not(self.board[b-1][a-1].getBomb()):
            self.select(b,a)
            
    def isWin(self):
        nonBomb=self.height*self.length-self.bombNum
        select=0
        for line in self.board:
            for square in line:
                if square.getText() in ['0','1','2','3','4','5','6','7','8']:
                    select=select+1
        if select==nonBomb:
            return True
        else:
            return False
     
    def showAllBombs(self):
        for line in self.board:
            for square in line:
                if square.getBomb():
                    square.changeText('B')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    