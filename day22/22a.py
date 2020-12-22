#!/usr/bin/env python3
from collections import deque

with open("input.txt") as f:
    input = f.read().split("\n\n")

p1_cards = deque()
for line in input[0].splitlines()[1:]:
    p1_cards.append(int(line))

p2_cards = deque()
for line in input[1].splitlines()[1:]:
    p2_cards.append(int(line))


while len(p1_cards) and len(p2_cards):
    play_one = p1_cards.popleft()
    play_two = p2_cards.popleft()

    if play_one > play_two:
        p1_cards.append(play_one)
        p1_cards.append(play_two)
    else:
        p2_cards.append(play_two)
        p2_cards.append(play_one)

winning_hand = []
if len(p1_cards):
    winning_hand = p1_cards
else:
    winning_hand = p2_cards

answer = 0
for index, item in enumerate(reversed(winning_hand)):
    answer += (index + 1) * item

print(answer)
