"""
--- Day 15: Chiton ---
You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?
"""
from dataclasses import dataclass
import numpy
import time


filename = 'input.txt'
# filename = 'test_input.txt'
risk_map = None


class Node:
    def __init__(self, risk_level):
        self.risk = 9999
        self.risk_level = risk_level

    def set_risk(self, total_risk):
        # if not self.risk:
        #     self.risk = total_risk + self.risk_level
        #     return 1
        # else:
        if total_risk + self.risk_level < self.risk:
            self.risk = total_risk + self.risk_level
            return 1
        return 0


def get_data():
    output = []
    with open(filename, 'r') as file:
        data_lines = file.readlines()
    for data_line in data_lines:
        data_line = data_line.strip('\n')
        output.append(data_line)
    return output


def create_map(input_data):
    map_data = numpy.empty((len(input_data), len(input_data[0])), dtype=Node)
    for line in range(len(input_data)):
        for number in range(len(input_data[line])):
            map_data[number, line] = Node(risk_level=int(input_data[line][number]))
    return map_data


def calculate_risk_to(x, y, current_risk):
    if risk_map[x, y].set_risk(current_risk):
        return 1
    else:
        return 0


def calculate_risks_around(x, y):
    global risk_map
    current_risk = risk_map[x, y].risk
    max_x = risk_map.shape[0] - 1
    max_y = risk_map.shape[1] - 1
    changes = 0

    # Left
    if x > 0:
        # if y > 0:
        #     changes += calculate_risk_to(x - 1, y - 1, current_risk)
        changes += calculate_risk_to(x - 1, y, current_risk)
        # if y < max_y:
        #     changes += calculate_risk_to(x - 1, y + 1, current_risk)
    # Middle
    if y > 0:
        changes += calculate_risk_to(x, y - 1, current_risk)
    if y < max_y:
        changes += calculate_risk_to(x, y + 1, current_risk)
    # Right
    if x < max_x:
        # if y > 0:
        #     changes += calculate_risk_to(x + 1, y - 1, current_risk)
        changes += calculate_risk_to(x + 1, y, current_risk)
        # if y < max_y:
        #     changes += calculate_risk_to(x + 1, y + 1, current_risk)

    return changes


def walk_through(max_x, max_y):
    total_changes = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            total_changes += calculate_risks_around(x, y)
    return total_changes


def reach_equilibrium():
    risk_map[0, 0].risk = 0
    total_changes = 99
    while total_changes != 0:
        total_changes = walk_through()


def ramp_up(dimension):
    global risk_map
    risk_map[0, 0].risk = 0
    for d in range(dimension):
        walk_through(d, d)
        print_risk(risk_map, d, d)


def print_risk(current_map, x_max, y_max):
    print("## MAP ##")
    for y in range(y_max):
        line = []
        for x in range(x_max):
            line.append(current_map[x, y].risk)
        print(line)


start = time.time()
data = get_data()
risk_map = create_map(data)
# walk_through(first=[0, 0], last=[risk_map.shape])
# reach_equilibrium()
ramp_up(risk_map.shape[0])
print("Complete")
print_risk(risk_map, risk_map.shape[0], risk_map.shape[1])
print(f"Complete: {(time.time() - start):.2f}")
