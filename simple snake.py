from turtle import width
import pygame
import random
import time

from pygame.version import PygameVersion

pygame.init()
width,height = 600,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

food_x, food_y = random.randrange(0,width)//10*10,random.randrange(0,height)//10*10

x,y = 50,50
d_x,d_y = 10,0

clock = pygame.time.Clock()

body_list = [(x,y)]

gameover = False

font = pygame.font.Font(None, 55)
font2 = pygame.font.Font(None, 25)

def snake():
    global x,y, food_x , food_y, gameover
    x = (x + d_x)%width
    y = (y + d_y)%height

    if ((x,y)  in body_list):
        gameover = True
        return
    # if the snake eat the food it will added into the body of snake
    body_list.append((x,y))
    if (food_x == x and food_y == y):
        while ((food_x,food_y) in body_list):
            food_x, food_y = random.randrange(0,width)//10*10,random.randrange(0,height)//10*10
    else:
        del body_list[0]

    screen.fill((0,0,0))
    score = font2.render('Made by PROFX ' + 'Score: ' + str(len(body_list)), True, (0,255,0))
    screen.blit(score, [0,0])
    pygame.draw.ellipse(screen, (255,0,0),[food_x , food_y,20,20])
    for (i,j) in body_list:
        pygame.draw.rect(screen, (255,255,255),[i,j,20,20])
    pygame.display.update()

while True:
    if gameover :
        screen.fill((0,0,0))
        score = font2.render('Your_Score: ' + str(len(body_list)), True, (255,0,0))
        screen.blit(score, [0,0])
        msg = font.render('GAME OVER!', False, 'Green')
        screen.blit(msg ,(80,150))
        pygame.display.update()
        time.sleep(8)
        pygame.quit()
        quit()
    events = pygame.event.get()
    for event in events:
         if (event.type == pygame.QUIT):
             pygame.quit()
             quit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                 if d_x != 10:
                    d_x = -10
                 d_y = 0
             elif event.key == pygame.K_RIGHT:
                 if d_x != -10:
                    d_x = 10
                 d_y = 0
             elif event.key == pygame.K_UP:
                 d_x = 0
                 if d_y != 10:
                    d_y = -10
             elif event.key == pygame.K_DOWN:
                 d_x = 0
                 if d_y != -10:
                     d_y = 10
             else:
                 continue
             snake()
    if(not events):
         snake()
    clock.tick(10)
