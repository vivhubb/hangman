from hangman_stages import hang, hbody
from string import ascii_letters

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
    pass
    """
    def __init__(self, random_word):
        self.random_word = random_word
        self.hang = hang
        self.hbody = hbody
        self.build_word = []

        for _ in range(len(self.random_word)):
            self.build_word.append('-')

    def get_user_input(self):
        """
        this function returns a valid user input
        """
        while True:
            guess = input('Guess a letter (A-Z): ')
            if guess in ascii_letters:
                return guess.upper()
            else:
                print('Invalid input. Please try again.')

    def check_user_input(self, guess):
        """
        this function checks if the user input is in randoom_word
        builds the build_word list if user input is in randoom_word
        """
        if guess in self.random_word:
            for index, value in enumerate(self.random_word):
                if guess == value:
                    self.build_word[index] = guess
            return True
        return False

    def run_game(self):
        """
        this function runs the game
        """
        self.print_board()
        guess = self.get_user_input()
        if not self.check_user_input(guess):
            print('error + 1')
            print('build the hangman')

    def print_board(self):
        """
        this function prints the game board
        """
        print(BANNER)
        print('\n'.join(self.hang))
        print(' '.join(self.build_word))
