"""
--- Day 10: Syntax Scoring ---
You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.
So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
[[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
<{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
Stop at the first incorrect closing character on each corrupted line.

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

To begin, get your puzzle input.
"""
import re


healthy = 0
missing = 0
corrupt = 0
other = 0

illegal_points = {
    None: 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

illegals = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0
}

from dataclasses import dataclass

filename = 'input.txt'


def get_data():
    output = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        output.append(line)
    return output

def read_in_line(line):
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    stack = []
    expecting = None
    for character in line:
        # Check for opening characters
        if character in opening:
            for bracket in range(len(opening)):
                if character == opening[bracket]:
                    if expecting:
                        stack.append(expecting)
                    expecting = closing[bracket]

        # Check for closing characters
        elif character in closing:
            if character == expecting:
                if len(stack) == 0:
                    expecting = None
                else:
                    expecting = stack[-1]
                    stack.pop()
            else:
                return character
    return None


# def check_line(line):
#     illegal = {
#         ')': 0,
#         ']': 0,
#         '}': 0,
#         '>': 0
#     }
#     global healthy, corrupt, missing, other, illegals
#
#     for character in line:
#         if character == '(':
#             illegal[')'] += 1
#         if character == ')':
#             illegal[')'] -= 1
#
#         if character == '[':
#             illegal[']'] += 1
#         if character == ']':
#             illegal[']'] -= 1
#
#         if character == '{':
#             illegal['}'] += 1
#         if character == '}':
#             illegal['}'] -= 1
#
#         if character == '<':
#             illegal['>'] += 1
#         if character == '>':
#             illegal['>'] -= 1
#
#     # Check for missing
#     # if sum(illegal.values()) != 0:
#     #     for value in illegal.values():
#     #         if value < 0:
#     #             break
#     #     else:
#     #         missing += 1
#             # return 3
#
#
#     # Check for OK
#
#
#     # Check for corrupt
#     print(f"{line}: \t\t{illegal}")
#     for key in illegal:
#         if illegal[key] < 0:
#             corrupt += 1
#             illegals[key] -= illegal[key]
#
#     for value in illegal.values():
#         if value != 0:
#             return 1
#     healthy += 1
#     return 0


illegal_total = 0
lines = get_data()
for line in lines:
    check = read_in_line(line)
    # print(f"{line}: \t\t{check}\t\t{illegal_points[check]}")
    print(f"{check}\t\t{illegal_points[check]}")
    if check:
        illegal_total += illegal_points[check]
#
# for total in illegals:
#     print(f"{total}: {illegals[total]}\t{illegals[total] * illegal_points[total]}")
#     illegal_total += illegals[total] * illegal_points[total]

print(f"Total: {illegal_total}")
print(len(lines))

