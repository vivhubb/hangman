from string import ascii_letters
import platform
import os
from hangman_stages import hang, hbody

BANNER = """
.............................
.............................
|_   _   _   _   _ _   _   _
| | |_| | | |_| | | | |_| | |
             _|
.............................
.............................
"""


class HangmanGame:
    """
    class Attributes:
        random_word -> stores random word choice from words list
        hang -> stores gibbet based on errors
        hbody -> stores hangman body by stages
        build_word -> initially stores the letters from random_word as '-'
        used_letters -> stores letters guessed by user
        error_limit -> defines error limit
        error_count -> counts the mistakes made by user
        winner -> stores if there is a winner at the end of the game
        level -> easy or hard game mode
    """
    def __init__(self, random_word, level):
        self.random_word = random_word
        self.hang = list(hang)
        self.hbody = list(hbody)
        self.build_word = []
        self.used_letters = []
        self.error_limit = 11
        self.error_count = 0
        self.winner = False
        self.level = level

        if level == 'E':
            for _ in range(len(self.random_word)):
                self.build_word.append('_')
        else:
            for x in self.random_word:
                if x == '/':
                    self.build_word.append('/')
                elif x == '-':
                    self.build_word.append('-')
                elif x == "'":
                    self.build_word.append("'")
                elif x == ' ':
                    self.build_word.append(' ')
                else:
                    self.build_word.append('_')

    def get_user_input(self):
        """
        this function returns a valid user input
        """
        while True:
            guess = input(' Guess a letter (A-Z): ')
            if guess in list(ascii_letters):
                guess = guess.upper()
                if guess in self.used_letters:
                    print(' This letter has already been used. \
Please try another.')
                else:
                    self.used_letters.append(guess)
                    return guess
            else:
                print(' Invalid input. Please try again.')

    def check_user_input(self, guess):
        """
        this function checks if the user input is in random_word
        builds the build_word list if user input is in random_word
        """
        if guess in self.random_word:
            for index, value in enumerate(self.random_word):
                if guess == value:
                    self.build_word[index] = guess
            return True
        return False

    def hang_man(self):
        """
        this function builds hangman based on error count
        """

        if self.error_count == 1:
            self.hang[1] = self.hbody[self.error_count - 1]
        elif self.error_count >= 2 and self.error_count <= 6:
            self.hang[2] = self.hbody[self.error_count - 1]
        elif self.error_count == 7:
            self.hang[3] = self.hbody[self.error_count - 1]
        elif self.error_count > 7:
            self.hang[4] = self.hbody[self.error_count - 1]

    def run_game(self):
        """
        this function runs the game
        """
        while self.error_count != self.error_limit:
            self.print_board()
            guess = self.get_user_input()
            if not self.check_user_input(guess):
                self.error_count += 1
                self.hang_man()
            if ''.join(self.build_word) == self.random_word:
                self.winner = True
                break

        self.print_board()

        if self.winner:
            print(f' YAY! YOU WON! The correct answer was: {self.random_word}')
        else:
            print(f' SORRY, GAME OVER :(.\n'
                  f' The correct answer was: {self.random_word}.')

    def print_board(self):
        """
        this function prints the game board
        """
        self.clear_screen()
        lives = self.error_limit - self.error_count

        print(BANNER)
        print('\n'.join(self.hang))
        print(' ' + ' '.join(self.build_word))
        print('\n Used letters: ' + ', '.join(self.used_letters) + "\n")
        if lives > 0 and not self.winner:
            print(f" You have {lives} " +
                  ("lives" if lives > 1 else "life") + " left.")

    def clear_screen(self):
        """
        this function clears the screen
        """
        if is_windows():
            os.system('cls')        # system call, clears screen
        else:
            os.system('clear')


def is_windows():
    """
    this function checks system platform
    """
    system_name = platform.system().lower()
    if system_name == 'windows':
        return True
    return False
