#!/usr/bin/env python3
from collections import defaultdict

def twoSumHashing(num_arr, pair_sum):
    hashTable = {}

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            return (num_arr[i], complement)
        hashTable[num_arr[i]] = num_arr[i]


with open("input.txt") as f:
    input = [int(x) for x in f.read().splitlines()]


preambleLength = 25
for i in range(preambleLength, len(input)):
    preamble = input[i-preambleLength:i]
    # print(preamble)
    # print(input[i])
    if twoSumHashing(preamble, input[i]) is None:
        print(input[i])
        exit(0)
