from utilities import utilities as u

def test_get_word_list():
    word_list = u.get_word_list()
    assert isinstance(word_list, list)
    assert '\n' not in ''.join(word_list)

def test_get_word():
    assert isinstance(u.get_word(), str)
    
def test_sanitization():
    game = u.Hangman()
    letter = u.select_random_letter()
    assert game.sanitization(letter) == (letter not in game.correct_guesses) or (letter not in game.incorrect_guesses)
        
def test_check_letter():
    game = u.Hangman()
    letter = u.select_random_letter()
    assert game.check_letter(letter) == (letter in game.word)
    
def test_find_indexes():
    game = u.Hangman()
    letter = u.select_random_letter()
    assert (len(game.find_indexes(letter)) > 0) == game.check_letter(letter)
    
def test_update_underscores():
    game = u.Hangman()
    letter = u.select_random_letter()
    game.update_underscores(letter)
    assert (letter in game.underscores) == game.check_letter(letter)
    
def test_check_word():
    sanitization = u.Sanitize()
    word = u.get_word()
    assert sanitization.check_word(word) == sanitization.dictionary.check(word)