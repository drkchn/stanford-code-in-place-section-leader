"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.


Mars Weight Section problem
Code in Place Week 3
"""


def main():

    # We write constants in all upper case
    MARS_CONSTANT = 0.378

    # We prompt for user input using Python's input function
    earth_weight = input("Enter a weight on Earth:")

    # User enters a string, so we need to first cast variable into a float, so we can run calculations
    earth_weight = float(earth_weight)

    # We perform the calculation for determining your weight on Mars
    mars_weight = earth_weight * MARS_CONSTANT

    # First, we need to cast the float into a str. Then, we use Python's print function to output your weight on Mars
    print("The equivalent weight on Mars:" + str(mars_weight))


if __name__ == "__main__":
    main()
