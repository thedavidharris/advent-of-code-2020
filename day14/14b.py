#!/usr/bin/env python3
import itertools
import re

with open("input.txt") as f:
    input = f.read().splitlines()

memory = {}
for line in input:
    if 'mask' in line:
        mask = line.split()[2]
    else:
        address = int((re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1))) 
        value = int(line.split("=")[-1].strip())

        address = '{0:036b}'.format(address)

        result = [address[i] if bit == '0' else mask[i] for i, bit in enumerate(mask)]

        for bits in itertools.product('01', repeat=result.count('X')):
            address_bitlist = []
            bitIndex = 0
            for char in result:
                if char == 'X':
                    address_bitlist.append(bits[bitIndex])
                    bitIndex += 1
                else:
                    address_bitlist.append(char)
            memory[int(''.join(address_bitlist), 2)] = value

print(sum(memory.values()))


