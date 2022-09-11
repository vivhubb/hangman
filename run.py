import random
from string import ascii_letters
from words import words
from hangman_game import HangmanGame
from rules import greeting, rules
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
        option = input('\nWanna play again? Type Y/N: ')
        if check_option(option):
            option = option.upper()

        if option in ['Y', 'N', 'YES', 'NO']:
            return option
        else:
            print('\nInvalid answer. Wanna play again? Type Y/N: ')


def check_option(option):
    """
    this function checks the user input from get_option()
    """
    for x in option:
        if x not in ascii_letters:
            return False
    return True


def get_difficulty(name):
    difficulty = 'X'

    while check_option(difficulty) and difficulty.upper() not in ['E',
                                                                  'H',
                                                                  'EASY',
                                                                  'HARD']:
        difficulty = input(f'{name}, are you ready to play? Please select \
difficulty EASY (E) or HARD (H): ')

    return difficulty.upper()


def main():
    """
    this is the main function of the program
    """
    name = input('Hello! Please type your name here: ')
    print(f'\nWelcome {name}!')
    print(greeting)
    see_rules = input('Would you like to see the Game Rules and Instructions \
before playing? (Y/N): ')

    if check_option(see_rules) and see_rules.upper() in ['Y', 'YES']:
        print(rules)

    difficulty = get_difficulty(name)

    # game loop
    while True:
        level = ''

        if difficulty.upper() in ['E', 'EASY']:
            random_choice = get_random_word()
            level = 'E'
        else:
            random_choice = get_random_phrase()
            level = 'H'

        hangman_game = HangmanGame(random_choice, level)
        hangman_game.run_game()

        option = get_option()
        if option in ['N', 'NO']:
            break
        else:
            difficulty = get_difficulty(name)           


main()
