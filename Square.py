#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:05:43 2018

@author: apple
"""

class Square:
    def __init__(self):
        self.text='-'
        self.selected=False
        self.flagged=False
        self.isBomb=False
        
    def beSelected(self):
        self.selected=True
        
    def isSelected(self):
        return self.selected
    
    def beFlagged(self):
        self.flagged=True
        
    def beUnflagged(self):
        self.flagged=False
        
    def setText(self,t):
        self.text=t
        
    def getText(self):
        return self.text
    
    def getBomb(self):
        return self.isBomb
    
    def setBomb(self,b):
        self.isBomb=b
        
    def isFlagged(self):
        return self.flagged
    
    def changeText(self,text):
        self.text=text