"""
Example "arcadeplus" library code.

This example shows how to use functions to draw a scene.
It does not assume that the programmer knows how to use classes yet.

A video walk-through of this code is available at:
https://vimeo.com/167296062

If Python and arcadeplus are installed, this example can be run from the command line with:
python -m arcadeplus.examples.drawing_with_functions
"""

# Library imports
import arcadeplus

# Constants - variables that do not change
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drawing With Functions Example"


def draw_background():
    """
    This function draws the background. Specifically, the sky and ground.
    """
    # Draw the sky in the top two-thirds
    arcadeplus.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      SCREEN_HEIGHT * (1 / 3),
                                      arcadeplus.color.SKY_BLUE)

    # Draw the ground in the bottom third
    arcadeplus.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT / 3,
                                      0,
                                      arcadeplus.color.DARK_SPRING_GREEN)


def draw_bird(x, y):
    """
    Draw a bird using a couple arcs.
    """
    arcadeplus.draw_arc_outline(x, y, 20, 20, arcadeplus.color.BLACK, 0, 90)
    arcadeplus.draw_arc_outline(x + 40, y, 20, 20, arcadeplus.color.BLACK, 90, 180)


def draw_pine_tree(x, y):
    """
    This function draws a pine tree at the specified location.
    """
    # Draw the triangle on top of the trunk
    arcadeplus.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100,
                                arcadeplus.color.DARK_GREEN)

    # Draw the trunk
    arcadeplus.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcadeplus.color.DARK_BROWN)


def main():
    """
    This is the main program.
    """

    # Open the window
    arcadeplus.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Start the render process. This must be done before any drawing commands.
    arcadeplus.start_render()

    # Call our drawing functions.
    draw_background()
    draw_pine_tree(50, 250)
    draw_pine_tree(350, 320)
    draw_bird(70, 500)
    draw_bird(470, 550)

    # Finish the render.
    # Nothing will be drawn without this.
    # Must happen after all draw commands
    arcadeplus.finish_render()

    # Keep the window up until someone closes it.
    arcadeplus.run()


if __name__ == "__main__":
    main()
