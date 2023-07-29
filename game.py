import pygame
import random
pygame.init()
screen = pygame.display.set_mode((650,1280))
pygame.display.set_caption("Hello")
alien=pygame.image.load("alien_4.png")
image = pygame.image.load("startup.png")
pygame.display.set_icon(image)
image_Player=pygame.image.load("space-invaders.png")
image_X=380
image_Y=1020
IN=0
Z=0
image_move = 0
alien_X=random.randint(0,600)
alien_Y=random.randint(0,400)
Change=0.8
#for the alien
def alien_p(x,y):
      screen.blit(alien,(x,y))
#for the space ship
def  player(x,y):
    screen.blit(image_Player,(x,y))
running = True
while running:
    color=(0,0,0)
    screen.fill(color)
  
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
            
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Z=1
            if event.key == pygame.K_UP:
                Z = -1
            if event.key == pygame.K_RIGHT:
                IN = 0.7
            if event.key== pygame.K_LEFT:
                IN =-0.7
        if event.type== pygame.KEYUP:
            #if event.type==pygame.K_LEFT or event.type==pygame.K_RIGHT :
                IN = 0
                Z = 0

    image_X += IN
    alien_X += Change
    image_Y += Z
    if alien_X<=0:
       anime_X=0
       Change=1
    if alien_X >=600:
        alien_X=600
        Change=-1
    
    if image_Y<=0:
        image_Y=0
    if image_Y >=1280:
        image_Y=1280
    if image_X<=0:
        image_X=0
    if image_X>=650:
        image_X=650
    
    alien_p(alien_X,alien_Y)
    player(image_X,image_Y)
    pygame.display.update()
