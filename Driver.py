#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:46:49 2018

@author: apple
"""
from Minesweeper import Minesweeper

win=0
lose=0
while True:
    height=int(input('Enter a height: '))
    length=int(input('Enter a length: '))
    bomb=int(input('Enter the number of bombs: '))
    while bomb>height*length:
        print('Invalid Input')
        height=int(input('Enter a height: '))
        length=int(input('Enter a length: '))
        bomb=int(input('Enter the number of bombs: '))
    minesweeper=Minesweeper(height,length,bomb)
    #minesweeper._getSolution()
    minesweeper.printBoard()
    x=int(input('Select an x coordinate: '))
    y=int(input('Select an y coordinate: '))
    while not minesweeper.checkValid(y,x):
        print('Invalid Input')
        x=int(input('Select an x coordinate: '))
        y=int(input('Select an y coordinate: '))
    minesweeper.selectFirst(y,x)
    minesweeper.printBoard()
    if minesweeper.isWin():
        win=win+1
        print('You win')
        again=input('Do you want to play again ("yes" or "no")? ')
        if again=='yes':
            continue
        elif again=='no':
            print('Win:'+str(win)+' Lose:'+str(lose))
            break
    while True:
        choice=input('“select” or “flag” or “unflag”? ')
        if choice=='select':
            x=int(input('Select an x coordinate: '))
            y=int(input('Select an y coordinate: '))
            if minesweeper.checkValid(y,x) and minesweeper.board[y-1][x-1].getBomb():
                minesweeper.showAllBombs()
                minesweeper.printBoard()
                minesweeper.setStatus('lose')
                print('Bomb! You lose')
                lose=lose+1
                break
            minesweeper.select(y,x)
            minesweeper.printBoard()
            if minesweeper.isWin():
                win=win+1
                print('You win')
                break
        elif choice=='flag':
            x=int(input('Select an x coordinate: '))
            y=int(input('Select an y coordinate: '))
            minesweeper.flag(y,x)
            minesweeper.printBoard()
        elif choice=='unflag':
            x=int(input('Select an x coordinate: '))
            y=int(input('Select an y coordinate: '))
            minesweeper.unflag(y,x)
            minesweeper.printBoard()
    again=input('Do you want to play again ("yes" or "no")? ')
    if again=='yes':
        continue
    elif again=='no':
        print('Win:'+str(win)+' Lose:'+str(lose))
        break
        
        
            
        
    
    
    
    
    
    
    
    
    
    
    