#!/usr/bin/env python3

print(sum([row[lineNumber * 3 % len(row)] == '#' for lineNumber, row in enumerate(open('input.txt').read().splitlines())]))