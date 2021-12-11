"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

To begin, get your puzzle input.

--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""

from dataclasses import dataclass

filename = 'input.txt'
h = 0
v = 0
d = 0

@dataclass
class Coord:
    x: int
    y: int


class Vent:
    def __init__(self, x1, y1, x2, y2):
        self.start = Coord(x1, y1)
        self.end = Coord(x2, y2)
        self.all_coords = []
        self.horozontal = check_horozontal(self)
        self.vertical = check_vertical(self)

    def populate_coords(self):
        global h, v, d
        if self.horozontal:
            h += 1
            if self.start.y < self.end.y:
                for y in range(self.start.y, self.end.y + 1):
                    self.all_coords.append(Coord(self.start.x, y))
            else:
                for y in range(self.end.y, self.start.y + 1):
                    self.all_coords.append(Coord(self.start.x, y))
        elif self.vertical:
            v += 1
            if self.start.x < self.end.x:
                for x in range(self.start.x, self.end.x + 1):
                    self.all_coords.append(Coord(x, self.start.y))
            else:
                for x in range(self.end.x, self.start.x + 1):
                    self.all_coords.append(Coord(x, self.start.y))
        else:
            d += 1
            # Check if increasing:
            if self.start.x < self.end.x:
                x_increase = 1
            else:
                x_increase = -1
            if self.start.y < self.end.y:
                y_increase = 1
            else:
                y_increase = -1

            if abs(self.start.x - self.end.x) != abs(self.start.y - self.end.y):
                raise IOError("Diagonal not at 45 deg")

            for i in range(abs(self.start.x - self.end.x) + 1):
                self.all_coords.append(Coord(self.start.x + (i * x_increase), self.start.y + (i * y_increase)))
        print("complete")


def check_horozontal(vent):
    if vent.start.x == vent.end.x:
        return True
    else:
        return False


def check_vertical(vent):
    if vent.start.y == vent.end.y:
        return True
    else:
        return False


def get_data():
    output = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.split(' -> ')
        start = line[0].split(',')
        end = line[1].split(',')
        coord = Vent(int(start[0]), int(start[1]), int(end[0]), int(end[1]))
        output.append(coord)
    return output


def sum_coords(coords_list):
    coord_dict = {}
    total_additions = 0
    for coord in coords_list:
        try:
            coord_dict[f"{coord.x}, {coord.y}"] += 1
            total_additions += 1
            print(f"{total_additions} = ({coord.x}, {coord.y}: {coord_dict[f'{coord.x}, {coord.y}']}")
        except KeyError:
            coord_dict[f"{coord.x}, {coord.y}"] = 1
    return coord_dict


def sum_greater_than(coord_dict, min):
    total = 0
    for value in coord_dict.values():
        if value >= min:
            total += 1
    return total


coordinates = get_data()
print(len(coordinates))

all_coords = []
for vent in coordinates:
    vent.populate_coords()
    all_coords.extend(vent.all_coords)

print(f"{len(all_coords)}")

dic = sum_coords(all_coords)
total = sum_greater_than(dic, 2)

print(len(dic))
to_pop = []
for item in dic:
    if dic[item] == 1:
        to_pop.append(item)

print(f"To Pop: {len(to_pop)}")

print(len(dic))


print(total)
# items = dic.values().sorted()
print(f"h = {h}")
print(f"v = {v}")
print(f"d = {d}")
print(h + v + d)
