#!/usr/bin/env python3

print(max([int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for line in open('input.txt', 'r').read().splitlines()]))
