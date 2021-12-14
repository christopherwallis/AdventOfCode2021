"""
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?
"""
from dataclasses import dataclass
import numpy


filename = 'input.txt'
# filename = 'test_input.txt'
dots = []
folds = []
dot_map = numpy.zeros((2000, 2000))


@dataclass
class Dot:
    x: int
    y: int


def get_data():
    global folds, dots
    output_dots = []
    output_folds = []
    with open(filename, 'r') as file:
        data_lines = file.readlines()
    for data_line in data_lines:
        data_line = data_line.strip('\n')
        if "fold" not in data_line:
            if len(data_line) == 0:
                continue
            coords = data_line.split(',')
            current_dot = Dot(int(coords[0]), int(coords[1]))
            output_dots.append(current_dot)
        else:
            output_folds.append(data_line.split(' ')[-1])
    folds = output_folds.copy()
    dots = output_dots.copy()
    return [len(output_dots), len(output_folds)]


def populate_dots():
    global dots, dot_map
    for dot in dots:
        dot_map[dot.x, dot.y] = 1


def wipe_past():
    pass


def fold(direction, position: int):
    global dot_map
    if direction == 'x':
        for row in range(position, len(dot_map)):
            for col in range(len(dot_map[row])):
                if dot_map[row, col] == 1:
                    dot_map[(2 * position) - row, col] = 1
                    dot_map[row, col] = 0
    elif direction == 'y':
        for col in range(position, len(dot_map[0])):
            for row in range(len(dot_map)):
                if dot_map[row, col] == 1:
                    dot_map[row, (2 * position) - col] = 1
                    dot_map[row, col] = 0


def count_dots():
    return numpy.count_nonzero(dot_map)


print(get_data())
populate_dots()
print(count_dots())
# for i in dot_map:
#     print(i)
fold(folds[0].split('=')[0], int(folds[0].split('=')[1]))

print(count_dots())
# for i in dot_map:
#     print(i)
print("Complete")