import pygame as game

from settings import *


class Level():
    """
    """

    def __init__(self):
        """
        """

        # Get the display surface.
        self.display_surface = game.display.get_surface()

        # Sprite group setup.
        self.visible_sprites = game.sprite.Group()
        self.obstacle_sprites = game.sprite.Group()

        # Sprite setup.
        self.create_map()

    def create_map(self):
        """
        """

        for row in WORLD_MAP:
            print(row)

    def get_display_surface(self):
        """
        """

        return self.display_surface

    def get_obstacle_sprites(self):
        """
        """

        return self.obstacle_sprites

    def get_visible_sprites(self):
        """
        """

        return self.visible_sprites

    def run(self):
        """
        """

        pass
