#!/usr/bin/python3
# ROT 13 cipher

# SET UP CONSTANTS
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print("ROT 13 cipher by Al Sweigart")

while True:
    print("Enter a message to encrypt/decrypt")
    print("Enter 'x' to EXIT")
    message = input('> ')

    if message.title() == 'X':
        break
    translated = ''
    for character in message:
        if character.isupper():  # Returns true is all characters a UPPER 
            trans_char_index = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[trans_char_index]
        elif character.islower():
            trans_char_index = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[trans_char_index]
        else:
            translated += character

    print("The translated message is")
    print(translated)
    print()
