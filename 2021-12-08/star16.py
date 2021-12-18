"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?

--- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
"""

"""
0 = None
1 = None
2 = [1] = cf
3 = [7] = acf
4 = [4] = bcdf
5 = [2, 3, 5] = adg + ce | cf | bf
6 = [0, 6, 9] = abfg + ce | de | cd
7 = [8]
"""


from dataclasses import dataclass
import time

filename = 'input1.txt'
inputs = []
outputs = []
matching_lengths = [2, 4, 3, 7]
segment_possibilities = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
possibilities = {
    0: None,
    1: None,
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

number_to_letter = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}


class Segment:
    def __init__(self, segment_letter):
        self.segment = segment_letter
        self.possibilities = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    def limit_possibilities(self, options):
        new_possible = []
        for option in options:
            if option in self.possibilities:
                new_possible.append(option)
        self.possibilities = new_possible

    def strip_possibilities(self, options):
        new_possible = []
        for possible in self.possibilities:
            if possible not in options:
                new_possible.append(possible)
        self.possibilities = new_possible


def what_is_possible(seven_seg_string):
    return possibilities[len(seven_seg_string)]


def create_segments():
    segs = {}
    for poss in segment_possibilities:
        segs[poss] = Segment(poss)
    return segs


def check_line(input_segs, output_segs):
    seg_line = create_segments()
    for number in input_segs:
        what_poss = what_is_possible(number)
        if len(what_poss) == 1:
            for seg in number:
                seg_line[seg].limit_possibilities(number_to_letter[what_poss[0]])
    for number in output_segs:
        what_poss = what_is_possible(number)
        if len(what_poss) == 1:
            for seg in number:
                seg_line[seg].limit_possibilities(number_to_letter[what_poss[0]])

    # print status
    for seg in seg_line:
        print(f"{seg_line[seg].segment}: {seg_line[seg].possibilities}")

    # Check for cf
    exclude_cf = 0
    for seg in seg_line:
        if seg_line[seg].possibilities == ['c', 'f']:
            exclude_cf += 1
    if exclude_cf == 2:
        for seg in seg_line:
            if len(seg_line[seg].possibilities) > 2:
                seg_line[seg].strip_possibilities(['c', 'f'])

    # print status
    print("Possibilities")
    for seg in seg_line:
        print(f"{seg_line[seg].segment}: {seg_line[seg].possibilities}")

    # Check for bd
    exclude_cf = 0
    for seg in seg_line:
        if seg_line[seg].possibilities == ['b', 'd']:
            exclude_cf += 1
    if exclude_cf == 2:
        for seg in seg_line:
            if len(seg_line[seg].possibilities) > 2:
                seg_line[seg].strip_possibilities(['d', 'b'])

    # print status
    print("Possibilities")
    for seg in seg_line:
        print(f"{seg_line[seg].segment}: {seg_line[seg].possibilities}")


#     Check for singles:
    exclude_single = 0
    for seg in seg_line:
        if len(seg_line[seg].possibilities) == 1:
            for other_seg in seg_line:
                if len(seg_line[other_seg].possibilities) > 1:
                    seg_line[other_seg].strip_possibilities(seg_line[seg].possibilities)

    # print status
    print("Possibilities")
    for seg in seg_line:
        print(f"{seg_line[seg].segment}: {seg_line[seg].possibilities}")
    input()


def get_data(filename):
    global inputs, outputs
    inputs = []
    outputs = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
            line_split = line.split(' | ')
            inputs.append(line_split[0].split(' '))
            outputs.append(line_split[1].split(' '))

    return len(outputs)


def check_segment_lengths(segments: list, lengths: list):
    matches = 0
    for segment in segments:
        if len(segment) in lengths:
            matches += 1
    return matches


def remove_letters(original: str, to_remove: str):
    output = ""
    for letter in original:
        if letter not in to_remove:
            output += letter
    return output


def check_if_in(original: str, check_for: str):
    for letter in check_for:
        if letter not in original:
            return False
    return True


def combine(first, second):
    temp = first + second
    output = ""
    for character in temp:
        if character not in output:
            output += character

    return output


def decode_line(input_data: list, outputs_data: list):
    decoded = {}

    all_data = input_data
    all_data.extend(outputs_data)

    # Low hanginging fruit:
    for number in all_data:
        if len(what_is_possible(number)) == 1:
            decoded[what_is_possible(number)[0]] = number
    if len(decoded) != 4:
        print(f"Warning - decoded {len(decoded)} words - {decoded}")
    # Differences
    for number in all_data:
        if len(number) == 5:
            if check_if_in(number, decoded[1]):
                decoded[3] = number
            else:
                temp = remove_letters(decoded[4], decoded[1])
                if check_if_in(number, temp):
                    decoded[5] = number
                else:
                    decoded[2] = number
    decoded[9] = combine(decoded[1], decoded[5])
    decoded[6] = combine(remove_letters(decoded[8], decoded[1]), decoded[5])

    # Find zero
    for number in all_data:
        if find_match(number, decoded) is None:
            decoded[0] = number
    if len(decoded) != 10:
        print(f"Warning: decoded length = {len(decoded)} - {decoded}")
    return decoded


def find_match(find_item, encoding):
    for number in encoding:
        if len(find_item) == len(encoding[number]):
            if check_if_in(find_item, encoding[number]):
                return number
    return None


start = time.time()
total = get_data(filename)
print(f"Lines of data: {total}")

number_of_matches = 0
for line in outputs:
    number_of_matches += check_segment_lengths(line, matching_lengths)
print(f"Matches: {number_of_matches}")

# check_line(inputs[0], outputs[0])
print(f"{time.time() - start}s")
sum_outputs = 0
for line in range(len(outputs)):
    code = decode_line(inputs[line], outputs[line])
    # for line in code:
    #     print(f"{line}: {code[line]}")

    output = ""
    for item in outputs[line]:
        match = find_match(item, code)
        if match is None:
            print(f"No match for {item} in {code}")
        else:
            output += f"{match}"
    print(output)
    sum_outputs += int(output)
print(f"Sum outputs = {sum_outputs}")
print(f"{time.time() - start}s")

