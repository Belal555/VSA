# Name: Belal and Mia   
# Date: 7/11/18


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
def hangman():
    word = choose_word(wordlist)
    random = word
    wrong_guess = 0
    lst = []
    for letter in random:
        lst.append(letter)
    #print lst

    blank = []
    for letter in random:
        blank.append("_")


    print"* * * * * * *"
    print"*|         |*"
    print"*|         |*"
    print"*|_________|* * * * * * * * * * * * * * * * * * * * * * * * *     "
    print"*|         |_____   ______ ____  ---- ---- ______   ______  *"
    print"*|         ||    |  |     |    ||    |    ||     |  |     | * "
    print"*|         ||____|\_|     |____||    |    ||_____|\_|     | *"
    print"* * * * * * * * * * * * * * * *|* * * * * * * * * * * * * * * "
    print"                               | "
    print"                           |___|"
    print""

    print" Welcome To Hangman!"
    print "-------------"
    print "|            "
    print "|            "
    print "|"
    print "|"
    print "|"
    print "|"
    print "|"
    print "|"
    print "_____________"
    print
    print ' '.join(blank)
    print
    print "I am thinking of a word that is" ,len(lst), "letters long!"
    print
    print "You have 20 chances to get it right! Easy enough?"

    counter = 0
    guess = 20
    var = string.lowercase
    print
    print "Available letters:" ,var

    win = False
    while guess > 0 and guess <= 20:
        if ("_") not in blank:
            win = True
            print ""
            print "------------------"
            print ""
            print "YAAAASSSSSSS QUEEN YOU WON!!!! <3"
            break
        user_input = raw_input("Choose a letter! ")
        print ""
        print "--------------------"
        print ""
        guess = guess - 1

        print "You have", int(guess), "left! "
        for letter in lst:
            if user_input == lst[counter]:
                blank[counter] = user_input
            counter = counter + 1

        if user_input not in var:
            print "You can't put that! TRY AGAIN"
            wrong_guess = wrong_guess + 1
        elif user_input not in random:
            print "Oops that is not correct!"
            wrong_guess = wrong_guess + 1
        if str(user_input) == str(random):
            win = True

        if wrong_guess == 1:
            print "-------------"
            print "|            |"
            print "|            O"
            print "|"
            print "|"
            print "|"
            print "|"
            print "|"
            print "|"
            print "_____________"
        if wrong_guess == 2:
            print "-------------"
            print "|            |"
            print "|            O"
            print "|            |"
            print "|            |"
            print "|            |"
            print "|"
            print "|"
            print "|"
            print "_____________"
        if wrong_guess == 3:
            print "-------------"
            print "|            |"
            print "|            O"
            print "|          _/|"
            print "|            |"
            print "|            |"
            print "|"
            print "|"
            print "|"
            print "_____________"
        if wrong_guess == 4:
            print "-------------"
            print "|            |"
            print "|            O"
            print "|          _/|\_"
            print "|            |"
            print "|            |"
            print "|"
            print "|"
            print "|"
            print "_____________"
        if wrong_guess == 5:
            print "-------------"
            print "|            |"
            print "|            O"
            print "|          _/|\_"
            print "|            |"
            print "|            |"
            print "|          _/ "
            print "|"
            print "|"
            print "_____________"
            print

        print' '.join(blank)

        if user_input in var:
            var = var.replace(user_input, "")
        print
        print "Available letters:" ,var
        counter = 0


        if wrong_guess == 6:

            print "-------------"
            print "|            |"
            print "|            O"
            print "|            |"
            print "|          _/|\_"
            print "|            |"
            print "|          _/ \_"
            print "|"
            print "|"
            print "______________"
            print "You have 0 guesses left"
            print
            print ' '.join(lst)
            print ""
            print "Oh no bby you lost :( </3"
            print
            break
        if win == True:
            guess = 0
hangman()
while True:
    play_again = raw_input("Would you like to play again? (y/n):")
    if play_again == "n":
        win = True
        print
        print "Aw too bad! Is this game too hard for the bby?"
        break


    if play_again == "y":
        print
        print "I see! Mama didn't raise no quitter,amiright?"
        print
        print
        hangman()





# if letter = user_input:







