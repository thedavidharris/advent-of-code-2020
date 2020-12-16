#!/usr/bin/env python3
import itertools
import collections

from collections import defaultdict

with open("input.txt") as f:
    input = f.read()


sections = input.split("\n\n")

rules_section = sections[0]

rules = {}
for rule in rules_section.splitlines():
    # name, ranges = rule.split(": ")[0]
    name, rule = rule.split(": ")
    subrules = rule.split(" or" )
    x1, y1 = [int(x) for x in subrules[0].split("-")]
    x2, y2 = [int(x) for x in subrules[1].split("-")]
    rules[name] = list(itertools.chain(range(x1,y1+1), range(x2,y2+2)))

ticket_section = sections[2].splitlines()[1:]
valid_tickets = []

# Part 1
invalid_values = []

total_range = list(itertools.chain(*rules.values()))
tickets = [[int(y) for y in ticket_line.split(",")] for ticket_line in ticket_section]

for ticket in tickets:
    is_valid = True
    for value in ticket:
        if value not in total_range:
            invalid_values.append(value)
            is_valid = False
    if is_valid:
        valid_tickets.append(ticket) 

# part 1
print("Part 1: " + str(sum(invalid_values)))

num_files = len(valid_tickets)

valid_mapping = collections.defaultdict(list)
for field in rules:
    for i in range(len(rules.keys())):
        if all(valid_tickets[i] in rules[field] for valid_tickets in valid_tickets):
            valid_mapping[field].append(i)

answer_set = {}

# Until all the possible options have been exhausted
while(any(valid_mapping.values())):
    for field, possibility in valid_mapping.items():
        # For some field, there's going to be only one possible match
        if len(possibility) == 1:
            correct_field = possibility[0]
            answer_set[field] = correct_field

            # Iterate through the rest of the possibilities
            for other in valid_mapping.values():
                # Remove this field as a possible value in the valid mappings
                if correct_field in other:
                    other.remove(correct_field)
            break

my_ticket = sections[1].splitlines()[1].split(",")

answer = 1
for field in answer_set:
    if "departure" in field:
        answer *= int(my_ticket[answer_set[field]])
print("Part 2: " + str(answer))




