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
class Wall():
    """
    """

    body = None

    across_height = 0
    across_width = 0

    down_height = 0
    down_width = 0

    pos_x = 0
    pos_y = 0

    color = ''

    def __init__(self, width, height, pos_x, pos_y, color):
        """
        """

        self.height = height
        self.width = width

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.color = color

        self.body = game.Rect(
            self.pos_x, self.pos_y,
            self.width, self.height
        )

    def get_body(self):
        return self.body

    def rebuild_body(self):
        self.body = game.Rect(
            self.pos_x, self.pos_y,
            self.width, self.height
        )

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_pos_x(self):
        return self.pos_x

    def set_pos_x(self, pos_x):
        self.pos_x = pos_x

    def get_pos_y(self):
        return self.pos_y

    def set_pos_y(self, pos_y):
        self.pos_y = pos_y

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


class Player():
    """
    """

    body = None

    width = 0
    height = 0
    pos_x = 0
    pos_y = 0
    color = None

    def __init__(self, width, height, pos_x, pos_y, color):
        """
        """

        self.height = height
        self.width = width

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.color = color

        self.body = game.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def go(self, x, y, walls):
        """
        """

        if x != 0:
            self.single_axis_go(x, 0, walls)

        if y != 0:
            self.single_axis_go(0, y, walls)

    def single_axis_go(self, x, y, walls):
        """
        """

        self.body.x += x
        self.body.y += y

        for wall in walls:
            if self.body.colliderect(wall.get_body()):
                self.wall_collisions(x, y, wall)

    def wall_collisions(self, x, y, wall):
        """
        """

        if x > 0:  # Going right; Hit left side of wall
            self.body.right = wall.get_body().left

        if x < 0:  # Going left; Hit right side of wall
            self.body.left = wall.get_body().right

        if y > 0:  # Going down; Hit top side of wall
            self.body.bottom = wall.get_body().top

        if y < 0:  # Going up; Hit bottom side of wall
            self.body.top = wall.get_body().bottom

    def get_body(self):
        return self.body

    def rebuild_body(self):
        self.body = game.Rect(
            self.pos_x, self.pos_y,
            self.width, self.height
        )

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_pos_x(self):
        return self.pos_x

    def set_pos_x(self, pos_x):
        self.pos_x = pos_x

    def get_pos_y(self):
        return self.pos_y

    def set_pos_y(self, pos_y):
        self.pos_y = pos_y

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


def get_walls():
    walls = []

    wall_1 = Wall(
        width=368,
        height=16,
        pos_x=16,
        pos_y=16,
        color=DARK_LIME_GREEN1
    )

    wall_2 = Wall(
        width=16,
        height=656,
        pos_x=16,
        pos_y=16,
        color=DARK_LIME_GREEN1
    )

    wall_3 = Wall(
        width=16,
        height=112,
        pos_x=368,
        pos_y=16,
        color=DARK_LIME_GREEN1
    )

    wall_4 = Wall(
        width=576,
        height=16,
        pos_x=368,
        pos_y=112,
        color=DARK_LIME_GREEN1
    )

    walls.append(wall_1)
    walls.append(wall_2)
    walls.append(wall_3)
    walls.append(wall_4)

    return walls


def event_loop():
    """
    """

    for event in game.event.get():

        if event.type == game.QUIT:
            game.quit()
            exit()


def graphics_renderer(player, walls):
    """
    """

    # Background
    screen.fill(PURE_LIME_GREEN)

    # Build maze
    build_maze(screen, walls)

    # Build player
    game.draw.rect(screen, player.get_color(), player.get_body())

    # Flip display
    game.display.flip()


def main_loop():
    """
    """

    clock = game.time.Clock()

    walls = get_walls()
    player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, 225, 425, VERY_DARK_LIME_GREEN1)

    while True:
        # Process inputs
        player_input(player, walls)
        event_loop()
        # Update game world
        # Generate outputs
        graphics_renderer(player, walls)
        clock.tick(60)


def build_maze(screen, walls):
    """
    """

    for wall in walls:
        game.draw.rect(screen, wall.get_color(), wall.get_body())


def player_input(player, walls):
    """
    """

    MOVING_SPEED = 2.05
    key = game.key.get_pressed()

    if key[game.K_DOWN]:
        player.go(0, MOVING_SPEED, walls)

    if key[game.K_LEFT]:
        player.go(-MOVING_SPEED, 0, walls)

    if key[game.K_RIGHT]:
        player.go(MOVING_SPEED, 0, walls)

    if key[game.K_UP]:
        player.go(0, -MOVING_SPEED, walls)


if __name__ == "__main__":
    main_loop()
