"""This file is to store various functions for yhe game"""
import sys
import pygame as pg
from bullet import Bullet

def check_event(ai_settings,screen,ship,bullets):
    """look for keyboard and mouse events"""
    for ev in pg.event.get():
        #check for exit
        if ev.type == pg.QUIT:
            sys.exit()
        #check for key presses
        elif ev.type == pg.KEYDOWN:
            key_down_events(ev,ai_settings,screen,ship,bullets)
#        elif ev.type == pg.KEYUP:
#            key_up_events(ev,ship)
        elif ev.type == pg.FINGERDOWN:
            finger_down_events(ev,ai_settings,screen,ship,bullets)
        elif ev.type == pg.FINGERUP:
            finger_up_events(ev,ship)                                      
            
def update_screen(ai_settings,ship,screen,bullets):
    """Update screen."""
    #display background
    #update_background(ai_settings,screen)
    screen.fill(ai_settings.bg_color)
    #draw ship
    ship.blitme()
    #Draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #make most recently drawn screen visible
    pg.display.flip()

#Update bullets
def update_bullets(ai_settings,bullets):
    #update bullets
    bullets.update()
    #remove old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
#        print(len(bullets))
    if ai_settings.bullet_delay > 0:
        ai_settings.bullet_delay -= 1


#event handling functions
def key_down_events(ev,ai_settings,screen,ship,bullets):
    #right movement
    if ev.key == pg.K_RIGHT:  
#        print("key down right")
        #ship.move_right = True
        ship.move_ship_right()
    #left movement
    elif ev.key == pg.K_LEFT:
#        print("key down left")        
        #ship.move_left = True
        ship.move_ship_left()
    elif ev.key == pg.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
"""def key_up_events(ev,ship):
    if ev.key == pg.K_RIGHT:
#        print("key up right")        
        ship.move_right = False
    elif ev.key == pg.K_LEFT:
#        print("key up left")        
        ship.move_left = False """
def finger_down_events(ev,ai_settings,screen,ship,bullets): 
    if (ev.x > 0.8):
        ship.move_right = True
    elif (ev.x < 0.2):
        ship.move_left = True
    elif ev.x > 0.2 and ev.x < 0.8:
        fire_bullet(ai_settings,screen,ship,bullets)     
def finger_up_events(ev,ship):
    if (ev.x > 0.8):
        ship.move_right = False
    elif (ev.x < 0.2):
        ship.move_left = False

def fire_bullet(ai_settings,screen,ship,bullets):
    #Create a bullets and add it to bullets
    #if(len(bullets) < ai_settings.bullet_allowed):
    if ai_settings.bullet_delay <= 0:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)  
        ai_settings.available_bullets = ai_settings.available_bullets - 1  
        if ai_settings.available_bullets <= 0:
            ai_settings.bullet_delay = ai_settings.reload_delay
            ai_settings.available_bullets = ai_settings.max_available_bullets
        else:
            ai_settings.bullet_delay = ai_settings.shoting_delay  
            
                      

#show space background
def update_background(ai_settings,screen):
    screen.blit(ai_settings.background,(0,0)) 
                  