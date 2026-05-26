from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers infinite
her bag. How can you solve this puzzle?

Spread Beepers Karel Section problem
Code in Place Week 2
"""


def main():

    # We first move Karel forward to initialize our algorithm
    move()

    # We continue running Karel when there's beepers in the second column from the left
    while beepers_present():
        pick_beeper()
        if no_beepers_present():
            # If there's no beepers, then this is the last beeper in the second column, and we want to move Karel back to the ending position
            last_beeper()

        # We keep moving Karel forward when there are no beepers present in the row. This means that we are not at the end of the row yet!
        while beepers_present():
            move()

        # We check if Karel faces east, because if Karel faces east and stops moving, then we know for a fact we are at the end of the row!
        if facing_east():
            beeper_end_of_row()

    # Once the while loop is finished running, Karel is facing the incorrect direction, so we turn her around, and conclude our program
    turn_around()


# Resets Karel's position so she goes back to her starting position (face east at the left most column)
def reset_Karel():
    while front_is_clear():
        move()
    turn_around()


# Turns Karel 180 degrees
def turn_around():
    for i in range(2):
        turn_left()


# Karel places a beeper at the end of the row, then we call the reset_Karel() helper function
def beeper_end_of_row():
    put_beeper()
    turn_around()
    reset_Karel()
    move()


# The last beeper in the stack of beepers, so we don't go to the end of the row. Karel immediately turns around and goes back to her starting position.
def last_beeper():
    put_beeper()
    turn_around()
    move()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    main()
