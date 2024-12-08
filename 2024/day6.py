from day_base import Day
import tqdm

OBSTACLE = "#"
GUARD = "^"


def go_N(x, y):
    return x, y - 1


def go_NE(x, y):
    return x + 1, y - 1


def go_E(x, y):
    return x + 1, y


def go_SE(x, y):
    return x + 1, y + 1


def go_S(x, y):
    return x, y + 1


def go_SO(x, y):
    return x - 1, y + 1


def go_O(x, y):
    return x - 1, y


def go_NO(x, y):
    return x - 1, y - 1


moving_functions = [go_N, go_E, go_S, go_O]


def get_new_moving_function(current_function):
    return moving_functions[
        (moving_functions.index(current_function) + 1) % len(moving_functions)
    ]


def is_cell_obstacle(x, y, map, moving_function, x_dim, y_dim):
    new_x, new_y = moving_function(x, y)
    if is_cell_outside(new_x, new_y, x_dim, y_dim):
        return False
    else:

        return map[new_y][new_x] == OBSTACLE


def is_cell_outside(x, y, x_dim, y_dim):
    return x < 0 or y < 0 or x >= x_dim or y >= y_dim


class Day6(Day):

    def __init__(self):
        super().__init__(
            2024, 6, "Guard Gallivant", debug=False, expected_a=41, expected_b=6
        )

    def part_a(self):
        map = self.input
        y_dim = len(map)
        x_dim = len(map[0])

        y = [y for y in range(len(map)) if GUARD in map[y]][0]
        x = map[y].index(GUARD)
        movements = {(x, y)}

        moving_function = go_N
        while not is_cell_outside(x, y, x_dim, y_dim):
            while not is_cell_outside(x, y, x_dim, y_dim) and not is_cell_obstacle(
                x, y, map, moving_function, x_dim, y_dim
            ):
                x, y = moving_function(x, y)
                movements.add((x, y))
            moving_function = get_new_moving_function(moving_function)
        return len(movements) - 1

    def part_b(self) -> int:
        orig_map = self.input
        y_dim = len(orig_map)
        x_dim = len(orig_map[0])
        orig_map = [[x for x in line] for line in orig_map]
        starting_y = [y for y in range(len(orig_map)) if GUARD in orig_map[y]][0]
        starting_x = orig_map[starting_y].index(GUARD)

        loopable = 0

        for obst_y in tqdm.tqdm(range(y_dim)):
            for obst_x in range(x_dim):
                map = [[x for x in row] for row in orig_map]
                if map[obst_y][obst_x] == ".":
                    map[obst_y][obst_x] = "#"
                    x, y = starting_x, starting_y
                    moving_function = go_N
                    visited = {(starting_x, starting_y, moving_function)}
                    blocked = False
                    while not is_cell_outside(x, y, x_dim, y_dim) and not blocked:
                        blocked = False
                        while not is_cell_outside(
                            x, y, x_dim, y_dim
                        ) and not is_cell_obstacle(
                            x, y, map, moving_function, x_dim, y_dim
                        ):

                            if is_blocked(x, y, moving_function, visited):
                                loopable += 1
                                blocked = True
                                break
                            x, y = moving_function(x, y)
                            visited.add((x, y, moving_function))

                        moving_function = get_new_moving_function(moving_function)
        return loopable


def is_blocked(x, y, moving_function, visited):
    new_x, new_y = moving_function(x, y)
    return (new_x, new_y, moving_function) in visited


if __name__ == "__main__":
    (Day6()).run()
