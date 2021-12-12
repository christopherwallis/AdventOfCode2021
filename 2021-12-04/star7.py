"""
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

Your puzzle answer was 67716.

--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

Your puzzle answer was 1830.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
from dataclasses import dataclass

filename = 'input1.txt'
initialised = False
call_numbers = []


@dataclass
class BingoNumber:
    value: int
    called: bool


class BingoCard:
    def __init__(self, line_data: list, index_number: int):
        self.index_number = index_number
        self.won = None
        self.line_data = []
        self.winning_number = None
        if not self.check_data_integrity(line_data):
            raise IOError(f"Bad input data: {line_data}")
        self.bingo_data = []
        self.convert_to_bingo()

    def check_data_integrity(self, line_data):
        if len(line_data) == 5:
            if len(line_data) != 5:
                return False
            for line in line_data:
                new_line_data = []

                for item in line[0].split(' '):
                    try:
                        new_line_data.append(int(item))
                    except ValueError:
                        pass
                if len(new_line_data) == 5:
                    self.line_data.append(new_line_data)
                else:
                    raise IOError(f"New line data length = {len(new_line_data)}")
        return True

    def convert_to_bingo(self):
        for line in self.line_data:
            bingo_line = []
            for item in line:
                bingo_line.append(BingoNumber(item, False))
            self.bingo_data.append(bingo_line)

    def check_for_bingo(self):
        # Check horizontals
        for line in self.bingo_data:
            check = 0
            for item in line:
                if item.called:
                    check += 1
            if check == 5:
                return True
            else:
                # print(f"Check: {check}")
                check = 0
        # Check verticals
        for col in range(len(self.bingo_data[0])):
            for line in self.bingo_data:
                if line[col].called:
                    check += 1
                else:
                    continue
            if check == 5:
                return True
            else:
                check = 0
                # print(f"Check = {check}")

        # No bingo
        return False

    def call_number(self, number_called):
        for row in self.bingo_data:
            for item in row:
                if item.value == number_called:
                    item.called = True

    def sum_of_uncalled(self):
        sum = 0
        for row in self.bingo_data:
            for item in row:
               if not item.called:
                   sum += item.value
        return sum


def get_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        return data


def parse_data(data):
    # Get bingo numbers to call
    global call_numbers
    for number in data[0].split(','):
        try:
            call_numbers.append(int(number))
        except ValueError:
            pass

    # Get bingo cards
    bingo_cards = []
    count = 0

    bingo_data = data[1:]
    card_data = []
    for line in bingo_data:
        data_parsed = line.strip("\n")
        if data_parsed == "":
            if len(card_data) != 0:
                bingo_cards.append(BingoCard(card_data, count))
                count += 1
            card_data = []
        else:
            card_data.append(data_parsed.split(","))
    bingo_cards.append(BingoCard(card_data, count))
    return bingo_cards


def get_last_winner(cards):
    worst = 0
    worst_card = None
    for card in cards:
        if card.won > worst:
            worst = card.won
            worst_card = card
    return worst_card


def call_all_numbers(cards):
    count = 0
    total_cards = len(cards)
    # Call numbers
    for number in call_numbers:
        for card in cards:
            card.call_number(number)
            if card.check_for_bingo():
                if not card.won:
                    print("Bingo")
                    card.won = count
                    card.winning_number = number
                    if count == total_cards:
                        return cards
                    count += 1
    raise IOError("Ran out of numbers before all cards won")
    return False


data = get_data(filename)
all_cards = parse_data(data)
winners = call_all_numbers(all_cards)
# sum = winner[0].sum_of_uncalled()
# print(sum)
# print(winner[1])
# print(f"Multipled: {sum * winner[1]}")
loser = get_last_winner(winners)
print(f"Loser: {loser.index_number}")
print(f"Winning number: {loser.winning_number}")
print(f"Sum of uncalled: {loser.sum_of_uncalled()}")

print("//////////////////////////////////////////")
print(f"Multiplication: {loser.winning_number * loser.sum_of_uncalled()}")