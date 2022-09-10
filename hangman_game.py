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
    pass
    """
    def __init__(self, random_word):
        self.random_word = random_word
        self.hang = hang
        self.hbody = hbody

    def print_board(self):
        """
        this function prints the game board
        """
        print(BANNER)
        print('\n'.join(self.hang))
