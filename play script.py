
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





    #variables
    speed1 = 2
    speed2 = 3
    speed3 = 4
    xpos1=0
    xpos2=0
    xpos3=0
    deltax=0
    deltay=0
    shift=0
    lane_list = [420,375,323,278,188,135,75]

    #Load up the images
    background_image=pygame.image.load("background.png").convert_alpha()
    
    spread_sheet=pygame.image.load("frogger.png").convert_alpha()
#
    #Cut out the models
    car_type1=spread_sheet.subsurface(110,47,50,40)

    car_type2=spread_sheet.subsurface(115,203,50,40)

    car_type3=spread_sheet.subsurface(45,128,120,47)

    car_type4=spread_sheet.subsurface(105,270,55,45)

    log_type1=spread_sheet.subsurface(277,341,223,51)

    log_type2=spread_sheet.subsurface(275,268,175,57)
     
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
      frog = pygame.image.load("frog.png").convert_alpha()
      


#converted car subsurface
      #Lane 1
      #First=startpos, second=biggeststart, third=distance
      car1=car_type1.get_rect()
      car1.x=(716-xpos2)%1516-200
      car1.y= lane_list[0]
      
      car2=car_type1.get_rect()
      car2.x=(916-xpos2)%1516-200
      car2.y= lane_list[0]

      car3=car_type1.get_rect()
      car3.x=(1116-xpos2)%1516-200
      car3.y= lane_list[0]

      car4=car_type1.get_rect()
      car4.x=(1316-xpos2)%1516-200
      car4.y= lane_list[0]

      car5=car_type1.get_rect()
      car5.x=(1516-xpos2)%1516-200
      car5.y= lane_list[0]

      #Lane 2
      #First and Second=Traveldistance, Third=startpos
      car6=car_type2.get_rect()
      car6.x=(700+xpos2)%700-100
      car6.y= lane_list[1]
      
      car7=car_type2.get_rect()
      car7.x=(900+xpos2)%900-300
      car7.y= lane_list[1]

      car8=car_type2.get_rect()
      car8.x=(1100+xpos2)%1100-500
      car8.y= lane_list[1]

      car9=car_type2.get_rect()
      car9.x=(1300+xpos2)%1300-700
      car9.y= lane_list[1]

      car10=car_type2.get_rect()
      car10.x=(1500+xpos2)%1500-900
      car10.y= lane_list[1]

      car11=car_type2.get_rect()
      car11.x=(1700+xpos2)%1500-1100
      car11.y= lane_list[1]

      car12=car_type2.get_rect()
      car12.x=(1900+xpos2)%1500-1300
      car12.y= lane_list[1]

      #Lane 3
      #First=startpos, second=biggeststart, third=distance
      car13=car_type3.get_rect()
      car13.x=(900-xpos1)%2150-250
      car13.y= lane_list[2]

      car14=car_type3.get_rect()
      car14.x=(1150-xpos1)%2150-170
      car14.y= lane_list[2]

      car15=car_type3.get_rect()
      car15.x=(1400-xpos1)%2150-170
      car15.y= lane_list[2]

      car16=car_type3.get_rect()
      car16.x=(1650-xpos1)%2150-170
      car16.y= lane_list[2]

      car17=car_type3.get_rect()
      car17.x=(1900-xpos1)%2150-170
      car17.y= lane_list[2]

      car18=car_type3.get_rect()
      car18.x=(2150-xpos1)%2150-170
      car18.y= lane_list[2]

      #Lane 4
      #First=startpos, second=biggeststart, third=distance
      car19=car_type3.get_rect()
      car19.x=(700-xpos3)%2230-170
      car19.y= lane_list[3]

      car20=car_type3.get_rect()
      car20.x=(870-xpos3)%2230-170
      car20.y= lane_list[3]

      car21=car_type3.get_rect()
      car21.x=(1040-xpos3)%2230-170
      car21.y= lane_list[3]

      car22=car_type3.get_rect()
      car22.x=(1210-xpos3)%2150-170
      car22.y= lane_list[3]

      car23=car_type3.get_rect()
      car23.x=(1380-xpos3)%2150-170
      car23.y= lane_list[3]

      car24=car_type3.get_rect()
      car24.x=(1550-xpos3)%2230-170
      car24.y= lane_list[3]

      car25=car_type3.get_rect()
      car25.x=(1720-xpos3)%2230-170
      car25.y= lane_list[3]

      car26=car_type3.get_rect()
      car26.x=(1890-xpos3)%2230-170
      car26.y= lane_list[3]

      car27=car_type3.get_rect()
      car27.x=(2060-xpos3)%2230-170
      car27.y= lane_list[3]

      car28=car_type3.get_rect()
      car28.x=(2230-xpos3)%2230-170
      car28.y= lane_list[3]

      #Lane 5 (Water1)
      #First=startpos, second=biggeststart, third=distance
      log1=log_type1.get_rect()
      log1.x=(1000-xpos1)%1900-450
      log1.y= lane_list[4]

      log2=log_type1.get_rect()
      log2.x=(1450-xpos1)%1900-450
      log2.y= lane_list[4]

      log3=log_type1.get_rect()
      log3.x=(1900-xpos1)%1900-450
      log3.y= lane_list[4]

      #Lane 6 (Water2)
      #First and Second=Traveldistance, Third=startpos
      log4=log_type2.get_rect()
      log4.x=(900+xpos1)%900-300
      log4.y= lane_list[5]

      log5=log_type2.get_rect()
      log5.x=(1350+xpos1)%1350-750
      log5.y= lane_list[5]

      log6=log_type2.get_rect()
      log6.x=(1800+xpos1)%1800-1200
      log6.y= lane_list[5]

      log7=log_type2.get_rect()
      log7.x=(2250+xpos1)%2250-1650
      log7.y= lane_list[5]

      #Lane 7 (Water3)
      #First=startpos, second=biggeststart, third=distance
      log8=log_type2.get_rect()
      log8.x=(1200-xpos1)%1800-300
      log8.y= lane_list[6]

      log9=log_type2.get_rect()
      log9.x=(1500-xpos1)%1800-300
      log9.y= lane_list[6]

      log10=log_type2.get_rect()
      log10.x=(1800-xpos1)%1800-300
      log10.y= lane_list[6]
      

      #Log and Car list
      car_list=[car1,car2,car3,car4,car5,car6,car7,car8,car9,car10,car11,car12,car13,car14,car15,car16,car17,car18,car19,car20,car21,car22,car23,car24,car25,car26,car27,car28]
      log_list=[log1,log2,log3,log4,log5,log6,log7,log8,log9,log10]
      


      frog=frog.subsurface((9+(shift%200),0,40,40))
