#!/usr/bin/python3
# Game to enter Binary and convert it to Decimal

print("Enter a number between 0 and 255")
print("This Decimal to Binary converter, will convert it")

decimal = int(input('> '))

binary = ""

if decimal < 0 or decimal > 255:
    print("Please enter a number between 0 and 255")

if decimal > 128:
    binary += '1'
    decimal -= 128
else:
    binary += '0'

if decimal > 64:
    binary += '1'
    decimal -= 64
else:
    binary += '0'

if decimal > 32:
    binary += '1'
    decimal -= 32
else:
    binary += '0'

if decimal > 16:
    binary += '1'
    decimal -= 16
else:
    binary += '0'

