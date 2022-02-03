import pygame as game

game.init()

font = game.font.Font(None, 30)


def debug(info, y=10, x=10):
    """
    """

    display_surface = game.display.get_surface()
    debug_surface = font.render(str(info), True, "White")
    debug_rectangle = debug_surface.get_rect(topleft=(x, y))
    game.draw.rect(display_surface, "Black", debug_rectangle)
    display_surface.blit(debug_surface, debug_rectangle)
