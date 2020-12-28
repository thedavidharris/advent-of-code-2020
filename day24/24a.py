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

print(sum(grid.values()))

