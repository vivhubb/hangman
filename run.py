import random
from string import ascii_letters
from words import words
from hangman_game import HangmanGame
from rules import greeting, rules

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


def main():
    """
    this is the main function of the program
    """
    name = input('Hello! Please type your name here: ')
    print(f'\nWelcome {name}!')
    print(greeting)
    see_rules = input('Would you like to see the Game Rules and Instructions \
before playing? (Y/N): ')
    play = ''

    if check_option(see_rules) and see_rules.upper() in ['N', 'NO']:
        play = 'Y'

    elif check_option(see_rules) and see_rules.upper() in ['Y', 'YES']:
        print(rules)
        play = input(f'{name}, are you ready to play? (Y/N)')

    if check_option(play) and play.upper() in ['Y', 'YES']:
        while True:
            random_word = get_random_word()
            hangman_game = HangmanGame(random_word)
            hangman_game.run_game()

            option = get_option()
            if option in ['N', 'NO']:
                break
    else:
        print('Quitting the game...')


main()
