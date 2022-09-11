greeting = '\nYou are about to play the HANGMAN game.'

rules = """
================================= GAME RULES =================================

The computer thinks of a random word or phrase, based on the difficulty
level you choose (easy(E) for guessing words and hard(H)) for guessing
phrases) and draws a row of dashes representing each letter of the
word. You will guess letters, one at a time, until you guess the word or the
man gets hung. Your goal is to guess the word before the man is hung.

Each time a correct letter is guessed from the word, the computer fills in
all the corresponding empty dashes with that letter for the word. If the
letter doesn't belong to the word, the computer will draw another
body part of the stick man. All special characters will be given, you'll only
have to guess letters.

The stick man consists of 11 body parts, meaning you can make 11 mistakes
guessing the right letters for the word. If the stick man is completed before
the word is guessed: YOU LOSE; if you guess the word before that: YOU WIN.

==============================================================================
"""
