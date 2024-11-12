import utilities.utilities as u

# begin game
def game():
      # get random word and print the number of letters
      entity = u.hangman()
      print(f'Word length: {len(entity.word)} letters -> {"_" * len(entity.word)}')
      # while word is not correctly guessed...
      while ''.join(entity.underscores) != entity.word:
            # guess a letter, make sure its not an already guessed letter, and increment total guesses
            letter = input('Guess a letter: ').lower()
            if not entity.sanitization(letter):
                  letter = input('Make sure to guess a new letter, and only one at a time: ').lower()
                  # if intentional misbehavior proceeds, kill program
                  if not entity.sanitization(letter):
                        print('You play too much.')
                        exit()
            entity.total_guesses += 1
            # if letter is correct, add it to correct guess set and print correct
            if entity.check_letter(letter):
                  entity.correct_guesses.append(letter)
                  print(f"Correct! -> {''.join(entity.update_underscores(letter))}")
            # if letter in incorrect, add it to incorrect guess set and print incorrect
            else:
                  entity.incorrect_guesses.append(letter)
                  print(f"Incorrect! -> {''.join(entity.underscores)}")
            # print total guesses, correct guesses, and incorrect guesses
            print(f'Total Guesses: {entity.total_guesses}')
            print(f'Correct Guesses ({len(entity.correct_guesses)}): {', '.join(entity.correct_guesses)}')
            print(f'Incorrect Guesses ({len(entity.incorrect_guesses)}): {', '.join(entity.incorrect_guesses)}\n')
      # print that the user guessed the word correctly in x amount of tries
      print(f'You have correctly guessed the word, "{entity.word}", in {entity.total_guesses} tries!\n')
      # ask if they want to play again, if yes, recurse, if anything else, exit
      play_again = input('Type \'y\' to play again, or \'q\' to quit: ').lower()
      if play_again == 'y':
            game()
      else:
            exit()
            
def main():
      # print greeting and begin game
      print('Welcome to Hangman!')
      game()

if __name__ == '__main__':
      main()