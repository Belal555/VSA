# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

word = choose_word(wordlist)
random = word
lst = []
for letter in random:
    lst.append(letter)
print lst

blank = []
for letter in random:
    blank.append("_")
print blank

print "Welcome to Hangman!"
print "I am thinking of a word that is" ,len(lst), "letters long!"

user_input = raw_input("Choose a letter!")
counter = 0
for letter in lst:
    if user_input == lst[counter]:
        blank[counter] = user_input
    counter = counter + 1
print blank


# alphabet = "Available letters: abcdefghigklmnopqrstuvwxyz"
# print alphabet

var = string.lowercase
print var
var = var.replace(user_input, "")
print var
# if letter = user_input:







