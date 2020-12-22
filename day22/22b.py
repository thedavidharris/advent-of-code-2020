#!/usr/bin/env python3
from collections import deque

with open("input.txt") as f:
    input = f.read().split("\n\n")

p1_input = deque()
for line in input[0].splitlines()[1:]:
    p1_input.append(int(line))

p2_input = deque()
for line in input[1].splitlines()[1:]:
    p2_input.append(int(line))

def play(p1_deck, p2_deck):
    seen = set()
    while len(p1_deck) and len(p2_deck):
        game_key = (tuple(p1_deck), tuple(p2_deck))
        if game_key in seen:
            return (1, p1_deck)
        seen.add(game_key)

        play_one = p1_deck.popleft()
        play_two = p2_deck.popleft()

        if len(p1_deck) >= play_one and len(p2_deck) >= play_two:
            new_p1_deck = deque(list(p1_deck)[:play_one])
            new_p2_deck = deque(list(p2_deck)[:play_two])
            winner, _ = play(new_p1_deck, new_p2_deck)
            if winner == 1:
                p1_deck.append(play_one)
                p1_deck.append(play_two)
            else: 
                p2_deck.append(play_two)
                p2_deck.append(play_one)
        else:
            if play_one > play_two:
                p1_deck.append(play_one)
                p1_deck.append(play_two)
            else:
                p2_deck.append(play_two)
                p2_deck.append(play_one)
            
    if len(p1_deck):
        return (1, p1_deck)
    else:
        return (2, p2_deck)

winner, deck = play(p1_input, p2_input)
print(sum(index * value for index, value in enumerate(reversed(deck), 1)))
