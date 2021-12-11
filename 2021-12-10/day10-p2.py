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

--- Part Two ---
Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

In the example above, there are five incomplete lines:

[({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
[(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
(((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
{<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
<{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
So, the last completion string above - ])}> - would be scored as follows:

Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
The five lines' completion strings have total scores as follows:

}}]])})] - 288957 total points.
)}>]}) - 5566 total points.
}}>}>)))) - 1480781 total points.
]]}}]}]}> - 995444 total points.
])}> - 294 total points.
Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.

Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?

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

missing_points = {
    None: 0,
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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


def read_in_line(line, return_stack=False):
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
    if return_stack:
        stack.append(expecting)
        return stack
    return None



illegal_total = 0
okay_lines = []
lines = get_data()
for line in lines:
    check = read_in_line(line)
    # print(f"{line}: \t\t{check}\t\t{illegal_points[check]}")
    print(f"{check}\t\t{illegal_points[check]}")
    if check:
        illegal_total += illegal_points[check]
    else:
        okay_lines.append(line)

print(f"Okay lines: {len(okay_lines)}")

missing_scores = []
for line in okay_lines:
    line_score = 0
    stack = read_in_line(line, return_stack=True)
    if stack:
        print(f"Stack length: \t\t{len(stack)}")
        while len(stack) > 0:
            line_score *= 5
            line_score += missing_points[stack[-1]]
            stack.pop()
    missing_scores.append(line_score)
    print(f"Line Score: \t\t{line_score}")

scores = len(missing_scores)
print(f"Missing scores: \t\t{len(missing_scores)}")

# Sort scores
missing_scores.sort()
print(missing_scores[int(scores/2)])


#
# for total in illegals:
#     print(f"{total}: {illegals[total]}\t{illegals[total] * illegal_points[total]}")
#     illegal_total += illegals[total] * illegal_points[total]

print(f"Illegal Points: \t\t{illegal_total}")
print(f"Total Lines:    \t\t{len(lines)}")


