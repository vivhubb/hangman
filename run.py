import random
from string import ascii_letters
from words import words
from hangman_game import HangmanGame
from rules import GREETING, RULES
from phrases import phrases

BANNER = """
.............................
.............................
|_   _   _   _   _ _   _   _
| | |_| | | |_| | | | |_| | |
             _|
.............................
.............................
"""


def get_random_word():
    """
    this function selects a random word from words list
    """
    while True:
        word = random.choice(words)
        if len(word) >= 4:
            return word.upper()


def get_random_phrase():
    """
    this function selects a random phrase from phrases list
    """
    phrase = random.choice(phrases)
    return phrase.upper()


def get_option():
    """
    this function allows the user to decide
    if they want to play again
    """
    option = None
    while True:
        option = input('\n Wanna play again? Type Y/N: ')
        if check_option(option):
            option = option.upper()

        if option in ['Y', 'N']:
            return option
        print('\n Invalid answer. Wanna play again? Type Y/N: ')


def check_option(option):
    """
    this function checks the user input from get_option()
    """
    for x in option:
        if x not in ascii_letters:
            return False
    return True


def get_name():
    """
    this function validates the name input
    """
    while True:
        name = input(' Please type your name here: ')
        if check_option(name) and name.strip() != '':
            return name
        print('Invalid input. Please try again.')


def get_difficulty(name):
    """
    this function gets difficulty request from user
    """
    difficulty = 'X'

    while check_option(difficulty) and difficulty.upper() not in ['E',
                                                                  'H',
                                                                  'Q']:
        difficulty = input(f' {name}, are you ready? Please select \
difficulty level to play.\n'
                           f' Type "E" (easy), "H" (hard) or "Q" to QUIT \
the game: ')

    return difficulty.upper()


def main():
    """
    this is the main function of the program
    """
    name = get_name()
    print(f'\n Welcome, {name}!')
    print(GREETING)
    see_rules = input(' Would you like to read the GAME RULES \
before playing? (Y/N): ')

    if check_option(see_rules) and see_rules.upper() == 'Y':
        print(RULES)

    difficulty = get_difficulty(name)

    # game loop
    while True:
        level = ''

        if difficulty.upper() == 'E':
            random_choice = get_random_word()
            level = 'E'
        else:
            random_choice = get_random_phrase()
            level = 'H'
        if difficulty.upper() == 'Q':
            break

        hangman_game = HangmanGame(random_choice, level)
        hangman_game.run_game()

        option = get_option()
        if option == 'N':
            break
        difficulty = get_difficulty(name)

    print(' Quitting the game...')


main()
