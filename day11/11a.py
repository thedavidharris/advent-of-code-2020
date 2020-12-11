#!/usr/bin/env python3
from itertools import product, chain
import copy

with open("input.txt") as f:
    input = [list(x) for x in f.read().splitlines()]

columns = len(input[0])
rows = len(input)

def neighbors(cell):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < columns for n in c):
            yield c

noChanges = False

currentInput = copy.deepcopy(input)
iter = 1
while True:
    newInput = [[0 for i in range(columns)] for j in range(rows)]
    noChanges = True
    for i in range(0,rows):
        for j in range(0, columns):
            place = currentInput[i][j]
            adjacent = [currentInput[x][y] for x,y in list(neighbors((i,j)))]
            numEmpty = sum([value == "L" for value in adjacent])
            numOccupied = sum([value == "#" for value in adjacent])
            if place == "L" and numOccupied == 0:
                newInput[i][j] = "#"
                noChanges = False
            elif place == "#" and numOccupied >= 4:
                newInput[i][j] = "L"
                noChanges = False
            else:
                newInput[i][j] = place   
    if noChanges:
        break
    else:
        currentInput = copy.deepcopy(newInput)
        
print(list(chain(*newInput)).count("#"))