import random
import string

# return a random letter
def select_random_letter(): 
    return random.choice(string.ascii_lowercase)

# open word-list.txt, read in each line and append it to a list while forcing lower-case letters and stripping new-line characters from the list-item, return the list of words
def get_word_list():
    with open('utilities/word-list.txt', 'r') as file:
        return [word.lower().strip() for word in file.readlines()]

# get a list of words, return a random one
def get_word():
    word_list = get_word_list()
    return random.choice(word_list)

class hangman:
    
    def __init__(self, *args, **kwargs):
        self.word = get_word()
        self.underscores = ['_' for letter in self.word]
        self.total_guesses = 0
        self.correct_guesses = []
        self.incorrect_guesses = []
    
    # sanitize inputs for only lowercase letters and no repeat guesses
    def sanitization(self, letter):
        if not letter in string.ascii_lowercase or (letter in self.correct_guesses or letter in self.incorrect_guesses) or len(letter) != 1:
            return False
        else:
            return True
        
    # check if letter is in word
    def check_letter(self, letter):
        if letter in self.word:
            return True
        else:
            return False
        
    # return a list of index locations where letter exists in word
    def find_indexes(self, letter): 
        indexes = [] 
        for index, character in enumerate(self.word):
            if character == letter: 
                indexes.append(index) 
        return indexes
        
    # return updates underscores with new correct letters
    def update_underscores(self, letter):
        for index in self.find_indexes(letter):
            self.underscores[index] = letter
        return self.underscores
