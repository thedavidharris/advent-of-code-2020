#!/usr/bin/env python3

print(sum([len(set.intersection(*[set(x) for x in g])) for g in [x.split("\n") for x in open('input.txt').read().split("\n\n")]]))