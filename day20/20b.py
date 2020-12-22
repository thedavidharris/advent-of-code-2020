#!/usr/bin/env python3
from collections import Counter
from math import prod

class Tile:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def top(self):
        return self.data[0]

    def bottom(self):
        return self.data[-1]

    def left(self):
        return ''.join([x[0] for x in self.data])

    def right(self):
        return ''.join([x[-1] for x in self.data])

    def edges(self):
        return [self.left(), self.right(), self.top(), self.bottom()]

    def flipped_edges(self):
        return [x[::-1] for x in self.edges()]


with open("input.txt") as f:
    input = [x.splitlines() for x in f.read().split("\n\n")]

tiles = []
print(len(input))
for part in input:
    tiles.append(Tile(part[0].split()[1].replace(":", ""), part[1:]))

edge_counter = Counter()
for tile in tiles:
    for edge in tile.edges():
        edge_counter[edge] += 1
    for edge in tile.flipped_edges():
        edge_counter[edge] += 1

corners = []
for tile in tiles:
    unique = 0
    for edge in tile.edges():
        if edge_counter[edge] == 1:
            unique += 1
    if unique == 2:
        corners.append(int(tile.id))

print(corners)
print(prod(corners))
