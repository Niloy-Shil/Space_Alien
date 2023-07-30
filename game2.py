import pygame
import math
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((720,1280))
#name of game
pygame.display.set_caption("Space Shottter")
#imgae of alien
alien=pygame.image.load("alien_4.png")
#image of logo
image = pygame.image.load("startup.png")
pygame.display.set_icon(image)
#image of soace ship
image_Player=pygame.image.load("space-invaders.png")

#image of bullets
bullets = pygame.image.load("alien.png")
damage =pygame.image.load("damage.png")

#image of background
back=pygame.image.load("foggy.png")
back_img=pygame.transform.scale(back,(720,1280))
Y=0
#moving variables
image_X=380
image_Y=1020
IN=0
Z=0
Change_Y=20
image_move = 0
alien_X=random.randint(0,600)
alien_Y=random.randint(0,400)
Change=25
r = 1
score = 0
#for bullets
bullet_change = 60
bullet_X=0
bullet_Y=0
bullets_state = "ready"

def collision(x1,y1,x2,y2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if  distance <45:
        return True
    else:
        return False
def crash(x1,y1,x2,y2):
    distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if distance<27:
        return True
    else:
        return False    
    
#for the alien
def alien_p(x,y):
      screen.blit(alien,(x,y))
#for the space ship
def  player(x,y):
    screen.blit(image_Player,(x,y))
#function for the bullets
def fire(x,y):
    global bullets_state
    bullets_state="fire"
    screen.blit(bullets,(x+16,y+10))
running = True
while running:
    screen.fill((0,0,0))
    
    screen.blit(back_img,(0,0))
  
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
              if bullets_state is  "ready":
                bullet_X=image_X
                bullet_Y=image_Y
                fire(bullet_X,bullet_Y)
              else:
                  pass
            #if event.key == pygame.K_DOWN:
                #Z=13
            #if event.key == pygame.K_UP:
                #Z = -13
            if event.key == pygame.K_RIGHT:
                IN = 35         
            if event.key== pygame.K_LEFT:
                IN =-35
        if event.type== pygame.KEYUP:
                IN = 0
                Z = 0

    image_X += IN
    alien_X += Change
    #alien_Y+= Change_Y
    #image_Y += Z
    #for alien to move
    if alien_X<=0:
       anime_X=0
       alien_Y+=Change_Y
       Change=25
    if alien_X >=600:
        alien_X=600
        Change=-25
        alien_Y+=Change_Y
        
    """if alien_Y<=0:
        alien_Y=0
        Change_Y=5
    if alien_Y >=400:
        alien_Y=400
        Change_Y=-5  
        """
        
    """if image_Y<=0:
        image_Y=0
    if image_Y >=1280:
        image_Y=1280
        
        """
    if image_X<=0:
        image_X=0
    if image_X>=650:
        image_X=650
    if bullets_state is "fire":
        bullet_Y -= bullet_change
        fire(bullet_X,bullet_Y)
        
    if bullet_Y <= 0:
              bullets_state="ready"
              bullet_X=image_X
              bullet_Y=image_Y    
    alien_p(alien_X,alien_Y)
    player(image_X,image_Y)
    Collision = collision(bullet_X,bullet_Y,alien_X,alien_Y)    
    if Collision:
              
              screen.blit(damage,(bullet_X,bullet_Y))
              bullet_Y = 1020
              bullets_state="ready"
              score += 1
              alien_X=random.randint(0,600)
              alien_Y=random.randint(0,400)
    destroy= crash(image_X,image_Y,alien_X,alien_Y)
    if destroy:
         screen.blit(damage,(bullet_X,bullet_Y))
         image_X=380
         image_Y=1020
         alien_X=random.randint(0,600)
         alien_Y=random.randint(0,400)               
    
    
  
              
      
   
    pygame.display.flip()
