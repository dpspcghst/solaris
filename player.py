import pygae as game


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
            self.single_axis_go(walls, x, 0)

        if y != 0:
            self.single_axis_go(walls, 0, y)

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

        self.body.x += x
        self.body.y += y

        print(f"{self.body.x}, {self.body.y}")

        for wall in walls:

            if self.body.colliderect(wall.get_body()):
                self.wall_collisions(wall, x, y)
                print(wall)

    def wall_collisions(self, wall, x, y):
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
