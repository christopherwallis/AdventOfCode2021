"""
--- Day 7: The Treachery of Whales ---
--- Part Two ---
The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

Move from 16 to 5: 66 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 0 to 5: 15 fuel
Move from 4 to 5: 1 fuel
Move from 2 to 5: 6 fuel
Move from 7 to 5: 3 fuel
Move from 1 to 5: 10 fuel
Move from 2 to 5: 6 fuel
Move from 14 to 5: 45 fuel
This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?
"""

from dataclasses import dataclass
import time

filename = 'input1.txt'


def get_data(filename):
    output_ints = []
    with open(filename, 'r') as file:
        output = file.readline()
        output = output.strip('\n')
        output = output.split(',')
        for item in output:
            output_ints.append(int(item))
        return output_ints


def get_max(positions):
    max = 0
    for item in positions:
        if item > max:
            max = item
    return max


def expensive_fuel(distance):
    total = 0
    while distance > 0:
        total += distance
        distance -= 1
    return total


def add_distances(data, position):
    total = 0
    for crab in data:
        total += expensive_fuel(abs(crab - position))
    return total


start = time.time()
crabs = get_data(filename)
print(f"Initial Crabs: {len(crabs)}")
maxi = get_max(crabs)
print(f"Max displacement: {maxi}")
minimum = expensive_fuel(maxi) * len(crabs)
best_position = 0
for posi in range(maxi):
    total_distance = add_distances(crabs, posi)
    print(f"{posi}: {total_distance}")
    if total_distance < minimum:
        minimum = total_distance
        best_position = posi

print(f"Best position: {best_position}")
print(f"Total Fuel: {minimum}")

