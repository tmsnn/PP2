from math import sqrt
import pygame
from random import randint

pygame.init()

#Global Variables:
WIDTH, HEIGHT = 800, 600
FPS = 60

#Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

#Initializing:
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

finished = False

drawing = False

color = BLACK

#Функции для рисовки:
def drawRect(color, pos, width, height):  
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4) 

def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

def square(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)
#рисуем прямоугольный треугольник
def r_triangle(color, z, x): 
    x1 = z[0]                 
    x2 = x[0]                 
    y1 = z[1]
    y2 = x[1]
    pygame.draw.line(screen, color, z, x, 2)
    pygame.draw.line(screen, color, (x1,y1), (x1,y2), 2)
    pygame.draw.line(screen, color, (x1,y2), (x2,y2), 2)
#функция для ромба
def romb(color, z,x): 
    x1 = z[0]
    x2 = x[0]
    delta = (abs(x1-x2)//2)//sqrt(3)
    y1 = z[1]
    y2 = x[1]
    pygame.draw.line(screen, color, (x1, y1), (x1-(delta), y2), 2)
    pygame.draw.line(screen, color, (x1 - (delta), y2), (x2 - (delta), y2), 2)
    pygame.draw.line(screen, color, (x1, y1), (x2, y1), 2)
    pygame.draw.line(screen, color, (x2 - (delta), y2), (x2, y1), 2)

#функция для правильного треугольника
def e_triangle(color,z,x): 
    x1 = z[0]
    x2 = x[0]
    y1 = z[1]
    y2 = x[1]
    pygame.draw.line(screen,color,z,x,2)
    deltax = abs(x2-x1)
    deltay = abs(y2-y1)
    x4 = (deltax + x1)
    y4 = (deltay + y1)
    
    y4 += deltax

    pygame.draw.line(screen,color,(x4,y4),x,2)
    pygame.draw.line(screen,color,z,(x4,y4),2)

RAD = 30

screen.fill(WHITE)
#начальные и последние координаты ректангла:
start_pos = 0
end_pos = 0

#константа чтобы менять инструмент:
mode = 0

#лист для рандомных 20 цветов
all_colors = []

for _ in range(20):
    all_colors.append((randint(0,255), randint(0,255), randint(0,255)))

while not finished:

    pos = pygame.mouse.get_pos() #позиция мышки

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            finished = True
        
        #выбор цвета:
        if event.type == pygame.MOUSEBUTTONDOWN: #мышка была зажата
            drawing = True
            start_pos = pos 

            if pos[0] > 20 and pos[0] < 720 and pos[1] > 20 and pos[1] < 40: 
                color = screen.get_at(pos)
       
        if event.type == pygame.MOUSEBUTTONUP:  #мышка была отпущена 
            drawing = False
            end_pos = pos #последняя позиция мышки

            rect_x = abs(start_pos[0] - end_pos[0]) #difference by x
            rect_y = abs(start_pos[1] - end_pos[1]) #difference by y
            
            if mode == 0:
                drawRect(color, start_pos, rect_x, rect_y)
            elif mode == 1:
                drawCircle(color, start_pos, rect_x)
            elif mode == 2:
                if rect_x<rect_y:rect_x=rect_y
                square(color, start_pos, rect_x, rect_x)
            elif mode == 3:
                r_triangle(color, start_pos,end_pos)
            elif mode == 4:
                e_triangle(color, start_pos,end_pos)
            elif mode == 5:
                romb(color, start_pos,end_pos)
        #стерка
        if event.type == pygame.MOUSEMOTION and drawing:  
            if mode == 6:
                eraser(pos, RAD)
        #меняем инструмент
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_SPACE: 
                mode += 1
                if mode==7 : mode=0
            if event.key == pygame.K_BACKSPACE: #если зажать спейс, очистится весь экран
                screen.fill(WHITE)

    w = 30  #ширина палитры
    for i, col in enumerate(all_colors):
        pygame.draw.rect(screen, col, (20 + i * w, 20, w, 20)) #dрисуем ректанглы для каждого цвета
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()