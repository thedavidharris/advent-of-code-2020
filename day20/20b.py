#!/usr/bin/env python3
from collections import Counter
from math import prod
from itertools import chain

class Tile:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.id)

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

    def rotate(self):
        self.data = list(zip(*self.data[::-1]))

    def flip(self):
        flipped = []
        for t in reversed(self.data):
            flipped.append(t)
        self.data = flipped

    def pretty_print(self):
        print(*(''.join(row) for row in self.data), sep='\n')

def remove_border(tile):
    return Tile(id=tile.id, data = [
        row[1:-1] for row in tile.data[1:-1]
    ])

def convert_data_to_strings(tile):
    return Tile(id=tile.id, data =[''.join(x) for x in tile.data])

orientation_functions = [
    lambda tile: tile,
    lambda tile: tile.rotate(),
    lambda tile: tile.rotate(),
    lambda tile: tile.rotate(),
    lambda tile: tile.flip(),
    lambda tile: tile.rotate(),
    lambda tile: tile.rotate(),
    lambda tile: tile.rotate(),
]

with open("input.txt") as f:
    input = [x.splitlines() for x in f.read().split("\n\n")]

tile_input = []
for part in input:
    tile_input.append(Tile(part[0].split()[1].replace(":", ""), part[1:]))

num_tiles = len(tile_input)

print("Input has " + str(num_tiles) + " tiles")

edge_counter = Counter()
for tile in tile_input:
    for edge in tile.edges():
        edge_counter[edge] += 1
    for edge in tile.flipped_edges():
        edge_counter[edge] += 1
print("Found " + str(len(edge_counter)) + " unique edges")

corners = []
for tile in tile_input:
    unique = 0
    for edge in tile.edges():
        if edge_counter[edge] == 1:
            unique += 1
    if unique == 2:
        corners.append(tile)

# Pick the first and orient it so it is top left
# There are two possible orientations here, because it can be flipped, just hardcoding around this 
top_left = corners[2]
for func in orientation_functions:
    func(top_left)
    if edge_counter[top_left.left()] == 1 and edge_counter[top_left.top()] == 1:
        break

print("Top left tile is " + str(top_left.id))

tile_image_matrix = [[top_left]]

all_tiles = set(tile_input)
used = {top_left}
remaining = all_tiles - used

print([x.id for x in used])
print([x.id for x in remaining])

current = top_left

# Start placing tiles to the right
def find_tile_to_right(tile, remaining_tiles):
    for candidate in remaining_tiles:
        for func in orientation_functions:
            func(candidate)
            if tile.right() == candidate.left():
                return candidate
    return None

def find_tile_on_bottom(tile, remaining_tiles):
    for candidate in remaining_tiles:
        for func in orientation_functions:
            func(candidate)
            if tile.bottom() == candidate.top():
                return candidate
    return None

while adjacent := find_tile_to_right(current, remaining):
    remaining.remove(adjacent)
    print(f"Adjacent tile is {adjacent.id}")

    tile_image_matrix[-1].append(adjacent)
    current = adjacent

outer_current = top_left

while adjacent := find_tile_on_bottom(outer_current, remaining):
    remaining.remove(adjacent)
    tile_image_matrix.append([adjacent])
    print(f"Next row start tile is {adjacent.id}")
    outer_current = adjacent

    inner_current = outer_current
    while adjacent := find_tile_to_right(inner_current, remaining):
        remaining.remove(adjacent)
        print(f"Adjacent tile is {adjacent.id}")
        tile_image_matrix[-1].append(adjacent)
        inner_current = adjacent

print()
print("Image Matrix is:")
print('\n'.join(['\t'.join([str(cell.id) for cell in row]) for row in tile_image_matrix]))
print()

removed_edges = [[remove_border(x) for x in inner] for inner in tile_image_matrix]
removed_edges = [[convert_data_to_strings(x) for x in inner] for inner in removed_edges]

removed_edge_data = [[x.data for x in inner] for inner in removed_edges]
corrected = ""
for row in removed_edge_data:
    zipped = [''.join(x) for x in list(zip(*row))]
    full_row = '\n'.join(zipped)
    corrected += full_row
    corrected += '\n'

print("Full image is: ")
print(corrected)

back_to_list = [list(x) for x in corrected.splitlines()]

def rotate_grid(grid):
    return list(zip(*grid[::-1]))

def flip_grid(grid):
    flipped_grid = []
    for t in reversed(grid):
        flipped_grid.append(t)
    return flipped_grid

# Too lazy to clean this up
grid = back_to_list
all_grid_orientations = [grid]

grid = rotate_grid(grid)
all_grid_orientations.append(grid)
grid = rotate_grid(grid)
all_grid_orientations.append(grid)
grid = rotate_grid(grid)
all_grid_orientations.append(grid)

grid = flip_grid(grid)
all_grid_orientations.append(grid)

grid = rotate_grid(grid)
all_grid_orientations.append(grid)
grid = rotate_grid(grid)
all_grid_orientations.append(grid)
grid = rotate_grid(grid)
all_grid_orientations.append(grid)

MONSTER = [
    '..................#.',
    '#....##....##....###',
    '.#..#..#..#..#..#...',
]

def is_monster(candidate, dx, dy):
	for x in range(len(MONSTER)):
		for y in range(len(MONSTER[x])):
			if MONSTER[x][y] == "#" and candidate[x+dx][y+dy] != "#":
				return False
	return True

for to_check in all_grid_orientations:
    cnt = 0
    for dx in range(0, len(to_check) - len(MONSTER)):
        for dy in range(0, len(to_check) - len(MONSTER[0])):
            if is_monster(to_check, dx, dy):
                cnt += 1
    print(f"Found {cnt} monsters at this orientation")
    if cnt > 0:
        print(str(grid).count("#") - "".join(MONSTER).count("#") * cnt)