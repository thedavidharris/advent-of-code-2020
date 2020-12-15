#!/usr/bin/env python3
from collections import defaultdict
import re

with open("input.txt") as f:
    input = f.read().splitlines()

memory = defaultdict(int)

for line in input:
    if 'mask' in line:
        mask = line.split()[2]
    else:
        address = int(re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)) 
        to_write = int(line.split("=")[-1].strip())

        or_mask = int(mask.replace('X', '0'), 2)
        and_mask = int(mask.replace('X', '1'), 2)

        masked = to_write | or_mask
        masked = masked & and_mask
        memory[address] = int(masked)
print(sum(memory.values()))
