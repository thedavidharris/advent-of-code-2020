#!/usr/bin/env python3
import re
from collections import defaultdict

def move(coordinate, direction):
    x, y, z = coordinate
    if direction == "e":
        return (x+1,y-1,z)
    if direction == "se":
        return (x,y-1,z+1)
    if direction == "sw":
        return (x-1,y,z+1)
    if direction == "w":
        return (x-1,y+1,z)
    if direction == "nw":
        return (x,y+1,z-1)
    if direction == "ne":
        return (x+1,y,z-1)

with open("input.txt") as f:
    input = [re.findall('e|se|sw|w|nw|ne', line) for line in f.read().splitlines()]

grid = defaultdict(bool)

for line in input:
    spot = (0,0,0)
    for direction in line:
        spot = move(spot, direction)
    grid[spot] = not grid[spot]

direction_set = {'e', 'se', 'sw', 'w', 'nw', 'ne'}

for day in range(100):
    positions = set()

    for spot in grid.keys():
        positions.add(spot)
        if grid[spot]:
            for way in direction_set:
                positions.add(move(spot, way))

    new_grid = defaultdict(bool)

    for position in positions:
        count = sum([grid[move(position, direction)] for direction in direction_set])
        if grid[position]:
            if (count == 0 or count > 2):
                new_grid[position] = False
            else:
                new_grid[position] = True
        if not grid[position]:
            if count == 2:
                new_grid[position] = True
            else:
                new_grid[position] = False
    grid = new_grid

print(sum(grid.values()))
