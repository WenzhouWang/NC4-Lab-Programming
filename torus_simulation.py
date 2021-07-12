# Rat Movement Simulation with slider controls 
import pygame
import math
import sys
import numpy as np
import matplotlib.pyplot as plt

from pygame.locals import(RLEACCEL, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_SPACE) 
import random
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


sys.path.append(".")
from RatTorusClasses import Slider, ImageWidget, MainWindow





WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 50)
BLUE = (50, 50, 255)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)
angle = 1
            
def move_coords(angle, radius, cen):
    theta = math.radians(angle)
    return (cen[0] + radius * math.cos(theta)), (cen[1] + radius * math.sin(theta))

def draw_line(surface, color, pos1, pos2, width):
    pygame.draw.line(surface, color, pos1, pos2, width)

            
   
pygame.display.set_caption("RatPosition")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
     
cen = 400, 300
angle = 1
rect = pygame.Rect(*cen,20,20)
speed = 65
next_tick = 500
vel = 1
c_list = []
p_list = []
movespeed = Slider("w", 0, 7, -7, 300)
slides = [movespeed]    
xp = 0
yp = 1

pygame.init()
running = True
while running:

    screen.fill((122,122,122))
    screen.fill((0,150,0), rect)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for s in slides:
                if s.button_rect.collidepoint(pos):
                    s.hit = True
        if event.type == pygame.MOUSEBUTTONUP:
            for s in slides:
                s.hit = False
        if event.type == pygame.QUIT:
            running = False
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
    angle += movespeed.val
    ticks = pygame.time.get_ticks() 
    coords = move_coords(angle, 100, cen)
    rect.center = coords

    if coords not in c_list:
        c_list.append((coords))
            
    for i in range(len(c_list)-1):
        draw_line(screen,(0,0,255), c_list[i], c_list[i+1], width =2)
        x_vec = c_list[i][0]
        y1_data = c_list[i][1]
        yp = math.cos(math.radians(angle))
    for s in slides:
        if s.hit:
            s.move()

    for s in slides:
        s.sketch()
    
    pygame.display.flip()
    clock.tick(60)
    xp = pygame.time.get_ticks()

    if xp and yp not in p_list:
        p_list.append([xp, yp])


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
pygame.quit()
 