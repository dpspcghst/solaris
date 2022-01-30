from sys import exit

import pygame as game

game.init()

BLACK = (0, 0, 0)
CAPTION = "Solaris"
DARK_LIME_GREEN1 = (0, 137, 0)  # dark lime green, first shade
DARK_LIME_GREEN2 = (0, 177, 0)  # dark lime green, second shade
MODE_HEIGHT = 450
MODE_WIDTH = 850
PLAYER_HEIGHT = 16
PLAYER_WIDTH = 16
PURE_LIME_GREEN = (0, 235, 0)  # pure lime green
VERY_DARK_LIME_GREEN1 = (0, 39, 0)  # very dark lime green, first shade
VERY_DARK_LIME_GREEN2 = (0, 98, 0)  # very dark lime green, second shade

# End constant variable assignments.

game.display.set_caption(CAPTION)
screen = game.display.set_mode((MODE_WIDTH, MODE_HEIGHT))


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


class Maze():
    """
    """

    def __init__(self):
        """
        """

        pass


class Player():
    """
    """

    body = None

    color = None

    height = 0
    width = 0

    pos_x = 0
    pos_z = 0

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

    def go(self, walls, x, y):
        """
        """

        if x != 0:
            self.single_axis_go(x, 0, walls)

        if y != 0:
            self.single_axis_go(0, y, walls)

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

    def single_axis_go(self, walls, x, y):
        """
        """

        self.rect.x += x
        self.rect.y += y

        for wall in walls:

            if self.rect.colliderect(walls.rect):
                self.wall_collisions(walls, x, y)

    def wall_collisions(self, wall, x, y):
        """
        """

        if x > 0:  # Going right; Hit left side of wall
            self.rect.right = wall.get_body().left

        if x < 0:  # Going left; Hit right side of wall
            self.rect.left = wall.get_body().right

        if y > 0:  # Going down; Hit top side of wall
            self.rect.bottom = wall.get_body().top

        if y < 0:  # Going up; Hit bottom side of wall
            self.rect.top = wall.get_body().bottom


class Wall():
    """
    Nice class to hold a wall rect.
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


def build_maze(screen, walls):
    """
    """

    for wall in walls:
        game.draw.rect(screen, wall.get_color(), wall.get_body())


def event_loop():
    """
    """

    for event in game.event.get():

        if event.type == game.QUIT:
            game.quit()
            exit()


def get_walls():
    """
    """

    walls = []

    wall_1 = Wall()

    wall_2 = Wall()

    wall_3 = Wall()

    wall_4 = Wall()

    walls.append(wall_1)
    walls.append(wall_2)
    walls.append(wall_3)
    walls.append(wall_4)

    return walls


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

    player = Player(
        PLAYER_WIDTH, PLAYER_HEIGHT, 225, 425, VERY_DARK_LIME_GREEN1
    )
    walls = get_walls()

    clock = game.time.Clock()

    while True:
        # Process inputs
        player_input(player, walls)
        event_loop()
        # Update game world
        # Generate outputs
        graphics_renderer(player, walls)
        clock.tick(60)


def player_input(player, walls):
    """
    """

    MOVING_SPEED = 1  # This number cannot be a negative float.
    key = game.key.get_pressed()

    if key[game.K_DOWN]:
        player.go(walls, 0, MOVING_SPEED)

    if key[game.K_LEFT]:
        player.go(walls, -MOVING_SPEED, 0)

    if key[game.K_RIGHT]:
        player.go(walls, MOVING_SPEED, 0)

    if key[game.K_UP]:
        player.go(walls, 0, -MOVING_SPEED)


if __name__ == "__main__":
    main_loop()
