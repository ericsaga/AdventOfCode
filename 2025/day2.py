from day_base import Day

class Day2(Day):

    def __init__(self):
        super().__init__(2025, 2, 'Gift Shop', debug=False, expected_a=1227775554, expected_b=4174379265)

    def part_a(self):
        invalid_ids = []
        for num_range in self.input[0].split(','):
            start, end = num_range.split('-')
            for i in range(int(start), int(end)+1):
                i = str(i)
                num_len = len(i)
                if num_len%2 == 0 and i[:int(num_len)//2] == i[int(num_len)//2:]:
                    invalid_ids.append(int(i))
        return sum(invalid_ids)

    def part_b(self):
        def find_factors(num):
            factors = []
            for x in range(1, num // 2 + 1):
                if num % x == 0:
                    factors.append(x)
            return factors

        invalid_ids = []
        for num_range in self.input[0].split(","):
            start, end = num_range.split("-")
            for num in range(int(start), int(end)+1):
                num = str(num)
                for seq_len in find_factors(len(num)):
                    potential_sequence = num[:seq_len]
                    if len(num)>1 and all([potential_sequence == num[i:i+seq_len] for i in range(seq_len, len(num), seq_len)]):
                        invalid_ids.append(int(num))
                        break
        return sum(invalid_ids)




if __name__ == '__main__':
    (Day2()).run()

