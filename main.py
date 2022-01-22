from sys import exit

import pygame as game

game.init()

dark_lime_green1 = (0, 137, 0)  # dark lime green, first shade
dark_lime_green2 = (0, 177, 0)  # dark lime green, second shade
height = 450
player_height = 25
player_width = 13
pure_lime_green = (0, 235, 0)  # pure lime green
very_dark_lime_green1 = (0, 39, 0)  # very dark lime green, first shade
very_dark_lime_green2 = (0, 98, 0)  # very dark lime green, second shade
wall_height = 125
wall_width = 13
width = 850

screen = game.display.set_mode((width, height))
game.display.set_caption("Solaris")

player_surface = game.Surface((player_width, player_height))
player_surface.fill(very_dark_lime_green1)
wall_surface1 = game.Surface((wall_width, wall_height))
wall_surface1.fill(dark_lime_green1)
wall_surface2 = game.Surface((wall_width, wall_height))
wall_surface2.fill(dark_lime_green1)

clock = game.time.Clock()


def event_loop():
    """
    """

    for event in game.event.get():

        if event.type == game.QUIT:
            game.quit()
            exit()


def graphics_renderer(image1, image2, image3):
    """
    """

    screen.fill(pure_lime_green)
    screen.blit(player_surface, (image1.x, image1.y))
    screen.blit(wall_surface1, (image2.x, image2.y))
    screen.blit(wall_surface2, (image3.x, image3.y))


def player_input(person):
    """
    """

    keys_pressed = game.key.get_pressed()

    if keys_pressed[game.K_DOWN]:

        if keys_pressed[game.K_LSHIFT]:
            person.y += 2.85

        else:
            person.y += 1.25

    if keys_pressed[game.K_LEFT]:

        if keys_pressed[game.K_LSHIFT]:
            person.x -= 2.85

        else:
            person.x -= 1.25

    if keys_pressed[game.K_RIGHT]:

        if keys_pressed[game.K_LSHIFT]:
            person.x += 2.85

        else:
            person.x += 1.25

    if keys_pressed[game.K_UP]:

        if keys_pressed[game.K_LSHIFT]:
            person.y -= 2.85

        else:
            person.y -= 1.25


def test_function(rect1, rect2, rect3):
    """
    """

    if rect1.colliderect(rect2) or rect1.colliderect(rect3):
        print("Wall!")

    else:
        print("No Wall!")


def main_loop():
    """
    """

    player_rectangle = game.Rect(53, 53, player_width, player_height)
    wall_rectangle1 = game.Rect(125, 125, wall_width, wall_height)
    wall_rectangle2 = game.Rect(250, 125, wall_width, wall_height)

    while True:
        event_loop()
        player_input(player_rectangle)
        graphics_renderer(player_rectangle, wall_rectangle1, wall_rectangle2)
        test_function(player_rectangle, wall_rectangle1, wall_rectangle2)
        game.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main_loop()