#converted frog subsurface
      frog_rect=frog.get_rect()
#coordinates for the new rect
      frog_rect.x=258+deltax
      frog_rect.y=590+deltay
      
      # Draw.

      screen.blit(background_image,[0,0])







#when you blit the converted image the format is (loaded_image,converted_image)
                     
      #Lane 1
      screen.blit(car_type1,car1)
      screen.blit(car_type1,car2)
      screen.blit(car_type1,car3)
      screen.blit(car_type1,car4)
      screen.blit(car_type1,car5)

      #Lane 2
      screen.blit(car_type2,car6)
      screen.blit(car_type2,car7)
      screen.blit(car_type2,car8)
      screen.blit(car_type2,car9)
      screen.blit(car_type2,car10)
      screen.blit(car_type2,car11)
      screen.blit(car_type2,car12)

      #Lane 3
      screen.blit(car_type3,car13)
      screen.blit(car_type3,car14)
      screen.blit(car_type3,car15)
      screen.blit(car_type3,car16)
      screen.blit(car_type3,car17)
      screen.blit(car_type3,car18)

      #Lane 4
      screen.blit(car_type4,car19)
      screen.blit(car_type4,car20)
      screen.blit(car_type4,car21)
      screen.blit(car_type4,car22)
      screen.blit(car_type4,car23)
      screen.blit(car_type4,car24)
      screen.blit(car_type4,car25)
      screen.blit(car_type4,car26)
      screen.blit(car_type4,car27)
      screen.blit(car_type4,car28)

      #lane 5 (Water1)
      screen.blit(log_type1,log1)
      screen.blit(log_type1,log2)
      screen.blit(log_type1,log3)

      #Lane 6 (Water2)
      screen.blit(log_type2,log4)
      screen.blit(log_type2,log5)
      screen.blit(log_type2,log6)
      screen.blit(log_type2,log7)

      #Lane 7 (Water3)
      screen.blit(log_type2,log8)
      

      xpos1+= speed1
      xpos2+= speed2
      xpos3+= speed3



      screen.blit(frog,frog_rect)

      collide=frog_rect.collidelist(car_list)

      if collide == 0:
          deltax=deltax-deltax
          deltay=deltay-deltay

      
      
      pygame.display.flip()
      fpsClock.tick(fps)

main()

