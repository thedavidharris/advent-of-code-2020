#!/usr/bin/env python3

valid = 0
with open('input.txt', 'r') as f:
    for line in f:
        numbers, character, password = line.split()
        low, high = numbers.split('-')
        character = character[0]

        if (password[int(low) - 1] == character) ^ (password[int(high) - 1] == character):
            valid += 1

print(valid)
