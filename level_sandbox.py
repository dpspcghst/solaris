import pygame as game


MODE_WIDTH = 850
MODE_HEIGHT = 450


class Wall(object):
    """
    """

    def __init__(self, pos):
        """
        """

        walls.append(self)
        self.rect = game.Rect(pos[0], pos[1], 16, 16)


game.init()

# Set up the display
screen = game.display.set_mode((MODE_WIDTH, MODE_HEIGHT))

clock = game.time.Clock()
walls = []  # List to hold the walls

# Holds the level layout in a list of strings.
level_one = [
    "                                             ",
    " zwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwowwwwwwwwwwww",
    " w                                          w",
    " w                                          w",
    " w                                          w",
    " w                                          w",
    " w                                          w",
    " w                                          w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " o",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " t",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w",
    " w"
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level_one:
    for col in row:
        if col == "w" or col == "z" or col == "o" or col == "t":
            Wall((x, y))
        if col == "E":
            # end_rect = game.Rect(x, y, 16, 16)
            pass
        x += 16
    y += 16
    x = 0

running = True
while running:

    clock.tick(60)

    for e in game.event.get():
        if e.type == game.QUIT:
            running = False
        if e.type == game.KEYDOWN and e.key == game.K_ESCAPE:
            running = False

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        game.draw.rect(screen, (255, 255, 255), wall.rect)
    game.display.flip()

