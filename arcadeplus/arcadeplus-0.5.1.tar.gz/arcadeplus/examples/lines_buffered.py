"""
Using a Vertex Buffer Object With Lines

If Python and arcadeplus are installed, this example can be run from the command line with:
python -m arcadeplus.examples.lines_buffered
"""
import arcadeplus
import random

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Vertex Buffer Object With Lines Example"


class MyGame(arcadeplus.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title)

        self.shape_list = arcadeplus.ShapeElementList()
        point_list = ((0, 50),
                      (10, 10),
                      (50, 0),
                      (10, -10),
                      (0, -50),
                      (-10, -10),
                      (-50, 0),
                      (-10, 10),
                      (0, 50))
        colors = [
            getattr(arcadeplus.color, color)
            for color in dir(arcadeplus.color)
            if not color.startswith("__")
        ]
        for i in range(200):
            x = SCREEN_WIDTH // 2 - random.randrange(SCREEN_WIDTH)
            y = SCREEN_HEIGHT // 2 - random.randrange(SCREEN_HEIGHT)
            color = random.choice(colors)
            points = [(px + x, py + y) for px, py in point_list]

            my_line_strip = arcadeplus.create_line_strip(points, color, 5)
            self.shape_list.append(my_line_strip)

        self.shape_list.center_x = SCREEN_WIDTH // 2
        self.shape_list.center_y = SCREEN_HEIGHT // 2
        self.shape_list.angle = 0

        arcadeplus.set_background_color(arcadeplus.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcadeplus.start_render()

        self.shape_list.draw()

    def on_update(self, delta_time):
        self.shape_list.angle += 1
        self.shape_list.center_x += 0.1
        self.shape_list.center_y += 0.1


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcadeplus.run()


if __name__ == "__main__":
    main()
