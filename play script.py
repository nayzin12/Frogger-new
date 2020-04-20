#
#
#        Frogger
#
#
#
#################################

import sys
 
import pygame
from pygame.locals import *
     
def main():

    pygame.init()
     
    fps = 60
    fpsClock = pygame.time.Clock()
     
    width, height = 516,680
    screen = pygame.display.set_mode((width, height))
    
    xpos=0
    #
    deltax=0
    deltay=0
    shift=0
     
    # Game loop.
    while True:
      screen.fill((0, 0, 0))
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

#
        if event.type == pygame.KEYDOWN:
                key = event.dict['key']
                if key == pygame.K_UP:
                    deltay-=20
                    for i in range(0,200,100):
                        shift+=i
                     
                elif key == pygame.K_LEFT:
                   deltax-=20
                   left=True
                elif key == pygame.K_RIGHT:
                   deltax+=20
                   left=False
                elif key == pygame.K_DOWN:
                    deltay+=20
                    for i in range(0,200,100):
                        shift+=i
                else:
                   deltax=0
      
      # Update.
      
      background_image=pygame.image.load("background.png")
    
      spread_sheet=pygame.image.load("frogger.png")
#
      frog = pygame.image.load("frog.png")

      car_type1=spread_sheet.subsurface((110,47,50,40))

      car_list=[]
#converted car subsurface
      car1=car_type1.get_rect()
#coordinates for the new rect
      car1.x=(816-xpos)%816-200
      car1.y=425

      car_list.append(car1)
    

      frog=frog.subsurface((9+(shift%200),0,40,40))
#converted frog subsurface
      frog_rect=frog.get_rect()
#coordinates for the new rect
      frog_rect.x=258+deltax
      frog_rect.y=590+deltay
      
      # Draw.

      screen.blit(background_image,[0,0])
#when you blit the converted image the format is (loaded_image,converted_image)
      screen.blit(car_type1,car1)
      xpos+=3
#when you blit the converted image the format is (loaded_image,converted_image)
      screen.blit(frog,frog_rect)

      collide=frog_rect.collidelist(car_list)

      if collide == 0:
          deltax=deltax-deltax
          deltay=deltay-deltay

      
      
      pygame.display.flip()
      fpsClock.tick(fps)

main()
