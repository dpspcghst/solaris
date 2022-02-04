from sys import exit

import pygame as game

from debug import debug
from level import Level
from player import Player
from settings import *

BLACK = (0, 0, 0)
DARK_LIME_GREEN2 = (0, 177, 0)  # dark lime green, second shade
horizontal_scroll = 0
vertical_scroll = 0
VERY_DARK_LIME_GREEN1 = (0, 39, 0)  # very dark lime green, first shade
VERY_DARK_LIME_GREEN2 = (0, 98, 0)  # very dark lime green, second shade


class Game():
    """
    """

    def __init__(self):
        """
        General setup.
        """

        game.init()

        self.screen = game.display.set_mode((MODE_WIDTH, MODE_HEIGHT))
        self.screen.fill(PURE_LIME_GREEN)
        game.display.set_caption("Solaris")
        self.clock = game.time.Clock()

        self.level = Level()

    def get_clock(self):
        """
        """

        return self.clock

    def get_level(self):
        """
        """

        return self.level

    def get_screen(self):
        """
        """

        return self.screen

    def render_graphics(self, player, walls):
        """
        """

        # Background
        self.screen.fill(PURE_LIME_GREEN)

        # Build maze.
        build_maze(self.screen, walls)

        debug("Fix")

        # Build player.
        game.draw.rect(self.screen, player.get_color(), player.get_body())

        # Flip display.
        game.display.flip()

        game.display.update()

    def run(self):
        """
        """

        player = Player(
            color=VERY_DARK_LIME_GREEN1,
            height=PLAYER_HEIGHT,
            pos_x=225,
            pos_y=225,
            width=PLAYER_WIDTH
        )
        walls = get_walls()

        while True:
            # Process inputs
            player_input(player, walls)
            loop_events()
            # Update game world
            # Generate outputs
            self.render_graphics(player, walls)
            self.level.run()
            self.clock.tick(FPS)


class Item():
    """
    """

    body = None

    color = None

    height = 0
    width = 0

    pos_x = 0
    pos_y = 0

    def __init__(self, color, height, pos_x, pos_y, width):
        """
        """

        self.color = color

        self.height = height
        self.width = width

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.body = game.Rect(
            self.pos_x, self.pos_y,
            self.width, self.height
        )

    def get_body(self):
        """
        """

        return self.body

    def get_color(self):
        """
        """

        return self.color

    def get_height(self):
        """
        """

        return self.height

    def get_pos_x(self):
        """
        """

        return self.pos_x

    def get_pos_y(self):
        """
        """

        return self.pos_y

    def get_width(self):
        """
        """

        return self.width

    def rebuild_body(self):
        """
        """

        self.body = game.Rect(
            self.pos_x, self.pos_y,
            self.width, self.height
        )

    def set_color(self, color):
        """
        """

        self.color = color

    def set_height(self, height):
        """
        """

        self.height = height

    def set_pos_x(self, pos_x):
        """
        """

        self.pos_x = pos_x

    def set_pos_y(self, pos_y):
        """
        """

        self.pos_y = pos_y

    def set_width(self, width):
        """
        """

        self.width = width


class Maze():
    """
    """

    def __init__(self):
        """
        """

        pass


class Wall():
    """
    Nice class to hold a wall rect.
    """

    body = None

    color = None
    name = ""

    height = 0
    width = 0

    pos_x = 0
    pos_y = 0

    def __init__(self, color, height, name, pos_x, pos_y, width):
        """
        """

        self.color = color
        self.name = name

        self.height = height
        self.width = width

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.body = game.Rect(
            self.pos_x, self.pos_y,
            self.width, self.height
        )

    def __str__(self):
        """
        """

        return f"{self.name}"

    def get_body(self):
        """
        """

        return self.body

    def get_color(self):
        """
        """

        return self.color

    def get_height(self):
        """
        """

        return self.height

    def get_pos_x(self):
        """
        """

        return self.pos_x

    def get_pos_y(self):
        """
        """

        return self.pos_y

    def get_width(self):
        """
        """

        return self.width

    def rebuild_body(self):
        """
        """

        self.body = game.Rect(
            self.pos_x, self.pos_y,
            self.width, self.height
        )

    def set_color(self, color):
        """
        """

        self.color = color

    def set_height(self, height):
        """
        """

        self.height = height

    def set_pos_x(self, pos_x):
        """
        """

        self.pos_x = pos_x

    def set_pos_y(self, pos_y):
        """
        """

        self.pos_y = pos_y

    def set_width(self, width):
        """
        """

        self.width = width


