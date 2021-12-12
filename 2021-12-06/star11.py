from dataclasses import dataclass
import time

filename = 'input1.txt'
extras = [0] * 9


def get_data(filename):
    output_ints = []
    with open(filename, 'r') as file:
        output = file.readline()
        output = output.strip('\n')
        output = output.split(',')
        for item in output:
            output_ints.append(int(item))
        return output_ints


def deal_with_extras(new_extras):
    global extras
    new_list = []
    for item in range(1, len(extras)):
        new_list.append(extras[item])
    new_list[6] += extras[0]
    new_list.append(extras[0] + new_extras)
    extras = new_list


def increment_day(jellyfish):
    next_day = []
    new_extras = 0
    for jelly in jellyfish:
        if jelly == 0:
            next_day.append(6)
            new_extras += 1
        else:
            next_day.append(jelly - 1)
    deal_with_extras(new_extras)
    return next_day


def extras_total():
    total = 0
    for item in extras:
        total += item
    return total


jf = get_data(filename)
day = 0
start = time.time()
print(f"Initial Jellyfish: {len(jf)}")
while day < 80:
    jf = increment_day(jf)
    day += 1
    print(f"Day: {day} - Time = {round(time.time() - start)}s - Jellyfish = {len(jf) + extras_total()}")
print(f"Day 80 Jellyfish: {len(jf) + extras_total()}")
while day < 256:
    jf = increment_day(jf)
    day += 1
    # print(f"Day: {day} - Time = {round(time.time() - start)}s - Jellyfish = {len(jf) + extras_total()}")
print(f"Day 256 Jellyfish: {len(jf) + extras_total()}")
