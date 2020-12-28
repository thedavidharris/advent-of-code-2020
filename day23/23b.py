#!/usr/bin/env pypy3
  
class Node:    
    def __init__(self,value):    
        self.value = value 
        self.next = None

n = 1000000
steps = 10000000

# Test input
# input = "389125467"

input = "157623984"
extended_input = [int(x) for x in list(input)] + list(range(10, n + 1))
nodes = [Node(int(x)) for x in extended_input]

lookup = {} # Index to Node
for index, node in enumerate(nodes):
    lookup[node.value] = node
    node.next = nodes[(index + 1) % len(nodes)]

current = nodes[0]
for _ in range(steps):
    pickup = current.next
    current.next = current.next.next.next.next

    current_value = current.value

    while current_value in [current.value, pickup.value, pickup.next.value, pickup.next.next.value]:
        current_value -= 1
        if current_value == 0:
            current_value = n

    drop_location = lookup[current_value]
    pickup.next.next.next = drop_location.next
    drop_location.next = pickup
    current = current.next

print(lookup[1].next.value * lookup[1].next.next.value)





