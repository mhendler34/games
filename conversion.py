#!/usr/bin/python3

import random

binary = ""

for i in range(8):
    temp = str(random.randint(0, 1))
    print(temp)
    binary += temp
print(binary)

b_digits = list(binary)
decimal_value = 0

for i in range(8):
    decimal_value += int(b_digits[i]) * (2 ** (7 - i))
    print(i)
    print(decimal_value)

print()
print("-----")
for i in range(7, -1, -1):
    print(i)

