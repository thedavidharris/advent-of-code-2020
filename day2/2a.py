#!/usr/bin/env python3
import re

print(sum(int(entry[0]) <= entry[3].count(entry[2]) <= int(entry[1]) for entry in [re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups() for line in open('input.txt', 'r').read().splitlines()]))