from sys import exit

import pygame as game

game.init()

dark_lime_green1 = (0, 137, 0)  # dark lime green, first shade
dark_lime_green2 = (0, 177, 0)  # dark lime green, second shade
height = 450
player_height = 25
player_width = 13
pure_lime_green = (0, 235, 0)  # pure lime green
running_speed = 2.85
very_dark_lime_green1 = (0, 39, 0)  # very dark lime green, first shade
very_dark_lime_green2 = (0, 98, 0)  # very dark lime green, second shade
walking_speed = 1.25
wall_height = 125
wall_width = 13
width = 850

screen = game.display.set_mode((width, height))
game.display.set_caption("Solaris")

player_rectangle = game.Rect(53, 53, player_width, player_height)
wall_rectangle1 = game.Rect(125, 125, wall_width, wall_height)
wall_rectangle2 = game.Rect(250, 125, wall_width, wall_height)

player_surface = game.Surface((player_width, player_height))
player_surface.fill(very_dark_lime_green1)
wall_surface1 = game.Surface((wall_width, wall_height))
wall_surface1.fill(dark_lime_green1)
wall_surface2 = game.Surface((wall_width, wall_height))
wall_surface2.fill(dark_lime_green1)

clock = game.time.Clock()


def collision_detection(rect1, rect2, rect3):
    """
    """

    if rect1.colliderect(rect2):

        if player_rectangle.x > 0:  # Moving right; Hit left side of wall
            player_rectangle.right = wall_rectangle1.left

        if player_rectangle.x < 0:  # Moving left; Hit right side of wall
            player_rectangle.left = wall_rectangle1.right

        if player_rectangle.y > 0:  # Moving down; Hit top side of wall
            player_rectangle.bottom = wall_rectangle1.top

        if player_rectangle.y < 0:  # Moving up; Hit bottom side of wall
            player_rectangle.top = wall_rectangle1.bottom

    if rect1.colliderect(rect3):

        if player_rectangle.x > 0:  # Moving right; Hit left side of wall
            player_rectangle.right = wall_rectangle2.left

        if player_rectangle.x < 0:  # Moving left; Hit right side of wall
            player_rectangle.left = wall_rectangle2.right

        if player_rectangle.y > 0:  # Moving down; Hit top side of wall
            player_rectangle.bottom = wall_rectangle2.top

        if player_rectangle.y < 0:  # Moving up; Hit bottom side of wall
            player_rectangle.top = wall_rectangle2.bottom


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


def graphics_renderer(image1, image2, image3):
    """
    """

    screen.fill(pure_lime_green)
    screen.blit(player_surface, (image1.x, image1.y))
    screen.blit(wall_surface1, (image2.x, image2.y))
    screen.blit(wall_surface2, (image3.x, image3.y))


def player_input(rectangle):
    """
    """

    keys_pressed = game.key.get_pressed()

    if keys_pressed[game.K_DOWN]:

        if keys_pressed[game.K_LSHIFT]:
            go(0, running_speed)

        else:
            go(0, walking_speed)

    if keys_pressed[game.K_LEFT]:

        if keys_pressed[game.K_LSHIFT]:
            go(-running_speed, 0)

        else:
            go(-walking_speed, 0)

    if keys_pressed[game.K_RIGHT]:

        if keys_pressed[game.K_LSHIFT]:
            go(running_speed, 0)

        else:
            go(walking_speed, 0)

    if keys_pressed[game.K_UP]:

        if keys_pressed[game.K_LSHIFT]:
            go(0, -running_speed)

        else:
            go(0, -walking_speed)


def main_loop():
    """
    """

    while True:
        event_loop()
        player_input(player_rectangle)
        graphics_renderer(player_rectangle, wall_rectangle1, wall_rectangle2)
        # collision_detection(player_rectangle, wall_rectangle1, wall_rectangle2)
        game.display.update()
        clock.tick(60)


def single_axis_go(x, y):
    """
    """

    player_rectangle.x += x
    player_rectangle.y += y

    if player_rectangle.colliderect(wall_rectangle1):

        if x > 0:  # Moving right; Hit left side of wall
            player_rectangle.right = wall_rectangle1.left

        if x < 0:  # Moving left; Hit right side of wall
            player_rectangle.left = wall_rectangle1.right

        if y > 0:  # Moving down; Hit top side of wall
            player_rectangle.bottom = wall_rectangle1.top

        if y < 0:  # Moving up; Hit bottom side of wall
            player_rectangle.top = wall_rectangle1.bottom

    if player_rectangle.colliderect(wall_rectangle2):

        if x > 0:  # Moving right; Hit left side of wall
            player_rectangle.right = wall_rectangle2.left

        if x < 0:  # Moving left; Hit right side of wall
            player_rectangle.left = wall_rectangle2.right

        if y > 0:  # Moving down; Hit top side of wall
            player_rectangle.bottom = wall_rectangle2.top

        if y < 0:  # Moving up; Hit bottom side of wall
            player_rectangle.top = wall_rectangle2.bottom


if __name__ == "__main__":
    main_loop()
