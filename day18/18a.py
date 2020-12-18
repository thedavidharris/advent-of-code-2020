#!/usr/bin/env python3
import re

class hacks(int):
    def __add__(self, b):
        return hacks(int(self) + b)
    def __sub__(self, b):
        return hacks(int(self) * b)

print(sum([eval(re.sub(r"(\d+)", r"hacks(\1)", line).replace("*", "-")) for line in open("input.txt").read().splitlines()]))