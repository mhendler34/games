#!/usr/bin/python3
# Trying to create a binary to decimal conversion game

import random

print("Would you like to work on converting binary octets to decimals?")
print("Enter (Y/n)")

response = input('> ').lower()

if response == 'y':

    while True:
        binary = ""  # Variable to store string of 1,0sss
        for i in range(8):  # Loop through 8 times
            temp = str(random.randint(0, 1))  # generate random 1 or 0
            binary += temp  # concatenate 1s and 0s together
        print("Convert the Binary Octet to Decimal Equivalent")
        print(binary)  # This is a string, not a number
        print("Enter decimal equivalent below")

        # CONVERT BINARY to DECIMAL
        b_digits = list(binary)  # Turn binary string to a list IOT access each
        decimal_value = 0

        # POP EACH ITEM FROM LIST
        digit_7 = b_digits.pop()  # Index position 7
        digit_6 = b_digits.pop()  # Index position 6
        digit_5 = b_digits.pop()  # Index position 5
        digit_4 = b_digits.pop()  # Index position 4
        digit_3 = b_digits.pop()  # Index position 3
        digit_2 = b_digits.pop()  # Index position 2
        digit_1 = b_digits.pop()  # Index position 1
        digit_0 = b_digits.pop()  # Index position 0

        # DO MATH ON EACH ITEM
        b7 = int(digit_7) * (2 ** 0)  # 2^0 = 1
        b6 = int(digit_6) * (2 ** 1)  # 2^1 = 2
        b5 = int(digit_5) * (2 ** 2)  # 2^2 = 4
        b4 = int(digit_4) * (2 ** 3)  # 2^3 = 8
        b3 = int(digit_3) * (2 ** 4)  # 2^4 = 16
        b2 = int(digit_2) * (2 ** 5)  # 2^5 = 32
        b1 = int(digit_1) * (2 ** 6)  # 2^6 = 64
        b0 = int(digit_0) * (2 ** 7)  # 2^7 = 128

        # ADD THEM ALL UP
        decimal_value = b7 + b6 + b5 + b4 + b3 + b2 + b1 + b0

        # for i in range(8):
        #    decimal_value += int(b_digits[i]) * (2 ** (7 - i))

        # GET USER RESPONSE AND CHECK ACCURACY
        answer = int(input('> '))

        if answer == decimal_value:
            print("That's right! You got it !!")
            print("Would you like to play again? (Y/n)")
            response = input('> ').lower()
            if response == 'y':
                continue
            else:
                print("Good work for today!")
                break

        if answer != decimal_value:
            print("Sorry, that's not quite right.")
            print("The correct answer is:")
            print(decimal_value)
            print("Would, you like to play again? (Y/n)")
            response = input('> ').lower()
            if response == 'y':
                continue
            else:
                print("Good work for today!")
                print("Work on it tomorrow")
                break

else:
    print("Maybe some other time")
'''
    for i in range(len(b_digits)):
        b_digit = b_digits.pop()
        if b_digit == '1':
            decimal_value = decimal_value + pow(2, i)
'''
