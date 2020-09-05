"""Settings for game."""
import pygame as pg


class Settings:
    def __init__(self):
        """Initiate settings."""
        self.fps = 60
        self.screen_size = 360, 720
        '# self.screen_width = 768'
        '# self.screen_height = 415'
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 30 / self.fps * 12

        '# Bulet settings'
        self.bullet_speed_factor = 30 / self.fps * 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.max_available_bullets = 5
        self.available_bullets = self.max_available_bullets
        self.bullet_delay = 0
        self.reload_delay = int(self.fps * 1.5)
        self.shoting_delay = int(self.fps * 0.2)
        '# self.bullets_allowed = 5'

    def load_background(self):
        self.background = pg.image.load('images/seamless-1315326_1280.jpg'
                                        ).convert()

