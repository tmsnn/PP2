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

#INITIALIZING:
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

finished = False

drawing = False

color = BLACK

#Функция чтобы нарисовать ректангл:
def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)
#Функция чтобы нарисовать круг:
def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)
#Функция чтобы создать стерку:
def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)

RAD = 30

#заливаем окно белым цветом
screen.fill(WHITE)
#Начальная и последняя позиция для ректангла:
start_pos = 0
end_pos = 0

#Меняем ректангл -> круг -> стерка и наоборот:
# 0 - Rect
# 1 - Circle
# 2 - Eraser
mode = 0

#лист для рандомных цветов
all_colors = []
# 20 рандомных цветов добавляем в лист
for _ in range(20):
    all_colors.append((randint(0,255), randint(0,255), randint(0,255)))
#главный цикл программы 
while not finished:
    clock.tick(FPS)
    #получаем координаты мышки
    pos = pygame.mouse.get_pos()
    #проверяем на все ивенты
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        
        #выбор цвета:
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pos
            if pos[0] > 20 and pos[0] < 720 and pos[1] > 20 and pos[1] < 40:
                color = screen.get_at(pos)
        #риуем ректангл учитывая координаты мышки
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pos
            rect_x = abs(start_pos[0] - end_pos[0])
            rect_y = abs(start_pos[1] - end_pos[1])
            #по дефолту рисуется ректангл
            if mode == 0:
                drawRect(color, start_pos, rect_x, rect_y)
            #при нажатии на спейс рисуется круг
            elif mode == 1:
                drawCircle(color, start_pos, rect_x)
        #при нажатии на спейс работает стерка
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 2:
                eraser(pos, RAD)
        #ивенты для изменения инструментов
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mode += 1
                mode %= 3
            if event.key == pygame.K_BACKSPACE:
                screen.fill(WHITE)

    w = 30  # ширина палитры
   
    for i, col in enumerate(all_colors):
        pygame.draw.rect(screen, col, (20 + i * w, 20, w, 20))

    pygame.display.flip() #показывает  содержимое экрана
pygame.quit() #закрывает игру