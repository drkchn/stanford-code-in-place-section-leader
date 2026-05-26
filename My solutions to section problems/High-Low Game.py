import random

"""
High-Low Game Section problem
Code in Place Week 4
"""

NUM_ROUNDS = 5


def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # NOTE: For the autograder to work, you must generate the
    # COMPUTER's number FIRST, then the user's

    iteration = 1
    my_score = 0
    while iteration <= NUM_ROUNDS:
        print("Round", iteration)
        computer_num = random.randint(1, 100)
        human_num = random.randint(1, 100)
        # statement below used for debugging
        # print("The computer's number is ", computer_num)
        print("Your number is", human_num)

        console_input = input(
            "Do you think your number is higher or lower than the computer's?: "
        )

        if human_num > computer_num and console_input == "higher":
            print("You were right! The computer's number was", computer_num)
            my_score += 1
        elif human_num < computer_num and console_input == "lower":
            print("You were right! The computer's number was", computer_num)
            my_score += 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer_num)
        iteration += 1
        print("Your score is now", my_score)
        print()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
