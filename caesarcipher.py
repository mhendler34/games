#!/usr/bin/python3
# Caesar cipher program by Al Sweigart

try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = 'ABDCEFGHIJKLMNOPQRSTUVWXYZ'

print("Caesar Cipher, by Al Sweigart")
print("\nThe Caesar Cipher encrypts letters by shifting them over by")
print("\nkey number. For example, a key of 2 means the letter A is")
print("\nencrypted into C, the letter B is encrypted into D.")
print()

# While loop for user to enter
while True:  # Stay in loop until they enter 'e' or 'd'
    print("Enter e for (e)ncrypt or d for (d)ecrypt.")
    response = input('> ').lower()
    if response == 'e':
        mode = 'encrypt'
        break
    elif response == 'd':
        mode = 'decrypt'
        break
#    print("Please enter 'e' or 'd'")

# Let user enter key to use
while True:  # Loop runs until user enters a valid key
    max_key = len(SYMBOLS) - 1  # Var = length of symbols -1 (25)
    print("Please enter the key (0 to {}) to use.".format(max_key))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
# Let the user enter the message to encrypt/decrypt
print("Enter the message to {}.".format(mode))
message = input('> ')

# Caesar Cipher only works on UPPERCASE LETTERS:
message = message.upper()
# Stores the encrypted/decrypted form of the message:
translated = ""

# Encrypt/decrypt each symbol in the message:
for symbol in message:  # For LOOP
    if symbol in SYMBOLS:  # Get encrypted/decrypted number for symbol
        num = SYMBOLS.find(symbol)  # Get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
# Handle the wrap-around if num is larger than the length of 
# SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
# Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting
        translated = translated + symbol
# Display the ecnrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print("Full {}ed text copied to clipboard.".format(mode))
except:
    pass

