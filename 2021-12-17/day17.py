"""
--- Day 17: Trick Shot ---
You finally decode the Elves' message. HI, the message says. You continue searching for the sleigh keys.

Ahead of you is what appears to be a large ocean trench. Could the keys have fallen into it? You'd better send a probe to investigate.

The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward) and y (upward, or downward if negative) directions. For example, an initial x,y velocity like 0,10 would fire the probe straight up, while an initial velocity like 10,-1 would fire the probe forward at a slight downward angle.

The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.
Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
Due to gravity, the probe's y velocity decreases by 1.
For the probe to successfully make it into the trench, the probe must be on some trajectory that causes it to be within a target area after any step. The submarine computer has already calculated this target area (your puzzle input). For example:

target area: x=20..30, y=-10..-5
This target area means that you need to find initial x,y velocity values such that after any step, the probe's x position is at least 20 and at most 30, and the probe's y position is at least -10 and at most -5.

Given this target area, one initial velocity that causes the probe to be within the target area after any step is 7,2:

.............#....#............
.......#..............#........
...............................
S........................#.....
...............................
...............................
...........................#...
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTT#TT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
In this diagram, S is the probe's initial position, 0,0. The x coordinate increases to the right, and the y coordinate increases upward. In the bottom right, positions that are within the target area are shown as T. After each step (until the target area is reached), the position of the probe is marked with #. (The bottom-right # is both a position the probe reaches and a position in the target area.)

Another initial velocity that causes the probe to be within the target area after any step is 6,3:

...............#..#............
...........#........#..........
...............................
......#..............#.........
...............................
...............................
S....................#.........
...............................
...............................
...............................
.....................#.........
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................T#TTTTTTTTT
....................TTTTTTTTTTT
Another one is 9,0:

S........#.....................
.................#.............
...............................
........................#......
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTT#
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
One initial velocity that doesn't cause the probe to be within the target area after any step is 17,-4:

S..............................................................
...............................................................
...............................................................
...............................................................
.................#.............................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT..#.............................
....................TTTTTTTTTTT................................
...............................................................
...............................................................
...............................................................
...............................................................
................................................#..............
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
..............................................................#
The probe appears to pass through the target area, but is never within it after any step. Instead, it continues down and to the right - only the first few steps are shown.

If you're going to fire a highly scientific probe out of a super cool probe launcher, you might as well do it with style. How high can you make the probe go while still reaching the target area?

In the above example, using an initial velocity of 6,9 is the best you can do, causing the probe to reach a maximum y position of 45. (Any higher initial y velocity causes the probe to overshoot the target area entirely.)

Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the target area after any step. What is the highest y position it reaches on this trajectory?
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
