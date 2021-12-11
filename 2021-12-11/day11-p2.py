"""
--- Part Two ---
It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be synchronizing!

In the example above, the first time all octopuses flash simultaneously is step 195:

After step 193:
5877777777
8877777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777

After step 194:
6988888888
9988888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888

After step 195:
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?
"""


filename = 'input.txt'
# filename = 'test_input.txt'
floor_map = []
total_flashes = 0


def get_data():
    output = []
    with open(filename, 'r') as file:
        data_lines = file.readlines()
    for data_line in data_lines:
        data_line = data_line.strip('\n')
        line_list = []
        for number in data_line:
            line_list.append(int(number))
        output.append(line_list)
    return output


def increase_all():
    global floor_map
    new_floormap = []
    for row in floor_map:
        new_row = []
        for col in row:
            new_row.append(col + 1)
        new_floormap.append(new_row)
    floor_map = new_floormap


def check_for_flashes():
    global floor_map
    flash_list = []
    for row in range(len(floor_map)):
        for col in range(len(floor_map[row])):
            if floor_map[row][col] > 9:
                flash_list.append([row, col])
    return flash_list


def increase_around_flashes(flash_list, flashed_list):
    global floor_map
    row = 0
    col = 1
    row_max = len(floor_map) - 1
    col_max = len(floor_map[0]) - 1
    for location in flash_list:
        if location not in flashed_list:
            flashed_list.append(location)
            # Low row
            if location[row] > 0:
                if location[col] > 0:
                    floor_map[location[row] - 1][location[col] - 1] += 1
                floor_map[location[row] - 1][location[col]] += 1
                if location[col] < col_max:
                    floor_map[location[row] - 1][location[col] + 1] += 1
            # Mid row
            if location[col] > 0:
                floor_map[location[row]][location[col] - 1] += 1
            if location[col] < col_max:
                floor_map[location[row]][location[col] + 1] += 1
            # High row
            if location[row] < row_max:
                if location[col] > 0:
                    floor_map[location[row] + 1][location[col] - 1] += 1
                floor_map[location[row] + 1][location[col]] += 1
                if location[col] < col_max:
                    floor_map[location[row] + 1][location[col] + 1] += 1
    return flashed_list


def reset_flashed():
    global floor_map, total_flashes
    new_flashes = 0
    new_floormap = []
    for row in floor_map:
        new_row = []
        for col in row:
            if col > 9:
                new_flashes += 1
                col = 0
            new_row.append(col)
        new_floormap.append(new_row)
    floor_map = new_floormap
    total_flashes += new_flashes
    return new_flashes


def print_state():
    for row in floor_map:
        line = ""
        for col in row:
            line = f"{line}{col}"
        print(line)


floor_map = get_data()

total_octopuses = len(floor_map) * len(floor_map[0])
for step in range(1000):
    already_flashed = []
    increase_all()
    flashes = check_for_flashes()
    while len(flashes) > len(already_flashed):
        already_flashed = increase_around_flashes(flashes, already_flashed)
        flashes = check_for_flashes()
    flash_this_round = reset_flashed()
    print(f"{step + 1}: \t {flash_this_round}")
    if flash_this_round == total_octopuses:
        print(f"Full flash - {step + 1}")
        print_state()
        break

print(f"Total Flashes: \t {total_flashes}")