from day_base import Day

def get_orientation(a,b):
    return 'inc' if b - a > 0 else 'dec'

def is_lev_safe(a,b, stage_orientation):
    return 1<=b-a<=3 if stage_orientation == 'inc' else 1<=a-b<=3

def is_increasing(a,b):
    return b-a>0

class Day2(Day):

    def __init__(self):
        super().__init__(2024, 2, 'Red-Nosed Reports', debug=True)
        
    def part_a(self):
        pass

    def part_b(self):
        total = 0
        for line in self.input:
            already_good = False
            numbers = [int(x) for x in line.split(" ")]
            stage_orientation = get_orientation(numbers[0], numbers[1])
            stage_result = [is_lev_safe(a, b, stage_orientation) for a, b in zip(numbers[:], numbers[1:])]
            if stage_result.count(False) == 0:
                total += 1
                already_good = True

            else:
                for del_idx in range(len(numbers)):
                    if not already_good:
                        new_numbers = [int(x) for x in line.split(" ") if x != del_idx]
                        new_numbers.pop(del_idx)
                        stage_orientation = get_orientation(new_numbers[0], new_numbers[1])
                        stage_result = [is_lev_safe(a, b, stage_orientation) for a, b in
                                        zip(new_numbers[:], new_numbers[1:])]
                        if stage_result.count(False) == 0:
                            total += 1
                            already_good = True
        return total


if __name__ == '__main__':
    (Day2()).run()

