# Research Control building structure for level design

from sys import exit

import pygame as game

game.init()

BLACK = (0, 0, 0)
CAPTION = "Solaris"
DARK_LIME_GREEN1 = (0, 137, 0)  # dark lime green, first shade
DARK_LIME_GREEN2 = (0, 177, 0)  # dark lime green, second shade
MODE_HEIGHT = 450
MODE_WIDTH = 850
player_height = 25
player_width = 13
PURE_LIME_GREEN = (0, 235, 0)  # pure lime green
VERY_DARK_LIME_GREEN1 = (0, 39, 0)  # very dark lime green, first shade
VERY_DARK_LIME_GREEN2 = (0, 98, 0)  # very dark lime green, second shade
wall_height = 125
wall_width = 13

# End initial variable assignments.

screen = game.display.set_mode((MODE_WIDTH, MODE_HEIGHT))
game.display.set_caption(CAPTION)

player_rectangle = game.Rect(53, 53, player_width, player_height)
wall_rectangle1 = game.Rect(125, 125, wall_width, wall_height)
wall_rectangle2 = game.Rect(250, 125, wall_width, wall_height)

exit_surface = game.Surface((player_width, player_height))
exit_surface.fill(BLACK)


def change_game_mode():
    """
    """

    pass


def event_loop():
    """
    """

    for event in game.event.get():

        if event.type == game.QUIT:
            game.quit()
            exit()


def go(x, y):
    """
    """

    if x != 0:
        single_axis_go(x, 0)

    if y != 0:
        single_axis_go(0, y)


def graphics_renderer():
    """
    """

    player_surface = game.Surface((player_width, player_height))
    player_surface.fill(VERY_DARK_LIME_GREEN1)
    wall_surface1 = game.Surface((wall_width, wall_height))
    wall_surface1.fill(DARK_LIME_GREEN1)
    wall_surface2 = game.Surface((wall_width, wall_height))
    wall_surface2.fill(DARK_LIME_GREEN1)

    screen.fill(PURE_LIME_GREEN)
    screen.blit(player_surface, (player_rectangle.x, player_rectangle.y))
    screen.blit(wall_surface1, (wall_rectangle1.x, wall_rectangle1.y))
    screen.blit(wall_surface2, (wall_rectangle2.x, wall_rectangle2.y))
    game.display.update()


def level_algorithm():
    """
    """

    pass


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


def music_loop():
    """
    """

    pass


def player_input():
    """
    """

    MOVING_SPEED = 2.05
    keys_pressed = game.key.get_pressed()

    if keys_pressed[game.K_DOWN]:
        go(0, MOVING_SPEED)

    if keys_pressed[game.K_LEFT]:
        go(-MOVING_SPEED, 0)

    if keys_pressed[game.K_RIGHT]:
        go(MOVING_SPEED, 0)

    if keys_pressed[game.K_UP]:
        go(0, -MOVING_SPEED)


def single_axis_go(x, y):
    """
    """

    player_rectangle.x += x
    player_rectangle.y += y

    if player_rectangle.colliderect(wall_rectangle1):
        wall1_collisions(x, y)

    if player_rectangle.colliderect(wall_rectangle2):
        wall2_collisions(x, y)


def title_screen():
    """
    """

    pass


def wall1_collisions(x, y):
    """
    """

    if x > 0:  # Going right; Hit left side of wall
        player_rectangle.right = wall_rectangle1.left

    if x < 0:  # Going left; Hit right side of wall
        player_rectangle.left = wall_rectangle1.right

    if y > 0:  # Moving down; Hit top side of wall
        player_rectangle.bottom = wall_rectangle1.top

    if y < 0:  # Moving up; Hit bottom side of wall
        player_rectangle.top = wall_rectangle1.bottom


def wall2_collisions(x, y):
    """
    Depending on the direction of the player rectangle, this function keeps
    the player from "phasing" through walls (i.e., treats the player and the
    second wall as solid objects).
    """

    if x > 0:  # Going right; Hit left side of wall
        player_rectangle.right = wall_rectangle2.left

    if x < 0:  # Going left; Hit right side of wall
        player_rectangle.left = wall_rectangle2.right

    if y > 0:  # Going down; Hit top side of wall
        player_rectangle.bottom = wall_rectangle2.top

    if y < 0:  # Going up; Hit bottom side of wall
        player_rectangle.top = wall_rectangle2.bottom


if __name__ == "__main__":
    main_loop()
