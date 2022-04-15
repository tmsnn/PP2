import pygame, time
import random

# initializing
pygame.init()

# colors 
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
#setting up FPS
FPS = 60
clock = pygame.time.Clock()

#other variables
WIDTH, HEIGHT = 800 , 600
speed = 5
score = 0
picked_coins = 0
i = 2
background = pygame.transform.scale(pygame.image.load("./img/road2.png"), (WIDTH, HEIGHT))
bgY = 0
bgY2 = - background.get_height()
BGSPEED = 3

#шрифты
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game Over', True, BLACK)

#музыка
pygame.mixer.music.load("./music/music1.mp3")
pygame.mixer.music.play()

#cоздаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racer')

#Создаем класс игрока 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("./img/Police.png"), (40,90))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
    #движение противника
    def move(self):
        global score, speed, i
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)
        # увеличиваем скорость противника когда игрок зарабатывает n монеток
        if picked_coins % i == 0 and picked_coins > 1:
            speed += 3
            i += 5
        
# создаем класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.transform.scale(pygame.image.load('./img/Audi.png'),(40,90))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)
    #движение игрока
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right <= WIDTH:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0,-self.speed)
        if keys[pygame.K_DOWN] and self.rect.bottom <= HEIGHT:
            self.rect.move_ip(0, self.speed)

#создаем класс монеток:
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = random.randint(5, 12)
        self.x = random.randint(20, WIDTH - 20)
        self.y = -100
        k  = random.randint(17, 40)
        self.image = pygame.transform.scale(pygame.image.load("./img/Gold_1.png"), (k, k))
        self.surf = pygame.Surface((k,k), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    #движение монеток
    def move(self):
        self.rect.move_ip(0, self.speed)
    #рисуем монетки
    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)
    #когда монетка выходит за рамки окна
    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()

# объекты для классов
P = Player()
E = Enemy()
C = Coin()

#создаем группы для спрайтов
coins = pygame.sprite.Group()
coins.add(C)

enemies = pygame.sprite.Group()
enemies.add(E)

all_sprites = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)

#добавляем новый юсер ивент

finished = False 
lose  = False
# главный цикл игры
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    #заливаем бекграунд
    screen.blit(background,(0,bgY))
    screen.blit(background,(0,bgY2))

    #условие для бесконечного бекграунда
    if bgY > background.get_height():
        bgY = -background.get_height()
    if bgY2 > background.get_height():
        bgY2 = -background.get_height()
    bgY += BGSPEED
    bgY2 += BGSPEED
    #принтим скор и койнсы
    scores = font_small.render(f'SCORE : {score}', True, BLACK)
    screen.blit(scores, (10,10))
    coinn = font_small.render(f'COIN : {picked_coins}', True, BLACK)
    screen.blit(coinn, (10, 29) )

    # выполняем функции для каждого элемента группы спрайтов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    #пока количество койнсов не достигнет 3, добавляем в койнсы
    if len(coins) < 3:
        coins.add(Coin())
    #пока количество противников не достигнет 5, добавляем в противники
    if len(enemies) < 5:
        enemies.add(Enemy())    
    
    #для каждого койна выполняем все функции для койнсов
    for coin in coins:
        coin.draw()
        coin.move()
        coin.kil()
    #коллизия для игрока и монет
        if pygame.sprite.collide_rect(P, coin):
            coin.kill()
            picked_coins += random.randrange(1, 4)
            coins.add(Coin())
   
    # колллизия между игроком и противником
    if pygame.sprite.spritecollideany(P, enemies):
        time.sleep(0.1)
        lose = True
        pygame.mixer.music.stop()
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3) 
        screen.fill(RECT_COLOR)

    #главный цикл игры
    while lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                lose = False
        screen.blit(game_over, (220,230))
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()