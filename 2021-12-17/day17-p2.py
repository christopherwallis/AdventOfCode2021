"""
--- Part Two ---
Maybe a fancy trick shot isn't the best idea; after all, you only have one probe, so you had better not miss.

To get the best idea of what your options are for launching the probe, you need to find every initial velocity that causes the probe to eventually be within the target area after any step.

In the above example, there are 112 different initial velocity values that meet these criteria:

23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7
How many distinct initial velocity values cause the probe to be within the target area after any step?
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
    with open(filename, 'r') as file:
        data_line = file.readline()
    new_line = data_line.strip('\n')
    return new_line


def in_area(x, y):
    global target_data
    if x not in range(target_ints[0], target_ints[1] + 1):
        return False
    if y not in range(target_ints[2], target_ints[3] + 1):
        return False
    return True


def calculate_steps(vx, vy, target=target_ints):
    """
    y_next = y_current
    """
    global highest_match
    initial_vel = [vx, vy]
    output_path = []
    new_coord = [0, 0]
    max_y = -0
    max_height = 0
    while (new_coord[0] <= target[1]) and (new_coord[1] >= target[2]):
        output_path.append(new_coord.copy())

        if new_coord[1] > max_y:
            max_y = new_coord[1]
        new_coord[0] += vx
        new_coord[1] += vy
        if vy == 0:
            max_height = new_coord[1]
        if vx > 0:
            vx = vx - 1
        else:
            if new_coord[0] < target_ints[0]:
                # print(f'Stopped early: \t{new_coord[0]} \t({initial_vel}')
                return False
        vy = vy - 1
        # print(f"x: {new_coord[0]}, \ty: {new_coord[1]}, \tvx: {vx}, \tvy: {vy}")
        if in_area(new_coord[0], new_coord[1]):
            print(f"MATCH: x: {new_coord[0]}, \ty: {new_coord[1]}, Target: {target}, MAX_Y:{max_y}")
            print(f"Max height = {max_height}, initial_vel = {initial_vel}")
            if highest_match < max_height:
                highest_match = max_height
            return True
    return False


start = time.time()
target_data_string = get_data()
target_data = pre.findall(target_data_string)
# for i in range(len(target_data[0])):
#     target_data[i] = int(target_data[0][i])
target_data = target_data[0]

for num in target_data:
    target_ints.append(int(num))
vx_min = 1
vx_max = target_ints[1] + 100
# vx_max = 100
vy_max_neg = target_ints[2] - 100
# vy_max_neg = 0
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

print(matches)
print(f"Highest Match:  {highest_match}")
print(f"Number Matches: {len(matches)}")

# calculate_steps(7, 2, target=target_ints)

print(f"Complete: {(time.time() - start):.2f}")
