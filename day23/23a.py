#!/usr/bin/env python3
  
class Node:    
    def __init__(self,value):    
        self.value = value 
        self.next = None

n = 9
steps = 100

# Test input
# input = "389125467"

input = "157623984"
extended_input = [int(x) for x in list(input)]
nodes = [Node(int(x)) for x in extended_input]

lookup = {}
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

current = lookup[1].next
while current.value != 1:
    print(current.value, end="")
    current = current.next





