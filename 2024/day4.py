from day_base import Day

def go_N(x,y):
    return x, y-1
def go_NE(x,y):
    return x+1, y-1
def go_E(x,y):
    return x+1, y
def go_SE(x,y):
    return x+1, y+1
def go_S(x,y):
    return x, y+1
def go_SO(x,y):
    return x-1, y+1
def go_O(x,y):
    return x-1, y
def go_NO(x,y):
    return x-1, y-1

def is_cell_expected_value(text,x,y, expected_value, x_dim, y_dim):
    return x>=0 and y>=0 and x<x_dim and y<y_dim and text[y][x] == expected_value

directions = ["N","NE","E","SE","S","SO","O","NO"]

map_direction_to_function = {
    "N": go_N,"NE":go_NE,"E":go_E,"SE":go_SE,"S":go_S,"SO":go_SO,"O":go_O,"NO":go_NO
}
map_direction_to_function2 = {
    "NE":go_NE,"SE":go_SE,"SO":go_SO,"NO":go_NO
}
class Day4(Day):

    def __init__(self):
        super().__init__(2024, 4, 'Ceres Search', debug=False)
        
    def part_a(self):
        total = 0
        word = "XMAS"
        text = self.input
        y_dim = len(text)
        x_dim = len(text[0])
        for y in range(y_dim):
            for x in range(x_dim):
                if text[y][x] == "X":
                    for direction, function in map_direction_to_function.items():
                        ok_char = 1
                        potential_word = True
                        new_x = x
                        new_y = y
                        while potential_word and ok_char < 4:
                            new_x, new_y = function(new_x, new_y)
                            if is_cell_expected_value(text, new_x, new_y, word[ok_char], x_dim, y_dim):
                                ok_char += 1
                            else:
                                potential_word = False
                        if ok_char == 4:
                            total += 1
        return total
    def part_b(self):
        word = "MAS"
        found_mas = []
        text = self.input
        y_dim = len(text)
        x_dim = len(text[0])
        for y in range(y_dim):
            for x in range(x_dim):
                if text[y][x] == "M":
                    for direction, function in map_direction_to_function2.items():
                        ok_char = 1
                        potential_word = True
                        new_x = x
                        new_y = y
                        while potential_word and ok_char < 3:
                            new_x, new_y = function(new_x, new_y)
                            if is_cell_expected_value(text, new_x, new_y, word[ok_char], x_dim, y_dim):
                                ok_char += 1
                            else:
                                potential_word = False
                        if ok_char == 3:
                            found_mas.append(((x, y), (new_x, new_y)))
        total = 0
        found_mas = set(found_mas)
        for mas1 in found_mas:
            mx1, my1 = mas1[0]
            sx1, sy1 = mas1[1]

            for mas2 in found_mas:
                if mas1 != mas2:
                    mx2, my2 = mas2[0]
                    sx2, sy2 = mas2[1]
                    if (mx1 == mx2 and my1 == my2 + 2 and sx1 == sx2 and sy1 == sy2 - 2) or (
                            my1 == my2 and mx1 == mx2 + 2 and sy1 == sy2 and sx1 == sx2 - 2):
                        total += 1

        return total


if __name__ == '__main__':
    (Day4()).run()

