import pygame
from random import randint

pygame.init()
#INITIALIZING
WIDTH, HEIGHT = 800, 600
FPS = 25

#цветы
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

background = pygame.transform.scale(pygame.image.load(r".\img\road2.png"), (WIDTH, HEIGHT)) #загружаем картинку для бекграунда
#создаем два бекграунда для эффекта бесконечной дороги
bgY = 0
bgY2 = - background.get_height()
BGSPEED = 7 #скорость движения бекграунда

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racer')

#включаем бесконечную музыку
pygame.mixer.music.load("./music/music1.mp3") 
pygame.mixer.music.play(-1) 

#создаем класс игрока, которая является красной машиной, при этом используем класс спрайтов для точной коллизии
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 400
        self.y = 500
        self.speed = 10
        self.image = pygame.transform.scale(pygame.image.load('.\img\Audi.png'),(40,90)) #подгоняем размер картинки на 40 х 90
        self.surf = pygame.Surface((40,90), pygame.SRCALPHA) #из каринки машины создаем серфейс и убираем края
        self.rect = self.surf.get_rect(center=(self.x,self.y)) #от серфейса получаем ректангл с центром селф,х селф,у
    
    #Переджвижение игрока
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
    #создаем серфейс игрока
    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)
#создаем класс противника 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = randint(8, 13)
        self.x = randint(80, WIDTH - 80)
        self.y = -100
        self.image = pygame.transform.scale(pygame.image.load(".\img\Police.png"), (40,90))
        self.surf = pygame.Surface((40,90), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    #передвижение противника
    def move(self):
        self.rect.move_ip(0, self.speed)
    #рисуем противника 
    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)
    #условие если враг выйдет за рамки окна
    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()
#cоздаем класс монеток
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = randint(10, 15) 
        self.x = randint(80, WIDTH - 80)
        self.y = -100
        self.image = pygame.transform.scale(pygame.image.load(".\img\Gold_1.png"), (25,25)) #подгоняем картинку монетки на размер 25х25
        self.surf = pygame.Surface((25,25), pygame.SRCALPHA) #монетку берем как серфейс и убираем края 
        self.rect = self.surf.get_rect(center = (self.x, self.y)) #серфейс преобразуем в ректангл с центром координатой х и у
    #передвижение монеток, по координате у
    def move(self):
        self.rect.move_ip(0, self.speed)
    #рисуем монетки (серфейс заполняем картинкой монетки)
    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)
    #если монетка вышла за пределы окна
    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 25) 
font_large = pygame.font.SysFont("Times New Roman", 70)

enemies = pygame.sprite.Group([Enemy() for _ in range(3)]) #создаем обьекты для класса врага
coins = pygame.sprite.Group([Coin() for _ in range(5)]) #создаем обьекты для класса монеток
p = Player()

SCORE = 0
game_over = font_large.render(f'GAME OVER', False, BLACK) #текст при проигрыше
finished = False
lose = False
#цикл для игры
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.blit(background,(0,bgY)) 
    screen.blit(background,(0,bgY2))

    #Условие для бесконечной дороги
    if bgY > background.get_height():
        bgY = -background.get_height()
    if bgY2 > background.get_height():
        bgY2 = -background.get_height()
    bgY += BGSPEED
    bgY2 += BGSPEED

    text = font.render(f"SCORE: {SCORE}", False, GREEN)   
    screen.blit(text, (50,20))

    p.draw()
    p.move()
    
    #пока количество врагов не превышает 3, добавляем еще врагов 
    if len(enemies) < 3:
        enemies.add(Enemy())
    #пока количество монет не превышает 5, добавляем еще монет
    if len(coins) < 5:
        coins.add(Coin())
    #для каждого врага выполняем следующие функции
    for enemy in enemies:
        enemy.draw()
        enemy.move()
        enemy.kil()
    #для каждой монетки выполняем следующие функции
    for coin in coins:
        coin.draw()
        coin.move()
        coin.kil()
    #при столкновении игрока и врага срабатывает цикл проигрыша
    if pygame.sprite.spritecollide(p, enemies, False):
        lose = True
        pygame.mixer.music.stop()
    #коллизия когда игрок зарабатывает монетку
    for coin in coins:
        if pygame.sprite.collide_rect(p, coin):
            coin.kill()
            SCORE += 1
            coins.add(Coin())

    game_over_score = font.render(f'SCORE: {SCORE} ', False, GREEN)
    
    #коллизия для двух врагов
    for enemy in enemies:
        for enemy2 in enemies:
            if enemy != enemy2 and pygame.sprite.collide_rect(enemy, enemy2):
                enemy2.kill()
    #цикл для проигрыша
    while lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                lose = False
        pygame.draw.rect(screen, WHITE, (100, 75, 600, 400))
        screen.blit(game_over, (190,100))
        screen.blit(game_over_score, (250,200))
        pygame.display.flip()
    
    pygame.display.flip()
pygame.quit()