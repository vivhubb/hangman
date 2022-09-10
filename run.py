import random
from words import words

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
