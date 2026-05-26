from karel.stanfordkarel import *

"""
Hospital Karel Section problem
Code in Place Week 1
"""


def main():

    # Karel continually moves forward when the front is clear
    while front_is_clear():
        move()

        # We check to see if Karel is at a beeper
        if beepers_present():

            # When Karel encounters a beeper, we call the helper function to build a hospital
            build_hospital()

    # Repeat each time we encounter a beeper
    # Move Karel (using while loop at line 6)
    # Check to see if Karel is at a beeper (if statement at line 10)
    # Karel builds a hospital (call helper function at line 13)
    # Finally, we have Karel stop at her destination


# Helper function calls other helper functions to build left + right hospital columns
def build_hospital():
    build_left_col()
    build_right_col()


# Builds the left column
def build_left_col():
    turn_left()

    # use a for loop to repeat an action twice
    for i in range(2):
        place_beeper_move()


def build_right_col():
    turn_right()
    place_beeper_move()
    turn_right()

    # use a for loop to repeat an action twice
    for i in range(2):
        place_beeper_move()

    if front_is_blocked():
        turn_left()


# Helper function Karel uses to build one beeper in the hospital
def place_beeper_move():
    move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    main()
