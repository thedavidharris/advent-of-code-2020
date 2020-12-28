#!/usr/bin/env python3

with open("input.txt") as f:
    card, door = [int(x) for x in f.read().splitlines()]

def transform(number):
    i = 0
    while True:
        if pow(7, i, 20201227) == number:
            return i
        i += 1

print(pow(card, transform(door), 20201227))