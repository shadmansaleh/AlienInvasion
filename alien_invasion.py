"""Alien invasion(Main file)."""
import pygame as pg
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_funcrions as gf


def run_game():
    """Main function"""
    '# initialize game and create screen object'
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode(ai_settings.screen_size,
                                 pg.SCALED | pg.HWSURFACE)
    pg.display.set_caption("Alien invasion")
    '# ai_settings.load_background()'
    '#make a ship'
    ship = Ship(screen, ai_settings)

    '#Make bulets group'
    bullets = Group()
    '#make a clock to comtrol fps.'
    clock = pg.time.Clock()

    while True:
        '#game loop'
        clock.tick(ai_settings.fps)
        '#check for events'
        gf.check_event(ai_settings, screen, ship, bullets)
        gf.update_bullets(ai_settings, bullets)
        '#update ship position'
        ship.move_ship()
        '#update display'
        gf.update_screen(ai_settings, ship, screen, bullets)


run_game()
