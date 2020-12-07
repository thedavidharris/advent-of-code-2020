#!/usr/bin/env python3
from collections import defaultdict

with open("input.txt") as f:
    input = f.read().splitlines()
    
containedin = defaultdict(set)
for line in input:
    color = line[:-1].split(' contain ')[0][:-5]
    for rule in line[:-1].split(' contain ')[1].split(", "):
        if rule != "no other bags":
            containedColor = " ".join(rule.split(" ")[1:-1])
            containedin[containedColor].add(color)

holdsGold = set()
def search(color):
    for c in containedin[color]:
        holdsGold.add(c)
        search(c)
search('shiny gold')
print(len(holdsGold))
