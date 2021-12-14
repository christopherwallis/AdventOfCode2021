"""
--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
"""
from dataclasses import dataclass
import time


filename = 'input.txt'
# filename = 'test_data.txt'
rules = {}
initial_chain = []


def get_data():
    global rules
    initial_polymer = []
    with open(filename, 'r') as file:
        data_lines = file.readlines()
    for p in data_lines[0].strip('\n'):
        initial_polymer.append(p)

    for data_line in data_lines:
        data_line = data_line.strip('\n')
        data_line = data_line.split(' -> ')
        if len(data_line) == 2:
            rules[data_line[0]] = data_line[1]

    return initial_polymer


def count_pairs(initial):
    poly_pairs = {}
    for p in range(len(initial) - 1):
        try:
            poly_pairs[f"{initial[p]}{initial[p+1]}"] += 1
        except KeyError:
            poly_pairs[f"{initial[p]}{initial[p+1]}"] = 1
    return poly_pairs


def grow_pairs(old_pairs):
    global rules
    new_pairs = {}
    for pair in old_pairs:
        try:
            new_pairs[f"{pair[0]}{rules[pair]}"] = new_pairs[f"{pair[0]}{rules[pair]}"] + old_pairs[pair]
        except KeyError:
            new_pairs[f"{pair[0]}{rules[pair]}"] = old_pairs[pair]

        try:
            new_pairs[f"{rules[pair]}{pair[1]}"] = new_pairs[f"{rules[pair]}{pair[1]}"] + old_pairs[pair]
        except KeyError:
            new_pairs[f"{rules[pair]}{pair[1]}"] = old_pairs[pair]
    return new_pairs


def count_parts(poly: dict):
    poly_dict = {}
    for part in poly:
        try:
            poly_dict[part[0]] += poly[part]
        except KeyError:
            poly_dict[part[0]] = poly[part]

        # try:
        #     poly_dict[part[1]] += poly[part]
        # except KeyError:
        #     poly_dict[part[1]] = poly[part]
    try:
        poly_dict[initial_chain[-1]] += 1
    except KeyError:
        poly_dict[initial_chain[-1]] = 1

    return poly_dict


start = time.time()
initial_chain = get_data()
print(initial_chain)
print(rules)
pairs = count_pairs(initial_chain)
for step in range(40):
    pairs = grow_pairs(pairs)

    parts_dict = count_parts(pairs)
    # parts_dict[polymer[0]] += 1
    # parts_dict[polymer[-1]] += 1

    print(f"{step + 1}: {sum(parts_dict.values())}")

    max_part = max(parts_dict, key=parts_dict.get)
    print(f"{max_part}: {parts_dict[max_part]}")
    min_part = min(parts_dict, key=parts_dict.get)
    print(f"{min_part}: {parts_dict[min_part]}")

print(f"Difference = {parts_dict[max_part] - parts_dict[min_part]}")