import pygame as pg


class Ship:
    """The spaceship(player)."""
    
    def __init__(self,screen,ai_settings):
        """Initialize spaceship amd set it's default position."""
        self.screen = screen 
        
        """Load imgae and image rect."""
        self.image = pg.image.load('images/ship.bmp').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        """Put ship at bottom center of screen."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom# - 500
        self.ai_settings = ai_settings
        #set speed
        #self.speed = 10 * ai_settings.ship_speed_factor
        self.centerx = float(self.rect.centerx)
        #movement flags
        self.move_left = False
        self.move_right = False
        
        
    def blitme(self):
        """Display ship."""
        #self.move_ship()
        self.screen.blit(self.image,self.rect)
        
    def move_ship(self):
        if self.move_right:
            self.move_ship_right()
            """ and self.rect.right + self.ai_settings.ship_speed_factor <= self.screen_rect.right:
            self.centerx = self.rect.centerx + self.ai_settings.ship_speed_factor
            self.rect.centerx = self.centerx"""
        if self.move_left:
             self.move_ship_left()
             """and self.rect.left - self.ai_settings.ship_speed_factor >= self.screen_rect.left :
            self.centerx = self.rect.centerx - self.ai_settings.ship_speed_factor
            self.rect.centerx = self.centerx"""
            
    def move_ship_right(self):
        if self.rect.right + self.ai_settings.ship_speed_factor <= self.screen_rect.right:
            self.centerx = self.rect.centerx + self.ai_settings.ship_speed_factor
            self.rect.centerx = self.centerx 
            
    def move_ship_left(self):
        if self.rect.left - self.ai_settings.ship_speed_factor >= self.screen_rect.left :
            self.centerx = self.rect.centerx - self.ai_settings.ship_speed_factor
            self.rect.centerx = self.centerx       