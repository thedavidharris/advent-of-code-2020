#!/usr/bin/env python3
from collections import defaultdict
from itertools import chain

with open("input.txt") as f:
    input = f.read().splitlines()


all_ingredients = set()
appearances = defaultdict(int)

possible = {}
for line in input:
    ingredients, allergens = line.split(" (contains ")
    ingredients = ingredients.split()
    allergens = allergens[:-1].split(", ")

    for ingredient in ingredients:
        all_ingredients.add(ingredient)
        appearances[ingredient] += 1

    for allergen in allergens:
        if allergen not in possible:
            possible[allergen] = set(ingredients)
        else:
            possible[allergen] &= set(ingredients)

answer = []

while len(possible) > 0:
    print(possible)
    allergen = min(possible, key=possible.get) 
    if len(possible[allergen]) > 0:
        ingredient = possible[allergen].pop()

        answer.append((allergen, ingredient))
        for key in possible.keys():
            possible[key].discard(ingredient)

    del possible[allergen]
print(",".join([x[1] for x in sorted(answer)]))