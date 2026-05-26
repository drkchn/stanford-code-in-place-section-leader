from graphics import Canvas
import random

"""
The following program generates: 
(1) a randomized number of circles on the Canvas between 0 to 100, with
(2) randomized sizes between 0 to 50 pixels, and with
(3) randomized colors.

The program generates all circles within the Canvas boundaries.

Random Circles Section problem
Code in Place Week 5 (Extensions included)
"""
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20


def main():
    print("Random Circles")
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_random_circles(canvas)


def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested.
    """
    colors = ["blue", "purple", "salmon", "lightblue", "cyan", "forestgreen"]
    return random.choice(colors)


def draw_random_circles(canvas):

    # generates a random number to randomize the number of circles that appear on our canvas
    random_num = random_number()

    for i in range(random_num):
        color = random_color()

        # generates a random number to alter the size of each circle
        size = random_size()

        # x and y coordinates to ensure the entire circle stays within the canvas
        x = random.randint(0, CANVAS_WIDTH - size)
        y = random.randint(0, CANVAS_HEIGHT - size)

        # when we create our circle, we add the randomized number (size) to our x and y coordinates
        canvas.create_oval(x, y, x + size, y + size, color)


def random_number():
    return random.randint(0, 100)


def random_size():
    return random.randint(0, 50)


if __name__ == "__main__":
    main()
