import pygame
from random import randrange
import psycopg2
from config import params

exist = False
playerName = input("Enter your name:")

config = psycopg2.connect(**params)
current = config.cursor()

pygame.init()

#Initializing
WIDTH, HEIGHT = 800,800
cell = 40   
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 10
#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255,182,193)
class Snake:
    #Initializing
    def __init__(self):
        self.speed = cell
        self.body = [[WIDTH//2, HEIGHT//2]]
        self.dx = self.speed
        self.dy = 0
        self.direction = ''
        self.color = RED
    #draw snake
    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell))
    #function for move snake
    def move(self,events):
    #check the directions for the correct movement of the snake
        global ok
        GG = True
        for event in events:
            if event.type == pygame.KEYDOWN:
                ok = True
                if event.key == pygame.K_LEFT and self.direction != 'right' and GG:
                    self.direction = 'left'
                    self.dx = -self.speed
                    self.dy = 0
                    GG = False
                elif event.key == pygame.K_RIGHT and self.direction != 'left' and GG:
                    self.direction = 'right'
                    self.dx = self.speed
                    self.dy = 0
                    GG = False
                elif event.key == pygame.K_UP and self.direction != 'down' and GG:
                    self.direction = 'up'
                    self.dx = 0
                    self.dy = -self.speed
                    GG = False
                elif event.key == pygame.K_DOWN and self.direction != 'up' and GG:
                    self.direction = 'down'
                    self.dx = 0
                    self.dy = self.speed
                    GG = False
        #correctly position the added element in the snake
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        #so that our snake melts in silence at the beginning of the game
        if ok:   
            self.body[0][0] += self.dx
            self.body[0][1] += self.dy
            GG = True
        
        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT
    #contact with food
    def collide_food(self,Food):
        global score,cnt,ONE_deas,ONE_S_P
        if self.body[0][0] == Food.x and self.body[0][1] == Food.y:
            ONE_deas = True
            ONE_S_P =True
            self.body.append([1000, 1000])
            score += 1
            cnt += 1
    #contact with self
    def collide_self(self):
        global lose
        if self.body[0] in self.body[1:]:
            lose = True
            #finished = True
            #choose_level = False
    #contact with deas. food
    def collide_deas(self,deas):
        global score,time_deas
        if self.body[0][0] in range(deas.x,deas.x + 2*cell) and self.body[0][1] in range(deas.y,deas.y+2*cell):
            score += int(FPS*2.5-time_deas)
            return True
    #check food created in our snake or not
    def check_food(self, Food): 
        if [Food.x, Food.y] in self.body:
            Food.redraw()
    def check_deas(self,disappearing_food):
        if [disappearing_food.x,disappearing_food.y] in self.body[1:]:
            disappearing_food.redraw()
    def check_speed_food(self,S_P):
        if [S_P.x, S_P.y] in self.body[1:]:
            S_P.redraw()
    

#class for food
class Food:
    #Initializing
    def __init__(self,color):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
        self.color = color
    #draw food
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, cell, cell)) 
    #if food in walls or in snake redraw our food
    def redraw(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
#class for wall
class Wall:
    #Initializing
    def __init__(self, x, y):
        self.x, self.y = x, y
    #draw wall
    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, cell, cell))
class disappearing_food(pygame.sprite.Sprite):
    def __init__(self):
        self.x = randrange(40, WIDTH-40, cell)
        self.y = randrange(40, HEIGHT-40, cell)
    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, cell*2, cell*2)) 
    def redraw(self):
        self.x = randrange(40, WIDTH-40, cell)
        self.y = randrange(40, HEIGHT-40, cell)
        
#Variables
font = pygame.font.Font("./font/player.ttf",40)
level = 0
restart = True
surf = pygame.surface.Surface((600,300))
choose_level = True


