import utilities as u

def test_get_word_list():
    word_list = u.get_word_list()
    assert len(word_list) == 10
    assert isinstance(word_list, list)
    for word in word_list:
        assert not '\n' in word

def test_get_word():
    assert isinstance(u.get_word(), str)
    
def test_sanitization():
    entity = u.hangman()
    letter = u.select_random_letter()
    assert (entity.sanitization(letter)) == (not letter in entity.correct_guesses or not letter in entity.incorrect_guesses)
        
def test_check_letter():
    entity = u.hangman()
    letter = u.select_random_letter()
    assert (entity.check_letter(letter)) == (letter in entity.word)
    
def test_find_indexes():
    entity = u.hangman()
    letter = u.select_random_letter()
    assert (len(entity.find_indexes(letter)) > 0) == (letter in entity.word)
    
def test_update_underscores():
    entity = u.hangman()
    letter = u.select_random_letter()
    entity.update_underscores(letter)
    assert (letter in entity.underscores) == (letter in entity.word)