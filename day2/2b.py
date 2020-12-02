#!/usr/bin/env python3
import re

print(sum((entry[3][int(entry[0]) - 1] == entry[2]) ^ (entry[3][int(entry[1]) - 1] == entry[2]) for entry in [re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups() for line in open('input.txt', 'r').read().splitlines()]))