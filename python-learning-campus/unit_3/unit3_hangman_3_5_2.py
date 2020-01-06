import pyfiglet
import sys
from pyfiglet import figlet_format
from pyfiglet import Figlet
custom_fig = Figlet(font='standard')

MAX_TRIES = 6
hangman_banner = pyfiglet.figlet_format("Hangman",font='standard')
print(hangman_banner,MAX_TRIES)
word = input ("Please enter a word: ")
print ("_ " * len(word))
print () 
guess_a_letter =  input ("Guess a letter: ")

print (guess_a_letter.lower())