while restart:
    #Variables
    finished = False
    snake = Snake()
    food = Food(GREEN)
    snake_speed = ""
    score = 0
    ok = False
    lose = False
    exist = False
    cnt = 1
    d_f = 0
    S_P = 0
    TIME_deas = False
    ONE_deas = True
    time_deas = 0
    while choose_level:
        events = pygame.event.get()
        pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                finished = True
                restart = False
                choose_level = False
            #choose our level
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    choose_level = False
            #choose our level
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] >= 130 and pos[0] <= 200 and pos[1] >= 440 and pos[1] <= 480:
                    snake_speed = "easy"
                    choose_level = False
                if pos[0] >= 300 and pos[0] <= 410 and pos[1] >= 440 and pos[1] <= 480:
                    snake_speed = "medium"
                    choose_level = False
                if pos[0] >= 500 and pos[0] <= 570 and pos[1] >= 440 and pos[1] <= 480:
                    snake_speed = "hard"
                    choose_level = False
        #create menu
        easy = font.render("easy",True,WHITE)
        medium = font.render("medium",True,WHITE)
        hard = font.render("hard",True,WHITE)
        text = font.render("Сlick to select level (speed)",True,WHITE)
        screen.fill(WHITE)
        surf.fill(BLUE)
        screen.blit(surf,(110,200))
        screen.blit(text,(120,380))
        screen.blit(easy,(130,440))
        screen.blit(medium,(300,440))
        screen.blit(hard,(500,440))
        pygame.display.flip()
    while not finished:
        #set our speed
        if snake_speed == "easy":
            FPS = 5
        elif snake_speed == "medium":
            FPS = 10
        elif snake_speed == "hard":
            FPS = 13
        clock.tick(FPS)
        screen.fill(BLACK)
        #create cells
        for i in range(0, WIDTH, cell):
            for j in range(0, HEIGHT, cell):
                pygame.draw.rect(screen, WHITE, (i, j, cell, cell), 1)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                finished = True
                restart = False
            #change level,restart,return to menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    if level < 5:
                        level += 1
                    finished = True
                    choose_level = False
                if event.key == pygame.K_m:
                    if level > 0:
                        level -= 1
                    finished = True
                    choose_level = False
                if event.key == pygame.K_r:
                    finished = True
                if event.key == pygame.K_y:
                    finished = True
                    choose_level = True
        walls_coor = open(f'level{level}.txt', 'r').readlines()#read our walls
        walls = []
        #create walls
        for i, line in enumerate(walls_coor):
            for j, each in enumerate(line):
                if each == "#":
                    walls.append(Wall(j * cell, i * cell))
        Score = font.render(f"score:{score}",True,WHITE)
        look_level = font.render(f"level:{level+1}",True,WHITE)
        #create,check time for deas. food 
        if cnt % 5 == 0 and ONE_deas:
            d_f = disappearing_food()
            ONE_deas = False
            TIME_deas = True
        if TIME_deas:
            time_deas += 1
            if time_deas == int(2.5*FPS) or snake.collide_deas(d_f):
                d_f = 0
                TIME_deas = False
                time_deas = 0
        #calling all functions
        try:
            d_f.draw()
            snake.check_deas(d_f)
            snake.collide_deas(d_f)
        except:
            pass
        food.draw()
        snake.draw()
        snake.move(events)
        snake.collide_food(food)
        snake.collide_self()
        snake.check_food(food)
        #draw walls
        for wall in walls:
            wall.draw()
            if food.x == wall.x and food.y == wall.y:
                food.redraw()
            if snake.body[0][0] == wall.x and snake.body[0][1] == wall.y:
                lose = True    
            try:
                if wall.x in range(d_f.x,d_f.x+cell*2) and wall.y in range(d_f.y,d_f.y+cell*2):
                    d_f.redraw()
            except:
                pass
        if lose:
            insert_into = '''
            INSERT INTO records VALUES (%s, %s);
            '''
            try:
                get = f'''
                    SELECT record FROM records WHERE name = '{playerName}';
                '''
                current.execute(get)
                output = current.fetchone()
                high_score = output[0]
                exist = True
            except:
                pass
            if exist:
                if score > high_score:
                    update = '''
                        UPDATE records SET record = %s WHERE name = %s;
                    '''
                    current.execute(update,(score,playerName))
            else:
                current.execute(insert_into, (f'{playerName}', f'{score}'))
            current.close()
            config.commit()
            config.close()
            
            finished = True
        screen.blit(Score,(50,42))
        screen.blit(look_level,(WIDTH-150,42))
        pygame.display.flip()
pygame.quit()