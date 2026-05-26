"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then
prints the equivalent weight on that planet.

Note that the user should type in a planet with
the first letter as uppercase, and you do not need
to handle the case where a user types in something
other than one of the planets (that is not Earth).

Planetary Weight Calculator Section problem
Code in Place Week 3 Extension
"""


def main():
    # Define our constants for each planet
    MERCURY_CONSTANT = 0.376
    VENUS_CONSTANT = 0.889
    MARS_CONSTANT = 0.378
    JUPITER_CONSTANT = 2.36
    SATURN_CONSTANT = 1.081
    URANUS_CONSTANT = 0.815
    NEPTUNE_CONSTANT = 1.14

    # We ask user for input (their weight)
    earth_weight = input("Enter a weight on Earth:")

    # Typecast variable from string to float
    earth_weight = float(earth_weight)

    # We ask user for input (other planet to convert Earth weight)
    planet = input("Enter a planet:")

    # We pre-define the other planet weight as 0
    planet_weight = 0

    # if/else structure to figure out which planet the user inputted
    if planet == "Mercury":
        planet_weight = earth_weight * MERCURY_CONSTANT
    elif planet == "Venus":
        planet_weight = earth_weight * VENUS_CONSTANT
    elif planet == "Mars":
        planet_weight = earth_weight * MARS_CONSTANT
    elif planet == "Jupiter":
        planet_weight = earth_weight * JUPITER_CONSTANT
    elif planet == "Saturn":
        planet_weight = earth_weight * SATURN_CONSTANT
    elif planet == "Uranus":
        planet_weight = earth_weight * URANUS_CONSTANT
    elif planet == "Neptune":
        planet_weight = earth_weight * NEPTUNE_CONSTANT

    # We round the converted planet weight to 2 decimals places
    planet_weight = round(planet_weight, 2)

    # First typecast planet_weight to string. Then output the value to the user
    print("The equivalent weight on " + planet + ":" + str(planet_weight))


if __name__ == "__main__":
    main()
