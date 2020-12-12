#!/usr/bin/env python3
with open("input.txt") as f:
    input = f.read().splitlines()


net_ns = 0
net_ew = 0

direction_to_degrees = {"N": 0,
                        "E": 90,
                        "S": 180,
                        "W": 270}

degrees_to_direction = {0: "N",
                        90: "E",
                        180: "S",
                        270: "W"}

face_direction = "E"
face_degrees = direction_to_degrees[face_direction]

for line in input:
    direction = line[0]
    magnitude = int(line[1:])

    if direction == "L":
        face_degrees = (face_degrees - magnitude) % 360
        print("Rotated " + str(magnitude) + " to now face " + degrees_to_direction[face_degrees])
        continue
    elif direction == "R":
        face_degrees = (face_degrees + magnitude) % 360
        print("Rotated " + str(magnitude) + " to now face " + degrees_to_direction[face_degrees])
        continue
    elif direction == "F":
        current_direction = degrees_to_direction[face_degrees]
    else:
        current_direction = direction
    
    if current_direction == "N":
        print("Moving " + str(magnitude) + " units " + current_direction)
        net_ns += magnitude
    if current_direction == "S":
        print("Moving " + str(magnitude) + " units " + current_direction)
        net_ns -= magnitude
    if current_direction == "E":
        print("Moving " + str(magnitude) + " units " + current_direction)
        net_ew += magnitude
    if current_direction == "W":
        print("Moving " + str(magnitude) + " units " + current_direction)
        net_ew -= magnitude

    print(net_ew, net_ns)

print(abs(net_ns)+abs(net_ew))
