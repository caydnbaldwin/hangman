from utilities import utilities as u

# begin game
def hangman():
      while True:
            # print greeting and begin game
            print('Welcome to Hangman!')

            # get random word and print the number of letters
            game = u.Hangman()
            print(f'Word length: {len(game.word)} letters -> {"_" * len(game.word)}')

            # while word is not correctly guessed...
            while ''.join(game.underscores) != game.word:
                  # guess a letter, make sure its not an already guessed letter, and increment total guesses
                  letter = input('Guess a letter: ').lower().strip()
                  if not game.sanitization(letter):
                        letter = input('Make sure to guess a new letter, and only one at a time: ').lower()
                        # if intentional misbehavior proceeds, kill program
                        if not game.sanitization(letter):
                              print('You play too much.')
                              exit()
                  game.total_guesses += 1
                  
                  # if letter is correct, add it to correct guess set and print correct
                  if game.check_letter(letter):
                        game.correct_guesses.append(letter)
                        print(f"Correct! -> {''.join(game.update_underscores(letter))}")
                  # if letter in incorrect, add it to incorrect guess set and print incorrect
                  else:
                        game.incorrect_guesses.append(letter)
                        print(f"Incorrect! -> {''.join(game.underscores)}")
                  # print total guesses, correct guesses, and incorrect guesses
                  print(f'Total Guesses: {game.total_guesses}')
                  print(f'Correct Guesses ({len(game.correct_guesses)}): {', '.join(sorted(game.correct_guesses))}')
                  print(f'Incorrect Guesses ({len(game.incorrect_guesses)}): {', '.join(sorted(game.incorrect_guesses))}\n')
                  
            # print that the user guessed the word correctly in x amount of tries
            print(f'You have correctly guessed the word, "{game.word}", in {game.total_guesses} tries!\n')
            
            # ask if they want to play again, if yes, recurse, if anything else, exit
            play_again = input('Type \'y\' to play again, or \'q\' to quit: ').lower().strip()
            if play_again != 'y':
                  break

if __name__ == '__main__':
      hangman()