#!/usr/bin/env python3
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

rows = len(input)
columns=len(input[0])

currentRow=0
currentColumn=0
count = 0
while currentRow < rows:
    currentRow+=1
    currentColumn+=3
    if currentRow >= rows:
        break
    if input[currentRow][currentColumn % columns] == '#':
        count +=1

print(count)

[(1,1),(3,1),(5,1),(7,1),(1,2)]