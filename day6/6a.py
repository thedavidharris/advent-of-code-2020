#!/usr/bin/env python3

print(sum([len(set(line.strip().replace('\n',''))) for line in open('input.txt').read().split("\n\n")]))