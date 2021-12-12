"""
--- Part Two ---
After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

Now, the 36 possible paths through the first example above are:

start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end
The slightly larger example above now has 103 paths through it, and the even larger example now has 3509 paths through it.

Given these new rules, how many paths through this cave system are there?
"""


filename = 'input.txt'
# filename = 'test_input.txt'
# filename = 'test_data_large.txt'
all_journeys = []


def get_data():
    output = []
    with open(filename, 'r') as file:
        data_lines = file.readlines()
    for data_line in data_lines:
        data_line = data_line.strip('\n')
        output.append(data_line.split('-'))
    return output


def find_paths_from(origin: str, connection_list: list):
    output = []
    for connection in connection_list:
        if connection[0] == origin:
            output.append(connection[1])
        if connection[1] == origin:
            output.append(connection[0])
    return output


def is_small(cave_name: str):
    return cave_name.islower()


def doubles(excluded_list, lower_check=False):
    excluded_dict = {}
    max_excluded = 0
    number_of_doubles = 0
    new_excluded_list = []
    if lower_check:
        for room in excluded_list:
            if room.islower():
                new_excluded_list.append(room)
    else:
        new_excluded_list = excluded_list
    for item in new_excluded_list:
        try:
            excluded_dict[item] += 1
        except KeyError:
            excluded_dict[item] = 1
        if excluded_dict[item] > max_excluded:
            max_excluded = excluded_dict[item]
        if excluded_dict[item] > 1:
            number_of_doubles += 1
    return number_of_doubles


def is_double_excluded(room, excluded_list):
    if room == "start":
        return True
    excluded_dict = {room: 0}
    double = False
    for item in excluded_list:
        try:
            excluded_dict[item] += 1
        except KeyError:
            excluded_dict[item] = 1
        if excluded_dict[item] > 1:
            double = True
    if excluded_dict[room] > 0 and double:
        return True
    return False


# def fact_check(final_journey):
#     j_sort = final_journey.copy().sort()
#
#     for i in range(len(j_sort)):
#         if j_sort[i] == j_sort[i-1]:



def find_all_paths(route: list, full_list, excluded):
    # Add to exclusion list:
    new_excluded = excluded.copy()
    if is_small(route[-1]):
        new_excluded.append(route[-1])
        # print(f"Excluding: {route[-1]}")
    #     Find all paths
    paths = find_paths_from(route[-1], full_list)
    for path in paths:
        if path in new_excluded and doubles(new_excluded) > 0:
            pass
        elif path == "start":
            pass
        else:
            journey = route.copy()
            journey.append(path)
            if path == 'end':
                if doubles(journey, lower_check=True) > 1:
                    print(f"Error in path: {doubles(journey)}: \t {journey}")
                if doubles(new_excluded) > 1:
                    print(f"Error in exclusions: {doubles(new_excluded)}: \t {journey}")
                all_journeys.append(journey)
            else:
                # print(f"Next step: {path}")
                find_all_paths(journey, full_list, new_excluded)


visited_small = []
connections = get_data()
current_location = "start"

# Do recursion
# find paths from start
# for each path from start find all paths
# from each path find all paths
# don't double any small caves
# end on end


excluded = []

find_all_paths([current_location], connections, excluded)
count = 0
all_journeys.sort()
for count in range(len(all_journeys)):
    if all_journeys[count] == all_journeys[count - 1]:
        print(f"DUPLICATE ERROR: {all_journeys[count]}")
    print(f"{count}: \t {all_journeys[count]}")
print(f"Total: \t {len(all_journeys)}")



