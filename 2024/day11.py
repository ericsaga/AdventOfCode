from day_base import Day
from math import log10, floor
import tqdm

MULTIPLYING_CONSTANT = 2024


def has_even_num_digits(num):
    return get_number_digits(num) % 2 == 0


def get_number_digits(num):
    return floor(log10(num)) + 1


def split_number_in_half(num):
    power_10 = 10 ** (get_number_digits(num) / 2)
    return [int(num // power_10), int(num % power_10)]


def process_stone(num):
    if num == 0:
        return [1]
    elif has_even_num_digits(num):
        return split_number_in_half(num)
    else:
        return [num * MULTIPLYING_CONSTANT]


class Day11(Day):

    def __init__(self):
        super().__init__(2024, 11, 'Plutonian Pebbles', debug=False, expected_a=55312)

    def part_a(self):
        current_line = {int(x):1 for x in self.input[0].split(' ')}
        blinks = 25
        for _ in range(blinks):

            new_line = {}
            for (stone, count) in current_line.items():
                new_stones = process_stone(stone)
                for new_stone in new_stones:
                    new_line[new_stone] = new_line.get(new_stone,0) + count
            current_line = new_line
        return sum(count for count in current_line.values())

    def part_b(self):
        current_line = {int(x): 1 for x in self.input[0].split(' ')}
        blinks = 75
        for _ in range(blinks):

            new_line = {}
            for (stone, count) in current_line.items():
                new_stones = process_stone(stone)
                for new_stone in new_stones:
                    new_line[new_stone] = new_line.get(new_stone, 0) + count
            current_line = new_line
        return sum(count for count in current_line.values())


if __name__ == '__main__':
    (Day11()).run()
