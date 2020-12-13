#!/usr/bin/env python3
with open("input.txt") as f:
    input = f.read().splitlines()

earliest_start = int(input[0])
bus_lines = [int(x) for x in input[1].split(",") if x.isdigit()]

current_time = earliest_start
while True:
    for bus in bus_lines:
        if current_time % bus == 0:
            print((current_time-earliest_start) * bus)
            exit(0)
    current_time += 1