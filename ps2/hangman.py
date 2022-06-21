# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
letters = ['e', 'i', 'k', 'p', 'r', 's']

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
word = choose_word(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    word = secret_word
    str = ""
    length = len(secret_word)
    count = 0
    for c in letters_guessed:
        if str.count(c) == 0:
            count = count + word.count(c)
        else:
            continue
        str = str + c
    if count < length:
        return False
    return True
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    length = len(secret_word)
    word = secret_word
    str = ""
    for i in word:
        if letters_guessed.count(i) == 0:
            str = str + "_ "
        else:
            for j in letters_guessed:
                if i == j:
                    str = str + i
                    break
    return str

#print(get_guessed_word(word, letters))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = letters_guessed
    alphabet = string.ascii_lowercase
    str = ""
    length = len(letters)
    for i in alphabet:
        count = 0
        for j in letters:
            if i != j:
                count = count + 1
        if count == length:
            str = str + i
    return str

#print(get_available_letters(letters))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    length = len(word)
    guesses = 6
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(length) + " letters long.")
    guessed = ""
    warnings = 3
    print("You have " + str(warnings) + " warnings left.")
    while guesses > 0 and not is_word_guessed(word, guessed):
        print("--------------")
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + get_available_letters(guessed))
        print("Please enter a letter: ")
        guess = input().lower()
        check = 0
        # Warnings
        if not guess.isalpha():
            if warnings == 0:
                guesses = guesses - 1
                print("Oops! You have no warnings left so you lose one guess: " + get_guessed_word(word,guessed))
            else:
                warnings = warnings - 1
                print("Oops! That is not a valid letter. You have " + str(warnings) + " warnings left: " + get_guessed_word(word,guessed))
            continue
        #already guessed
        already_guessed = False
        for i in guessed:
            if i == guess:
                if warnings > 0:
                    warnings = warnings - 1
                    print("Oops! You've already guessed that letter! You have " + str(warnings) + " warnings left: " + get_guessed_word(word,guessed))
                else:
                    guesses = guesses - 1
                    print("Oops! You've already guessed that letter! You have " + str(guesses) + " guesses left: " + get_guessed_word(word,guessed))
                already_guessed = True
                break
        if already_guessed:
            continue
        # Guesses
        #not guessed
        guessed = guessed + guess
        for i in word:
            if guess == i:
                break
            check = check + 1
        if check == len(word):
            print("Oops! That letter is not in my word: " + get_guessed_word(word, guessed))
            #vowel
            if (guess == "a" or guess == "e" or guess == "i" or guess == "o" or guess == "u"):
                guesses = guesses - 2
            else: #consonants
                guesses = guesses - 1
        else:
            print("Good guess: " + get_guessed_word(word, guessed))
    if guesses == 0:
        print("You lose. The word was: " + word)
    else:
        print("You win.")
        print("Your total score was: " + str(guesses * len(guessed)))




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word): #this took a stupidly large amount of time because of the last clause
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    other_len = len(other_word)
    unique = 0
    count = 0
    str = ""
    skip = []
    for i in my_word:
        if i != " ":
            str = str + i
            if i != "_":
                unique = unique + 1
    if not len(str) == other_len:
        return False
    for i in range(other_len):
        j = str[i]
        k = other_word[i]
        ToAdd = True
        for m in skip:
            if m == i:
                ToAdd = False
                break
        if j == "_":
            ToAdd = False
            for l in range(i, other_len):
                if k == other_word[l]:
                    skip.append(l)
        if j != k:
            ToAdd = False
        if ToAdd:
            count = count + 1
    if unique == count:
        return True
    return False


def show_possible_matches(my_word): #ezpz
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    matches = ""
    for i in wordlist:
        if match_with_gaps(my_word, i):
            matches = matches + i + " "
    if len(matches) != 0:
        return matches
    return "No matches found."



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    length = len(word)
    guesses = 6
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(length) + " letters long.")
    guessed = ""
    warnings = 3
    print("You have " + str(warnings) + " warnings left.")
    while guesses > 0 and not is_word_guessed(word, guessed):
        print("--------------")
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + get_available_letters(guessed))
        print("Please enter a letter: ")
        guess = input().lower()
        print(word)
        print(guess)
        check = 0
        # Warnings
        if guess == "*":
            print("Possible word matches are: ")
            print(show_possible_matches(get_guessed_word(word, guessed)))
            continue
        if not guess.isalpha():
            if warnings == 0:
                guesses = guesses - 1
                print("Oops! You have no warnings left so you lose one guess: " + get_guessed_word(word, guessed))
            else:
                warnings = warnings - 1
                print("Oops! That is not a valid letter. You have " + str(
                    warnings) + " warnings left: " + get_guessed_word(word, guessed))
            continue
        #HINT
        # already guessed
        already_guessed = False
        for i in guessed:
            if i == guess:
                if warnings > 0:
                    warnings = warnings - 1
                    print("Oops! You've already guessed that letter! You have " + str(
                        warnings) + " warnings left: " + get_guessed_word(word, guessed))
                else:
                    guesses = guesses - 1
                    print("Oops! You've already guessed that letter! You have " + str(
                        guesses) + " guesses left: " + get_guessed_word(word, guessed))
                already_guessed = True
                break
        if already_guessed:
            continue
        # Guesses
        # not guessed
        guessed = guessed + guess
        for i in word:
            if guess == i:
                break
            check = check + 1
        if check == len(word):
            print("Oops! That letter is not in my word: " + get_guessed_word(word, guessed))
            # vowel
            if (guess == "a" or guess == "e" or guess == "i" or guess == "o" or guess == "u"):
                guesses = guesses - 2
            else:  # consonants
                guesses = guesses - 1
        else:
            print("Good guess: " + get_guessed_word(word, guessed))
    if guesses == 0:
        print("You lose. The word was: " + word)
    else:
        print("You win.")
        print("Your total score was: " + str(guesses * len(guessed)))\



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #print(show_possible_matches("a_ pl_ "))


    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
   # secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
