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
        self.used_letters = []
        self.error_limit = 11
        self.error_count = 0

        for _ in range(len(self.random_word)):
            self.build_word.append('-')

    def get_user_input(self):
        """
        this function returns a valid user input
        """
        while True:
            guess = input('Guess a letter (A-Z): ')
            if guess in list(ascii_letters):
                guess = guess.upper()
                if guess in self.used_letters:
                    print('This letter has already been used. \
Please try another.')
                else:
                    self.used_letters.append(guess)
                    return guess
            else:
                print('Invalid input. Please try again.')

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
                break
        self.print_board()

    def print_board(self):
        """
        this function prints the game board
        """
        lives = self.error_limit - self.error_count
        print(BANNER)
        print('\n'.join(self.hang))
        print(' '.join(self.build_word))
        print('\nLetters used: ' + ', '.join(self.used_letters) + "\n")
        print(f"You have {lives} "+("lives" if lives > 1 else "life")+" left.")
