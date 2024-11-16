import random
import string
import enchant

# cache the word list to avoid repeated file reads
_cached_word_list = None

# return a random letter
def select_random_letter(): 
    return random.choice(string.ascii_lowercase)

# open word-list.txt, read in each line and append it to a list while forcing lower-case letters and stripping new-line characters from the list-item, return the list of words
def get_word_list():
    global _cached_word_list
    if _cached_word_list is None:
        with open('utilities/word-list.txt', 'r') as file:
            _cached_word_list = list(map(lambda word: word.lower().strip(), file))
    return _cached_word_list

# get a list of words, return a random one
def get_word():
    return random.choice(get_word_list())

class Hangman:
    # create object by getting a random word, create an underscores attribute that has the same length as the word, initialize total guesses, correct guesses, and incorrect guesses
    def __init__(self, *args, **kwargs):
        self.word = get_word()
        self.underscores = list('_' * len(self.word))
        self.total_guesses = 0
        self.correct_guesses = []
        self.incorrect_guesses = []
    
    # sanitize inputs for only lowercase letters, no repeat guesses, and only one letter
    def sanitization(self, letter):
        return (
            letter in string.ascii_lowercase and
            letter not in self.correct_guesses and
            letter not in self.incorrect_guesses and
            len(letter) == 1
        )
        
    # check if letter is in word
    def check_letter(self, letter):
        return letter in self.word
        
    # return a list of index locations where letter exists in word
    def find_indexes(self, letter): 
        return [index for index, character in enumerate(self.word) if character == letter]
        
    # return updated underscores with new correct letters
    def update_underscores(self, letter):
        for index in self.find_indexes(letter):
            self.underscores[index] = letter
        return self.underscores

class Sanitize:
    dictionary = enchant.Dict('en_US')
    # create object
    def __init__(self, *args, **kwargs):
        self.new_word_list = set()
        self.old_list = 0
        self.new_list = 0
        
    def check_word(self, word):
        return self.dictionary.check(word)
