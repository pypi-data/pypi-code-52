"""
Starting Template Simple

Once you have learned how to use classes, you can begin your program with this
template.

If Python and arcadeplus are installed, this example can be run from the command line with:
python -m arcadeplus.examples.starting_template_simple
"""
import arcadeplus

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template Simple"


class MyGame(arcadeplus.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcadeplus.set_background_color(arcadeplus.color.WHITE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        arcadeplus.start_render()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcadeplus.run()


if __name__ == "__main__":
    main()
