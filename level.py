import pygame as game

from player import Player
from settings import *
from tile import Tile


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

        for row_index, row in enumerate(WORLD_MAP):

            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == "w":
                    Tile([self.obstacle_sprites, self.visible_sprites], (x, y))
                if column == "p":
                    Player([self.visible_sprites], (x, y))

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

        self.visible_sprites.draw(self.display_surface)
