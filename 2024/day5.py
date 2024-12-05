from day_base import Day


class Day5(Day):
    #3892
    def __init__(self):
        super().__init__(2024, 5, 'description', debug=False)
        
    def part_a(self):
        separator = self.input.index("")
        rules = set([ tuple(rule.split('|')) for rule in self.input[:separator]])
        updates = [update.split(',') for update in self.input[separator+1:]]
        total = sum([ int(update[len(update)//2]) for update in updates if process_update(update, rules)])
        return total

    def part_b(self):
        separator = self.input.index("")
        rules = set([tuple(rule.split('|')) for rule in self.input[:separator]])
        updates = [update.split(',') for update in self.input[separator + 1:]]
        incorrect_updates = [update for update in updates if not process_update(update, rules)]
        corrected_updates = [swap_update(update, rules) for update in incorrect_updates]
        total = sum([int(update[len(update)//2]) for update in corrected_updates])

        # total = sum([ int(swap_update(update, rules)[len(swap_update(update, rules))//2]) for update in incorrect_updates])
        return total

def process_update(update, rules):
    potentially_ok = True
    i = 0
    while potentially_ok and i<len(update)-1:
        previous = update[:i]
        next = update[i+1:]
        current = update[i]
        for prev_number in previous:
            #check [prev, current] in rules, otherwise WRONG
            if (current, prev_number) in rules:
                potentially_ok = False
                break
            else:
                break
        for next_number in next:
            #check [current, next] in rules, otherwise wrong
            if (next_number, current) in rules:
                potentially_ok = False
                break
            else:
                break
        i += 1
    if potentially_ok and i == len(update)-1:
        return True

def swap_update(update, rules):
    i = 0
    to_flip =[]
    while i<len(update)-1:
        previous = update[:i]
        next = update[i+1:]
        current = update[i]
        for prev_number in previous:
            #check [prev, current] in rules, otherwise WRONG
            if (current, prev_number) in rules:
                idx_a, idx_b = i, update.index(prev_number)
                update[idx_a], update[idx_b] = update[idx_b], update[idx_a]
                i=0
                break
            else:
                break
        for next_number in next:
            #check [current, next] in rules, otherwise wrong
            if (next_number, current) in rules:
                idx_a, idx_b = i, update.index(next_number)
                update[idx_a], update[idx_b] = update[idx_b], update[idx_a]
                i=0
                break
            else:
                break
        i += 1
    return update

if __name__ == '__main__':
    (Day5()).run()