def build_maze(screen, walls):
    """
    """

    for wall in walls:
        game.draw.rect(screen, wall.get_color(), wall.get_body())


def get_walls():
    """
    Lengthen walls 13 and 14 until they meet. Move walls 9 and 10 to the right
    by 16 pixels.
    """

    walls = []

    wall_1 = Wall(
        color=DARK_LIME_GREEN1,
        height=176,
        name="One",
        pos_x=0 - horizontal_scroll,
        pos_y=0 - vertical_scroll,
        width=16
    )

    wall_2 = Wall(
        color=DARK_LIME_GREEN1,
        height=16,
        name="Two",
        pos_x=0 - horizontal_scroll,
        pos_y=0 - vertical_scroll,
        width=144
    )

    wall_3 = Wall(
        color=DARK_LIME_GREEN1,
        height=48,
        name="Three",
        pos_x=128 - horizontal_scroll,
        pos_y=0 - vertical_scroll,
        width=16
    )

    wall_4 = Wall(
        color=DARK_LIME_GREEN1,
        height=16,
        name="Four",
        pos_x=128 - horizontal_scroll,
        pos_y=32 - vertical_scroll,
        width=272
    )

    wall_5 = Wall(
        color=DARK_LIME_GREEN1,
        height=16,
        name="Five",
        pos_x=128 - horizontal_scroll,
        pos_y=96 - vertical_scroll,
        width=304
    )

    wall_6 = Wall(
        color=DARK_LIME_GREEN1,
        height=208,
        name="Six",
        pos_x=128 - horizontal_scroll,
        pos_y=112 - vertical_scroll,
        width=16
    )

    wall_7 = Wall(
        color=DARK_LIME_GREEN1,
        height=16,
        name="Seven",
        pos_x=64 - horizontal_scroll,
        pos_y=224 - vertical_scroll,
        width=80
    )

    wall_8 = Wall(
        color=DARK_LIME_GREEN1,
        height=80,
        name="Eight",
        pos_x=64 - horizontal_scroll,
        pos_y=224 - vertical_scroll,
        width=16
    )

    wall_9 = Wall(
        color=DARK_LIME_GREEN1,
        height=192,
        name="Nine",
        pos_x=432 - horizontal_scroll,
        pos_y=96 - vertical_scroll,
        width=16
    )

    wall_10 = Wall(
        color=DARK_LIME_GREEN1,
        height=16,
        name="Ten",
        pos_x=400 - horizontal_scroll,
        pos_y=288 - vertical_scroll,
        width=80
    )

    wall_11 = Wall(
        color=DARK_LIME_GREEN1,
        height=16,
        name="Eleven",
        pos_x=128 - horizontal_scroll,
        pos_y=160 - vertical_scroll,
        width=80
    )

    wall_12 = Wall(
        color=DARK_LIME_GREEN1,
        height=16,
        name="Twelve",
        pos_x=256 - horizontal_scroll,
        pos_y=160 - vertical_scroll,
        width=80
    )

    wall_13 = Wall(
        color=DARK_LIME_GREEN1,
        height=16,
        name="Thirteen",
        pos_x=144 - horizontal_scroll,
        pos_y=288 - vertical_scroll,
        width=208
    )

    wall_14 = Wall(
        color=DARK_LIME_GREEN1,
        height=128,
        name="Fourteen",
        pos_x=336 - horizontal_scroll,
        pos_y=160 - vertical_scroll,
        width=16
    )

    walls.append(wall_1)
    walls.append(wall_2)
    walls.append(wall_3)
    walls.append(wall_4)
    walls.append(wall_5)
    walls.append(wall_6)
    walls.append(wall_7)
    walls.append(wall_8)
    walls.append(wall_9)
    walls.append(wall_10)
    walls.append(wall_11)
    walls.append(wall_12)
    walls.append(wall_13)
    walls.append(wall_14)

    return walls


def loop_events():
    """
    """

    for event in game.event.get():

        if event.type == game.QUIT:
            game.quit()
            exit()


def player_input(player, walls):
    """
    """

    MOVING_SPEED = 1  # This number cannot be a negative float.
    key = game.key.get_pressed()
    # joysticks = game.joystick.get_count()

    if key[game.K_DOWN]:
        player.go(walls, 0, MOVING_SPEED)

    if key[game.K_LEFT]:
        player.go(walls, -MOVING_SPEED, 0)

    if key[game.K_RIGHT]:
        player.go(walls, MOVING_SPEED, 0)

    if key[game.K_UP]:
        player.go(walls, 0, -MOVING_SPEED)


if __name__ == "__main__":
    game = Game()
    game.run()
