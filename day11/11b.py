#!/usr/bin/env python3
from itertools import product, chain
import copy

with open("input.txt") as f:
    input = [list(x) for x in f.read().splitlines()]

columns = len(input[0])
rows = len(input)

currentInput = copy.deepcopy(input)

iter=0
while True:
    newInput = [[0 for i in range(columns)] for j in range(rows)]
    noChanges = True
    for i in range(0,rows):
        for j in range(0, columns):
            adjacent = 0
            place = currentInput[i][j]
            if place != '.':
                for x in [1,0,-1]:
                    for y in [1,0,-1]:
                        if (x,y) == (0,0):
                            continue
                        idk = 0
                        empty = True
                        while(empty):
                            idk += 1
                            new_x = i+idk*x
                            new_y = j+idk*y
                            if new_x in range(rows) and new_y in range(columns):
                                nextValue = currentInput[new_x][new_y]
                                if nextValue != '.':
                                    empty = False
                                    if nextValue == '#':
                                        adjacent += 1
                            else:
                                empty = False
            if place == '#' and adjacent >= 5:
                newInput[i][j] = 'L'
                noChanges = False
            elif place == 'L' and adjacent == 0:
                newInput[i][j] = '#'
                noChanges = False
            else:
                newInput[i][j] = place
    if noChanges:
        break
    else:
        print ("Iter " + str(iter))
        for row in newInput:
            print(''.join(row))
        print('------------------------------------------------------')
        currentInput = copy.deepcopy(newInput)
        iter += 1
        
print(list(chain(*newInput)).count("#"))