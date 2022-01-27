from sys import exit

import pygame as game

game.init()

BLACK = (0, 0, 0)
CAPTION = "Solaris"
DARK_LIME_GREEN1 = (0, 137, 0)  # dark lime green, first shade
DARK_LIME_GREEN2 = (0, 177, 0)  # dark lime green, second shade
MODE_HEIGHT = 450
MODE_WIDTH = 850
PLAYER_HEIGHT = 80
PLAYER_WIDTH = 80
PURE_LIME_GREEN = (0, 235, 0)  # pure lime green
VERY_DARK_LIME_GREEN1 = (0, 39, 0)  # very dark lime green, first shade
VERY_DARK_LIME_GREEN2 = (0, 98, 0)  # very dark lime green, second shade

# End initial variable assignments.

game.display.set_caption(CAPTION)
screen = game.display.set_mode((MODE_WIDTH, MODE_HEIGHT))

exit_surface = game.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
exit_surface.fill(BLACK)


# Nice class to hold a wall rect
class Wall(object):
    """
    """

    def __init__(self):
        """
        """

        WALL1_ACROSS_HEIGHT = 16
        WALL1_ACROSS_WIDTH = 368
        WALL1_DOWN_HEIGHT = 656
        WALL1_DOWN_WIDTH = 16
        WALL2_ACROSS_HEIGHT = 16
        WALL2_ACROSS_WIDTH = 576
        WALL2_DOWN_HEIGHT = 112
        WALL2_DOWN_WIDTH = 16

        self.rect1 = game.Rect(
            16, 16, WALL1_ACROSS_WIDTH, WALL1_ACROSS_HEIGHT)
        self.rect2 = game.Rect(16, 16, WALL1_DOWN_WIDTH, WALL1_DOWN_HEIGHT)
        self.rect3 = game.Rect(368, 16, WALL2_DOWN_WIDTH, WALL2_DOWN_HEIGHT)
        self.rect4 = game.Rect(
            368, 112, WALL2_ACROSS_WIDTH, WALL2_ACROSS_HEIGHT)


wall = Wall()


class Player(object):
    """
    """

    def __init__(self):
        """
        """

        self.rect = game.Rect(225, 425, PLAYER_WIDTH, PLAYER_HEIGHT)

    def go(self, x, y):
        """
        """

        if x != 0:
            self.single_axis_go(x, 0)

        if y != 0:
            self.single_axis_go(0, y)

    def single_axis_go(self, x, y):
        """
        """

        self.rect.x += x
        self.rect.y += y

        if self.rect.colliderect(wall.rect1):
            self.wall1_collisions(x, y)

        if self.rect.colliderect(wall.rect2):
            self.wall2_collisions(x, y)

        if self.rect.colliderect(wall.rect3):
            self.wall3_collisions(x, y)

        if self.rect.colliderect(wall.rect4):
            self.wall3_collisions(x, y)

    def wall1_collisions(self, x, y):
        """
        """

        if x > 0:  # Going right; Hit left side of wall
            self.rect.right = wall.rect1.left

        if x < 0:  # Going left; Hit right side of wall
            self.rect.left = wall.rect1.right

        if y > 0:  # Going down; Hit top side of wall
            self.rect.bottom = wall.rect1.top

        if y < 0:  # Going up; Hit bottom side of wall
            self.rect.top = wall.rect1.bottom

    def wall2_collisions(self, x, y):
        """
        """

        if x > 0:  # Going right; Hit left side of wall
            self.rect.right = wall.rect2.left

        if x < 0:  # Going left; Hit right side of wall
            self.rect.left = wall.rect2.right

        if y > 0:  # Going down; Hit top side of wall
            self.rect.bottom = wall.rect2.top

        if y < 0:  # Going up; Hit bottom side of wall
            self.rect.top = wall.rect2.bottom

    def wall3_collisions(self, x, y):
        """
        """

        if x > 0:  # Going right; Hit left side of wall
            self.rect.right = wall.rect3.left

        if x < 0:  # Going left; Hit right side of wall
            self.rect.left = wall.rect3.right

        if y > 0:  # Going down; Hit top side of wall
            self.rect.bottom = wall.rect3.top

        if y < 0:  # Going up; Hit bottom side of wall
            self.rect.top = wall.rect3.bottom

    def wall4_collisions(self, x, y):
        """
        """

        if x > 0:  # Going right; Hit left side of wall
            self.rect.right = wall.rect4.left

        if x < 0:  # Going left; Hit right side of wall
            self.rect.left = wall.rect4.right

        if y > 0:  # Going down; Hit top side of wall
            self.rect.bottom = wall.rect4.top

        if y < 0:  # Going up; Hit bottom side of wall
            self.rect.top = wall.rect4.bottom


player = Player()


def event_loop():
    """
    """

    for event in game.event.get():

        if event.type == game.QUIT:
            game.quit()
            exit()


def graphics_renderer():
    """
    """

    screen.fill(PURE_LIME_GREEN)
    maze_builder()
    game.draw.rect(screen, VERY_DARK_LIME_GREEN1, player.rect)
    game.display.flip()


def main_loop():
    """
    """

    clock = game.time.Clock()

    while True:
        # Process inputs
        player_input()
        event_loop()
        # Update game world
        # Generate outputs
        graphics_renderer()
        clock.tick(60)


def maze_builder():
    """
    """

    game.draw.rect(screen, DARK_LIME_GREEN1, wall.rect1)
    game.draw.rect(screen, DARK_LIME_GREEN1, wall.rect2)
    game.draw.rect(screen, DARK_LIME_GREEN1, wall.rect3)
    game.draw.rect(screen, DARK_LIME_GREEN1, wall.rect4)


def player_input():
    """
    """

    MOVING_SPEED = 2.05
    key = game.key.get_pressed()

    if key[game.K_DOWN]:
        player.go(0, MOVING_SPEED)

    if key[game.K_LEFT]:
        player.go(-MOVING_SPEED, 0)

    if key[game.K_RIGHT]:
        player.go(MOVING_SPEED, 0)

    if key[game.K_UP]:
        player.go(0, -MOVING_SPEED)


if __name__ == "__main__":
    main_loop()
