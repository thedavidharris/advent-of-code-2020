#!/usr/bin/env python3
with open("input.txt") as f:
    input = [(x[0], int(x[1:])) for x in f.read().splitlines()]

# x-axis is real number component, y is imaginary
directions = {
    "N": 0+1j,
    "S": 0-1j,
    "E": 1+0j,
    "W": -1+0j
}

rotations = {
    "L": 0+1j,
    "R": 0-1j
}

ship = 0+0j
waypoint = 10+1j

for op, magnitude in input:
    if op in "LR":
        waypoint *= (rotations[op] ** (magnitude / 90))
    if op in "NSEW":
        waypoint += magnitude * directions[op]
    if op == "F":
        ship += magnitude * waypoint

print(int(abs(ship.real) + abs(ship.imag)))