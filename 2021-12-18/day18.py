"""

"""
from dataclasses import dataclass
import numpy
import re
import time


filename = 'input.txt'
# filename = 'test_input.txt'

target_ints = []
re_match = r'target area: x=(\d*)..(\d*), y=(\D?\d*)..(\D?\d*)'
pre = re.compile(re_match)
highest_match = 0


def get_data():
    output = []
    with open(filename, 'r') as file:
        data_lines = file.readlines()
    for line in data_lines:
        output.append(line.strip('\n'))
    return output


def interpret_line(input_line):




start = time.time()
target_data_string = get_data()
target_data = pre.findall(target_data_string)
# for i in range(len(target_data[0])):
#     target_data[i] = int(target_data[0][i])
target_data = target_data[0]

for num in target_data:
    target_ints.append(int(num))
vx_min = 1
vx_max = target_ints[1]
vx_max = 100
vy_max_neg = target_ints[2]
vy_max_neg = 0
vy_max_pos = target_ints[1] - target_ints[3] + 1000

matches = []
print(f"Range vx: \t{vx_min}, {vx_max}")
print(f"Range vy: \t{vy_max_neg}, {vy_max_pos}")
print(f"Target:   \t{target_ints}")
for vx in range(vx_min, vx_max):
    print(f"Initial x = {vx}")
    for vy in range(vy_max_neg, vy_max_pos):
        if calculate_steps(vx, vy, target=target_ints):
            matches.append([vx, vy])
            print(f"{len(matches)}: {matches[-1]}")
        else:
            # print(f"Miss: {vx}, {vy}")
            pass
print(f"Highest Match: {highest_match}")

# calculate_steps(7, 2, target=target_ints)

print(f"Complete: {(time.time() - start):.2f}")
