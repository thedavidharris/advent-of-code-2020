#!/usr/bin/env python3
import re

rules = {}

def build_regex(rule_num, depth):
    if rules[rule_num].startswith('"'):
        return rules[rule_num].replace('"', '')

    current_rules = []

    for rule_part in rules[rule_num].split("|"):
        inner = []
        for reference in rule_part.split():
            inner.append(build_regex(reference, depth + 1))
        current_rules.append("".join(inner))

    return "(" + "|".join(current_rules) + ")"

 
with open("input.txt") as f:
    rules_input, messages = f.read().split("\n\n")

for rule_input in rules_input.splitlines():
    num, definition = rule_input.split(": ")
    rules[num] = definition

regex = re.compile(build_regex("0", 0))

messages = messages.splitlines()
print(sum([regex.fullmatch(message) is not None for message in messages]))

