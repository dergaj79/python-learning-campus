import pyfiglet
import sys
from pyfiglet import figlet_format
from pyfiglet import Figlet
custom_fig = Figlet(font='standard')
old_letters_guessed = []
MAX_TRIES = 6
hangman_banner = pyfiglet.figlet_format("Hangman",font='standard')
print(hangman_banner,MAX_TRIES)
word = input ("Please enter a word: ")
print ("_ " * len(word))
print ()
letter_guessed = input("Guess a letter: ")


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    hangman exercise 6.4.1
    the function will check if the input guessing is valid and return boolean
    :param letter_guessed
    :rtype:bool
    """

    if (letter_guessed.isalpha() and (len(letter_guessed) > 1)) :
        return False
    elif (letter_guessed.isalpha() != True) and (len(letter_guessed) == 1) :
        return False
    elif ((letter_guessed.isalpha() != True) and (len(letter_guessed) > 1)) :
        return False
    elif (letter_guessed in old_letters_guessed):
        return False
    else :
        old_letters_guessed.append(letter_guessed)
        return True


def is_valid_input(letter_guessed):
    """
    hangman exercise 5.5.1
    the function will check if the input guessing is valid and return boolean
    :param letter_guessed
    :rtype:bool
    """
    if (letter_guessed.isalpha() and (len(letter_guessed) > 1)) :
        return False
    elif (letter_guessed.isalpha() != True) and (len(letter_guessed) == 1) :
        return False
    elif ((letter_guessed.isalpha() != True) and (len(letter_guessed) > 1)) :
        return False
    else :
        return True
        #print(letter_guessed.lower())


def main():
   # print(is_valid_input(letter_guessed = letter_guessed))
    res = check_valid_input(letter_guessed=letter_guessed, old_letters_guessed=old_letters_guessed)
    #old_letters_guessed.append(res)

if __name__ == "__main__":
    main()
