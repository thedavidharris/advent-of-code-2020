#!/usr/bin/env python3
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

rows = len(input)
columns=len(input[0])

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

multipliedTrees = 1
for slope in slopes:
    currentRow=0
    currentColumn=0
    count = 0
    while currentRow < rows:
        currentColumn+=slope[0]
        currentRow+=slope[1]
        if currentRow >= rows:
            break
        if input[currentRow][currentColumn % columns] == '#':
            count +=1
    multipliedTrees *= count

print(multipliedTrees)