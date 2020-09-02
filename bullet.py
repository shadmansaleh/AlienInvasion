import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets."""
    def __init__(self,ai_settings,screen,ship):
        """Create a bullet at ships current position."""
        super().__init__()
        self.screen = screen
        
        #Create a bullet rect
        self.rect = pg.Rect(ship.rect.centerx,ship.rect.top,ai_settings.bullet_width,ai_settings.bullet_height)
        
        #Save bullet position for easy accesss as decimal value
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """move bullet up the screen."""
        #update decimal position of the bullet
        self.y -= self.speed_factor
        #update rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw bullet on the screen"""
        pg.draw.rect(self.screen,self.color,self.rect)
