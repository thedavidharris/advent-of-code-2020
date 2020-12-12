#!/usr/bin/env python3
from math import sin, cos, radians

with open("input.txt") as f:
    input = f.read().splitlines()

waypoint = (10,1)
ship_point = (0,0)

for line in input:
    direction = line[0]
    magnitude = int(line[1:])

    if direction == "F":
        net_move = (waypoint[0] * magnitude, waypoint[1] * magnitude)
        ship_point = (ship_point[0] + net_move[0], ship_point[1] + net_move[1])
        print(line + " | " + "Moved ship " + str(net_move) + " to " + str(ship_point))

    if direction in "NSEW":
        oldWaypoint = waypoint
        if direction == "N":
            waypoint = (waypoint[0], waypoint[1] + magnitude)
        if direction == "S":
            waypoint = (waypoint[0], waypoint[1] - magnitude)
        if direction == "E":
            waypoint = (waypoint[0] + magnitude, waypoint[1])
        if direction == "W":
            waypoint = (waypoint[0] - magnitude, waypoint[1])
        print(line + " | " + "Moved waypoint from " + str(oldWaypoint) + " to " + str(waypoint))

    if direction in "LR":
        angle = radians((magnitude % 360))
        if direction == "R":
            angle *= -1
        x = round(cos(angle)*waypoint[0] - sin(angle)*waypoint[1])
        y = round(sin(angle)*waypoint[0] + cos(angle)*waypoint[1])
        print(line + " | " + "Rotated waypoint from " + str(waypoint) + " to " + str((int(x),int(y))))
        waypoint = (int(x),int(y))

print(abs(ship_point[0]) + abs(ship_point[1]))