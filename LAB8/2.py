import pygame 
from random import randint, randrange 
pygame.init() 

#INITIALIZING
WIDTH, HEIGHT = 800, 600 
FPS = 9 
cell = 40 
#colors
WHITE = (255, 255, 255) 
GREY = (68, 75, 82) 
RED = (252, 108, 133) 
GREEN = (0, 168, 107) 
BLACK = (0, 0, 0) 
BLUE = (121, 160, 193) 
SNAKE_COLOR = (221, 141, 35)
FOOD_COLOR = (31, 146, 93)
BCG = (204, 204, 255)
RECT_COLOR = (204, 255, 204)

#шрифты 
font = pygame.font.SysFont("Copperplate Gothic Bold", 25) 
font1 = pygame.font.SysFont("Copperplate Gothic Bold", 70) 
 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Snake') 

#global variables
level = 1 
SCORE = 0 
sp = 20 
game_over = font1.render(f'GAME OVER', False, BLACK) 
finished = False 
lose = False 
 
clock = pygame.time.Clock()  

#создаем класс еды
class Food: 
    def __init__(self): 
        self.x = randrange(0, WIDTH, cell) 
        self.y = randrange(0, HEIGHT, cell) 
    def draw(self): 
        pygame.draw.rect(screen, FOOD_COLOR , (self.x, self.y, cell, cell))  
    def redraw(self): 
        self.x = randrange(0, WIDTH, cell) 
        self.y = randrange(0, HEIGHT, cell) 

#создаем класс змейки
class Snake: 
    def __init__(self): 
        self.speed = sp 
        self.body = [[80, 80],[1000,1000],[1040,1040],[1080,1080],[1120,1120],[1160, 1160]] 
        self.dx = self.speed 
        self.dy = 0 
        self.destination = '' 
        self.color = SNAKE_COLOR
    #передвижение змейки
    def move(self): 
        for event in events: 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT and self.destination != 'right': 
                    self.dx = -self.speed 
                    self.dy = 0 
                    self.destination = 'left' 
                if event.key == pygame.K_RIGHT and self.destination != 'left': 
                    self.dx = self.speed 
                    self.dy = 0 
                    self.destination = 'right' 
                if event.key == pygame.K_UP and self.destination != 'down': 
                    self.dx = 0 
                    self.dy = -self.speed 
                    self.destination = 'up' 
                if event.key == pygame.K_DOWN and self.destination != 'up': 
                    self.dx = 0 
                    self.dy = self.speed 
                    self.destination = 'down' 
        for i in range(len(self.body) - 1, 0, -1): 
            self.body[i][0] = self.body[i - 1][0] 
            self.body[i][1] = self.body[i - 1][1] 
 
        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 
 
        self.body[0][0] %= WIDTH 
        self.body[0][1] %= HEIGHT 
    #рисуем змейку
    def draw(self): 
        for block in self.body: 
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell)) 
    #условие когда змейка съедает еду
    def collide_food(self, f:Food): 
        global SCORE
        global level 
        global FPS 
        if self.body[0][0] == f.x and self.body[0][1] == f.y: 
            # f.redraw() 
            SCORE += 1 
            if SCORE % 3 == 0: 
                level += 1 
                FPS += 3
                # sp = self.speed 
            self.body.append([1000, 1000]) 
    #коллизия когда змейка соударяется об себя
    def collide_self(self): 
        global lose 
        if self.body[0] in self.body[1:]: 
            lose = True 
    #условие для проверки чтобы еда не появлялась внутри змейки
    def check_food(self, f:Food): 
        if [f.x, f.y] in self.body: 
            f.redraw() 
            pygame.mixer.music.load(r".\music\apple.mp3")
            pygame.mixer.music.play(0)
#объекты класса змейки и еды
s = Snake() 
f = Food() 

#основной цикл игры
while not finished: 
    clock.tick(FPS) 
    screen.fill(BCG) 
    #прописываем все ивенты
    events = pygame.event.get() 
    for event in events: 
        if event.type == pygame.QUIT: 
            finished = True 
     
    s.draw() 
    s.move() 
    f.draw() 
    s.collide_food(f) 
    s.collide_self() 
 
    game_over_score = font1.render(f'SCORE: {SCORE} ', False, GREEN)     
 
    f.draw() 
    s.draw() 
    s.move() 
    s.collide_food(f) 
    s.collide_self() 
    s.check_food(f) 
      
    text = font.render(f"LEVEL : {level}", False, BLACK) 
    screen.blit(text,(25, 20)) 
    text1 = font.render(f"SCORE : {SCORE}", False, BLACK) 
    screen.blit(text1,(25, 40)) 
    
    #цикл для проигрыша
    while lose: 
        pygame.draw.rect(screen, RECT_COLOR, (100, 75, 600, 400)) 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                finished = True
                lose = False 
            screen.blit(game_over, (270,200)) 
            screen.blit(text,(350, 270)) 
            screen.blit(text1,(350, 300)) 
            pygame.display.flip() 
    pygame.display.flip() 
pygame.quit()