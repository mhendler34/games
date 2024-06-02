#!/usr/bin/python3
# Game to enter Binary and convert it to Decimal

print("Enter a number between 0 and 255")
print("This Decimal to Binary converter, will convert it")

decimal = int(input('> '))

binary = ""

if decimal < 0 or decimal > 255:
    print("Please enter a number between 0 and 255")

if decimal >= 128:  # This could be 2 ** 7
    binary += '1'
    decimal -= 128
else:
    binary += '0'

if decimal >= 64:  # This could be 2 ** 6
    binary += '1'
    decimal -= 64
else:
    binary += '0'

if decimal >= 32:  # This could be 2 ** 5
    binary += '1'
    decimal -= 32
else:
    binary += '0'

if decimal >= 16:  # This could be 2 ** 4
    binary += '1'
    decimal -= 16
else:
    binary += '0'

if decimal >= 8:
    binary += '1'
    decimal -= 8
else:
    binary += '0'

if decimal >= 4:
    binary += '1'
    decimal -= 4
else:
    binary += '0'

if decimal >= 2:
    binary += '1'
    decimal -= 2
else:
    binary += '0'

if decimal >= 1:
    binary += '1'
    decimal -= 1
else:
    binary += '0'

print(binary)




