#!/usr/bin/env python3
from collections import defaultdict
from itertools import product

with open("input.txt") as f:
    input = [list(x) for x in f.read().splitlines()]

columns = len(input[0])
rows = len(input)

def neighbors(cell):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell:
            yield c

active_coordinates = set()

for x in range(0, rows):
    for y in range(0,columns):
        if input[x][y] == '#':
            active_coordinates.add((x,y,0,0))

for cycle in range(6):
    active_neighbor_counts = defaultdict(int)
    
    for coordinate in active_coordinates:
        for neighbor in neighbors(coordinate):
            active_neighbor_counts[neighbor] += 1

    new_active = set()
    for cube, count in active_neighbor_counts.items():
        if cube in active_coordinates:
            if count == 2 or count == 3:
                new_active.add(cube)
        elif count == 3:
            new_active.add(cube)

    active_coordinates = new_active

print(len(active_coordinates))

        