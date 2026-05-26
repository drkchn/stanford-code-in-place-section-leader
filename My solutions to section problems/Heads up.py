import random

"""
Heads Up Section problem
Code in Place Week 6
"""

# Name of the file to read in!
FILE_NAME = "cswords.txt"


def get_words_from_file():
    """
    This function has been implemented for you. It opens a file,
    and stores all of the lines into a list of strings.
    It returns a list of all lines in the file.
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip()
        # if the line was only whitespace characters, skip it
        if line != "":
            lines.append(line)
    return lines


def main():
    # your code here :)
    lines_list = get_words_from_file()
    # print(lines_list)

    play_game(lines_list)


def play_game(game_list):

    while True:
        random_number = random.randint(0, len(game_list) - 1)
        random_word = game_list[random_number]
        print("Your word is: ")
        input(random_word)
        print()


if __name__ == "__main__":
    main()
