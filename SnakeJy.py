import pygame as pg
import random
from pygame.locals import *
pg.init()

snake_length = []
class Snake():
    def __init__(self, xpos, ypos, prev_x, prev_y):
        self.xpos = xpos
        self.ypos = ypos
        self.prev_x = prev_x
        self.prev_y = prev_y
    
#    def add_snake(self):
#        snake_length.append(self)

def snake_pos():
    counter = 1
    while counter <= len(snake_length)-1:
        snake_length[counter].prev_x = snake_length[counter].xpos
        snake_length[counter].prev_y = snake_length[counter].ypos
        snake_length[counter].xpos = snake_length[counter-1].prev_x
        snake_length[counter].ypos = snake_length[counter-1].prev_y
        counter += 1

def snake_bod(snake_length):
    length = len(snake_length)
    snake_length.append(Snake(snake_length[length-1].prev_x, snake_length[length-1].prev_y, None, None))

def snake_lose():
    counter = 1
    while (counter <= len(snake_length)-1):
        x = snake_length[counter]
        if (x.xpos - 10 <= snake_length[0].xpos <= x.xpos +10 and x.ypos -10 <= snake_length[0].ypos <= x.ypos +10):
            running = False
        counter += 1


SIZE = WIDTH , HEIGHT = 800,600
clock = pg.time.Clock()
WINDOWS = pg.display.set_mode(SIZE)

snake_size = 20
x_change = 0
y_change = 0
cube_x = random.randrange(20,780,20)
cube_y = random.randrange(20, 580, 20)
score = 0
snake_length.append(Snake(400,300, None, None))

font = pg.font.Font(None, 24)
text = font.render('Score: ' + str(score), False, 'white')
textRect = text.get_rect()
textRect.center = (40, 20)

running = True
while (running):
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            running = False
        elif (event.type == pg.KEYDOWN):
            if (event.key == pg.K_ESCAPE):
                running = False
            elif (event.key == pg.K_RIGHT and x_change != -20):
                x_change = 20
                y_change = 0
            elif (event.key == pg.K_LEFT and x_change != 20):
                x_change = -20
                y_change = 0
            elif (event.key == pg.K_UP and y_change != 20):
                x_change = 0
                y_change = -20
            if (event.key == pg.K_DOWN and y_change != -20):
                x_change = 0
                y_change = 20

    snake_pos()
    snake_length[0].prev_x = snake_length[0].xpos
    snake_length[0].prev_y = snake_length[0].ypos
    
    WINDOWS.fill('black')

    for x in snake_length:
        pg.draw.rect(WINDOWS, 'white', pg.Rect(x.xpos, x.ypos, snake_size - 1 ,snake_size - 1))
    
    if (len(snake_length) > 1):
        snake_lose()
        
    snake_length[0].xpos += x_change
    snake_length[0].ypos += y_change

    font = pg.font.Font(None, 24)
    text = font.render('Score: ' + str(score), False, 'white')
    textRect = text.get_rect()
    textRect.center = (40, 20)

    if (cube_x - 10 <= snake_length[0].xpos <= cube_x + 10 and cube_y - 10 <= snake_length[0].ypos <= cube_y + 10 ):
        cube_x = random.randrange(20,780,20)
        cube_y = random.randrange(20, 580,20)
        if (score >= 10):
            snake_bod(snake_length)
            snake_bod(snake_length)
            score += 2
        elif (score >= 20):
            snake_bod(snake_length)
            snake_bod(snake_length)
            snake_bod(snake_length)
            score += 3
        else:
            snake_bod(snake_length)
            score += 1
        
    WINDOWS.blit(text,textRect)

    if (800 <= snake_length[0].xpos):
        snake_length[0].xpos = 0
    elif (snake_length[0].xpos <= 0):
        snake_length[0].xpos = 800

    elif (600 <= snake_length[0].ypos):
        snake_length[0].ypos = 0
    elif (snake_length[0].ypos <= 0):
        snake_length[0].ypos = 600

    pg.draw.rect(WINDOWS, 'red', pg.Rect(cube_x, cube_y, 20, 20))
    pg.display.flip()
    clock.tick(15)

WINDOWS.fill('black')
font = pg.font.Font(None, 72)
text = font.render('You Lose!!!!' , False, 'white')
textRect = text.get_rect()
textRect.center = (400, 300)

clock.tick(0.1)
pg.quit()
quit()
