from graphics import Canvas

"""
Your job is to write a program that draws a circle wherever the mouse is located on the screen. The user will move their mouse within the canvas, and a circle should be drawn with its left and top x and y values as the x and y values of the user's mouse. Each circle should have a width and height of CIRCLE_SIZE (a constant defined for you in the starter code), and a color of your choosing. The animation should have a delay of DELAY (another constant defined for you in the starter code). 

As an extension, only draw a circle if the mouse is on the canvas. To do this, check that the mouse_x and mouse_y are within the boundaries of CANVAS_WIDTH and CANVAS_HEIGHT.

The program generates all circles within the Canvas boundaries.

Scribbles Section problem
Code in Place 2023
Outdated problem
"""

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # your animation code here :)

    animate_circles(canvas)


def animate_circles(canvas):

    while True:
        x_within_bounds = (
            canvas.get_mouse_x() <= CANVAS_WIDTH and canvas.get_mouse_x() >= 0
        )
        y_within_bounds = (
            canvas.get_mouse_y() <= CANVAS_WIDTH and canvas.get_mouse_y() >= 0
        )
        if x_within_bounds and y_within_bounds:
            canvas.create_oval(
                canvas.get_mouse_x(),
                canvas.get_mouse_y(),
                canvas.get_mouse_x() + CIRCLE_SIZE,
                canvas.get_mouse_y() + CIRCLE_SIZE,
                "BLUE",
            )

        time.sleep(DELAY)


if __name__ == "__main__":
    main()
