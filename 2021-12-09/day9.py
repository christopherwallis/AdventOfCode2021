

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

