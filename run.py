import random
from words import words
from hangman_game import HangmanGame

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


def main():
    """
    this is the main function of the program
    """
    random_word = get_random_word()
    hangman_game = HangmanGame(random_word)
    hangman_game.print_board()


main()
