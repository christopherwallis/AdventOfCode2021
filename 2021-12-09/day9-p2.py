"""
Advent of Code[About][Events][Shop][Settings][Log Out]Christopher Wallis 13*
   var y=2021;[Calendar][AoC++][Sponsors][Leaderboard][Stats]
Our sponsors help make Advent of Code possible:
McGraw Hill - Join us in transforming education. We are looking for talented, passionate, mission-driven software engineers and leaders looking to make a difference globally. COVID has provided the inflection point, come set the direction.
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 585.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

Answer:


Although it hasn't changed, you can still get your puzzle input.

You can also [Share] this puzzle.
"""

filename = 'input.txt'


def get_data():
    output = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        line_list = []
        for number in line:
            line_list.append(int(number))
        output.append(line_list)
    return output


def check_around(row, col, floormap):
    height = floormap[row][col]
    around = []
    if row > 0:
        if floormap[row - 1][col] <= height:
            return False
        else:
            around.append(floormap[row - 1][col])
    if row < len(floormap) - 1:
        if floormap[row + 1][col] <= height:
            return False
        else:
            around.append(floormap[row + 1][col])
    if col > 0:
        if floormap[row][col - 1] <= height:
            return False
        else:
            around.append(floormap[col - 1][col])
    if col < len(floormap[0]) - 1:
        if floormap[row][col + 1] <= height:
            return False
        else:
            around.append(floormap[col + 1][col])
    print(f"LOW: ({row, col}) {height} < {around}")
    return True


def check_around_nine(row, col, floormap):
    around = []
    if row < 0 or row >= len(floormap) or col < 0 or col >= len(floormap[0]):
        return []

    if row > 0:
        if floormap[row - 1][col] != 9:
            around.append([row - 1, col])
    if row < len(floormap) - 1:
        if floormap[row + 1][col] != 9:
            around.append([row + 1, col])
    if col > 0:
        if floormap[row][col - 1] != 9:
            around.append([row, col - 1])
    if col < len(floormap[0]) - 1:
        if floormap[row][col + 1] != 9:
            around.append([row, col + 1])
    # print(f"LOW: ({row, col}) {height} < {around}")
    return around


def check_row(midpoint, row_data):
    basin_size = 0
    position = midpoint

    # Check higher
    while row_data[position] < 9:
        basin_size += 1
        position += 1
    max = position
    # Reset position
    position = midpoint
    # Check lower
    while row_data[position] < 9:
        basin_size += 1
        position -= 1
    min = position

    return basin_size


def calculate_basin(point, floormap):
    basin_size = -1
    new_basin_size = 0
    row = point[0]
    col = point[1]
    locations_in_basin = [[row, col]]
    checked = []
    while new_basin_size > basin_size:
        basin_size = new_basin_size
        for location in locations_in_basin:
            if location not in checked:
                basin_size += 1
                locations_in_basin.extend(check_around_nine(location[0], location[1], floormap))
                checked.append(location)
    print(f"({row}, {col}) - {len(checked)} : {basin_size}")
    return basin_size


lows = []
floor_map = get_data()

for row in range(len(floor_map)):
    for col in range(len(floor_map[row])):
        if check_around(row, col, floor_map):
            lows.append([row, col, floor_map[row][col] + 1])

count = 0
risk = 0
for point in lows:
    count += 1
    risk += point[2]
    print(f"{count}: {point[0]}, {point[1]} \t- \t{point[2]} \t=>\t{risk}")

print(f"Total lows: {len(lows)}")
print(f"Risk: {risk}")

basins = []
for point in lows:
    basin_size = calculate_basin(point, floor_map)
    basins.append(basin_size)

print(basins)
basins.sort()
sorted = basins
print(f"{sorted[-3:]}")
print(f"{sorted[-3] * sorted[-2] * sorted[-1]}")