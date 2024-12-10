from day_base import Day


def go_N(x, y):
    return x, y - 1


def go_E(x, y):
    return x + 1, y


def go_S(x, y):
    return x, y + 1


def go_O(x, y):
    return x - 1, y


moving_functions = [go_N, go_E, go_S, go_O]


def coordinates_safe(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def parse_path(current_x, current_y, map, paths, current_path):
    current_value = map[current_y][current_x]
    needed_value = current_value + 1
    if current_value < 9:
        for moving_function in moving_functions:
            new_x, new_y = moving_function(current_x, current_y)
            if (
                coordinates_safe(new_x, new_y, len(map[0]), len(map))
                and map[new_y][new_x] == needed_value
            ):
                parse_path(
                    new_x,
                    new_y,
                    map,
                    paths,
                    current_path + [(new_x,new_y)],
                )
    if current_value == 9:
        paths.append(current_path)
        return


class Day10(Day):

    def __init__(self):
        super().__init__(2024, 10, "Hoof It", debug=False, expected_a=36)

    def part_a(self):
        map = [[int(x) for x in row] for row in self.input]
        width = len(map[0])
        height = len(map)
        total = 0
        for y in range(height):
            for x in range(width):
                if map[y][x] == 0:
                    paths = []
                    parse_path(x, y, map, paths, [(x, y)])
                    visited_9s = []
                    for path in paths:
                        if path[-1] not in visited_9s:
                            visited_9s.append(path[-1])
                    total += len(visited_9s)
        return total

    def part_b(self):
        map = [[int(x) for x in row] for row in self.input]
        width = len(map[0])
        height = len(map)
        total = 0
        for y in range(height):
            for x in range(width):
                if map[y][x] == 0:
                    paths = []
                    parse_path(x, y, map, paths, [(x, y)])
                    total += len(paths)
        return total


if __name__ == "__main__":
    (Day10()).run()
