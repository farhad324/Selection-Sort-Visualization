# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:48:33 2020

@author: farhad324 (Md. Farhadul Islam)
"""

import pygame
import easygui

msg = "Enter Values for Selection Sorting\n\n     Enter values using commas"
title = "Selection Sorting Values"
fieldNames = ["Values"]
fieldValues = []  
fieldValues = easygui.multenterbox(msg,title, fieldNames)

while 1:
    errmsg=''
    if fieldValues[0].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[0])
        fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
    else:
        break
pygame.init() 
height=fieldValues[0].strip().split(',')

for i in range(len(height)):
    height[i]=int(height[i])
    
size1= len(height)*30
size2= max(height) +10
win = pygame.display.set_mode((size1, size2)) 
pygame.display.set_caption("Selection") 
  
x = 5
y = 0
width = 20
run = True
col=(255,0,0)
def show(height,col): 
    
      for i in range(len(height)): 
            
        pygame.draw.rect(win, col, (x + 30 * i, y, width, height[i])) 
        
while run:
    execute = False
    pygame.time.delay(10) 
    keys = pygame.key.get_pressed() 
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            run = False
            
    if keys[pygame.K_SPACE]: 

        execute = True
  
    if execute == False: 
  
        win.fill((0, 0, 0)) 
        show(height,col) 
        pygame.display.update() 
  
    else: 
  
        for i in range(len(height)):         
            min_idx = i

            for j in range(i+1, len(height)): 
  
                if height[min_idx] > height[j]:         
                    min_idx = j
            col=(0,255,0)
            height[i], height[min_idx] = height[min_idx], height[i]
            win.fill((0, 0, 0)) 
            show(height,col) 
            pygame.time.delay(400) 
            pygame.display.update()
            
        col=(0,0,255) 
        show(height,col)
        pygame.display.update()
        message="Sorting Complete\n\n\nDeveloped by Md. Farhadul Islam\nCSE111 Project\nSeptember 2020"
        easygui.msgbox(message, title="Result")
        
pygame.quit()
