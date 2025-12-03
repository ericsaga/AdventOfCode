from day_base import Day


class Day3(Day):
    def __init__(self):
        super().__init__(
            2025, 3, "Lobby", debug=False, expected_a=357, expected_b=3121910778619
        )

    def part_a(self):
        digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
        joltages = []
        for bank in self.input:
            occurences = set(bank[:-1])
            max_j = ""
            for _ in range(2):
                for finding_digit in digits:
                    if finding_digit in occurences:
                        max_j_index = bank.index(finding_digit)
                        max_j += finding_digit
                        bank = bank[max_j_index + 1 :]
                        occurences = set(bank)
                        break
            joltages.append(int(max_j))
        return sum(joltages)

    def part_b(self):
        digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
        joltages = []
        for bank in self.input:
            max_j = ""
            for round in range(12):
                missing_digits = 12 - len(max_j)
                margin = len(bank) - missing_digits
                new_bank = bank[: margin + 1]
                occurences = set(new_bank)
                for finding_digit in digits:
                    if finding_digit in occurences:
                        max_j_index = bank.index(finding_digit)
                        max_j += finding_digit
                        bank = bank[max_j_index + 1 :]
                        break
            joltages.append(int(max_j))
        return sum(joltages)


if __name__ == "__main__":
    (Day3()).run()

# def random():
#     digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
#     joltages = []
#     for bank in self.input:
#         occurences = set(bank)
#         max_j = ""
#         for _ in range(2):
#             for finding_digit in digits:
#                 if finding_digit in occurences:
#                     max_j_index = bank.index(finding_digit)
#                     max_j += finding_digit
#                     bank = bank[max_j_index+1:]
#                     occurences = set(bank)
#                     break
#         joltages.append(int(max_j))
