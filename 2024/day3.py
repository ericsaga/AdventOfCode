from day_base import Day
import re

regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
def find_closest_value_smaller(value, idxs_list):
    return max(x for x in idxs_list if x < value)


def get_orientation(a,b):
    return 'inc' if b - a > 0 else 'dec'

def is_lev_safe(a,b, stage_orientation):
    return 1<=b-a<=3 if stage_orientation == 'inc' else 1<=a-b<=3

def is_increasing(a,b):
    return b-a>0

class Day3(Day):

    def __init__(self):
        super().__init__(2024, 3, 'Mull It Over', debug=True)
        
    def part_a(self):
        text = '\n'.join(self.input)
        results = re.findall(regex, text)
        return sum([int(a) * int(b) for a, b in results])

    def part_b(self):
        text = '\n'.join(self.input)
        regex_dos = "(do\(\))"
        regex_donts = "(don't\(\))"

        dos = re.finditer(regex_dos, text)
        donts = re.finditer(regex_donts, text)
        dos_idxs = [0] + [x.start() for x in dos]
        donts_idxs = [-1] + [x.start() for x in donts]

        results = re.finditer(regex, text)
        potential_muls = [(x.start(), (int(x.group(1)), int(x.group(2)))) for x in results]

        total = 0
        for (value, (a, b)) in potential_muls:
            closest_do = find_closest_value_smaller(value, dos_idxs)
            closest_dont = find_closest_value_smaller(value, donts_idxs)
            if closest_do > closest_dont:
                total += a * b

        return total


if __name__ == '__main__':
    (Day3()).run()

