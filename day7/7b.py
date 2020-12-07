#!/usr/bin/env python3
from collections import defaultdict

with open("input.txt") as f:
    input = f.read().splitlines()
    
contains = defaultdict(list)
for line in input:
    color = line[:-1].split(' contain ')[0][:-5]
    for rule in line[:-1].split(' contain ')[1].split(", "):
        if rule != "no other bags":
            containedColor = " ".join(rule.split(" ")[1:-1])
            count = int(rule.split(' ')[0])
            contains[color].append((containedColor, count))

def total(color):
    value = 0
    for innerColor, count in contains[color]:
        value += count * (1 + total(innerColor))
    return value
print(total('shiny gold'))