#!/usr/bin/env python3
from collections import defaultdict

with open('input.txt') as f:
    # Read input, cast to int and sort the list
    adapters = list(sorted(int(line) for line in f))

# Generate a dictionary for key=joltage and value=ways to get to the joltage
waysdict = defaultdict(int)
waysdict[0] = 1

# For each adapater
for i in adapters:
    # The number of ways to get to said adapter is the sum of the ways to get to any of the prior 3 joltages
    waysdict[i] = waysdict[i-1] + waysdict[i-2] + waysdict[i-3]

# Print ways to get to the highest adapter joltage
print(waysdict[adapters[-1]])