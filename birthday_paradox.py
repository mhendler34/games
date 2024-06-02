#!/usr/bin/python3
# Birthday paradox simulation

import datetime
import random


def get_birthdays(number_of_birthdays):
    """Returns a list of number random date objects for birthdays"""
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthday list."""
    if len(birthdays) == len(set(birthdays)):
        return None
    # Compare each birthday to every other birthday
    for a, birthday_A in enumerate(birthdays):
        for b, birthday_B in enumerate(birthdays[a + 1:]):
            if birthday_A == birthday_B:
                return birthday_A


# DISPLAY INTRO
print('''Birthday Paradox, by Al Sweigart. The Birthday Paradox shows us that
      in a group of N people, the odds that two of them have matching
      birthdays is surprisingly large. The program does a Monte Carlo
      simulation (that is, repeated random simulations) to explore
      this concept.
      It is not actually a paradox, JUST SURPRISING''')

# Set up a TUPLE of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
while True:  # Keep asking until user enters a valid amount
    print("How many birthdays shall I generate (Max 100)")
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break
    else:
        print("Please enter a whole number between 0 and 100")
print()

# Generate and Display the bithdays:
print("Here are", num_bdays, "birthdays:")
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
        month_name = MONTHS[birthday.month - 1]
        date_text = '{} {}'.format(month_name, birthday.day)
        print(date_text, end='')
print()
print()

# Determine if there are 2 birthdays that are a match
match = get_match(birthdays)

# Display the results
print("In this simulation, ", end='')
if match is not None:
    month_name = MONTHS[match.month - 1]
    date_text = '{} {}'.format(month_name, match.day)
    print("mulitple people have a birthday on", date_text)
else:
    print("There are no matching birthdays.")
print()

# Run through 100,000 simulations:
print("Generating", num_bdays, "random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let us run another 100,000 simulations.")
sim_match = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) != None:
        sim_match = sim_match + 1
print("100,000 simulations run.")

# Display simulation results
probability = round(sim_match / 100_000 * 100, 2)
print("Out of 100,000 simulations of", num_bdays, "people, there was a")
print("matching birthday in that group", sim_match, "times. This means")
print("that", num_bdays, "people have a", probability, "% chance of")
print("having a matching birthday in their group.")
print("That is proabably more than you would think.")







