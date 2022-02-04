import pygame as game

from settings import *


class Tile(game.sprite.Sprite):
    """
    """

    def __init__(self, groups, pos):
        """
        """

        super().__init__(groups)
        self.image = game.Surface((TILE_WIDTH, TILE_HEIGHT))
        self.image.fill(DARK_LIME_GREEN1)
        self.rect = self.image.get_rect(topleft=pos)

    def get_image(self):
        """
        """

        return self.image

    def get_rect(self):
        """
        """

        return self.rect
