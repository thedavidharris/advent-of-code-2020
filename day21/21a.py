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

safe = all_ingredients - set(chain(*possible.values()))
print(sum(value for key, value in appearances.items() if key in safe))







