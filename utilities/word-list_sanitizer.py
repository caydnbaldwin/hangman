import utilities as u

def sanitize():
    # create object
    sanitization = u.Sanitize()
    
    # go into old file and get new word list    
    with open('old-word-list.txt', 'r') as file:
        for word in (line.lower().strip() for line in file):
            sanitization.old_list += 1
            if sanitization.check_word(word):
                sanitization.new_word_list.add(word)
                sanitization.new_list += 1
    
    # go into new file and write new word list
    with open('word-list.txt', 'w') as new_file:
        new_file.write('\n'.join(sorted(sanitization.new_word_list)) + '\n')
            
    print(f'Task Complete! The old list had {sanitization.old_list} words. Removed {sanitization.old_list - sanitization.new_list} words. New list has {sanitization.new_list} words.')

if __name__ == '__main__':
    sanitize()