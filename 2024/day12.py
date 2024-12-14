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
class Day12(Day):

    def __init__(self):
        super().__init__(2024, 12, 'Garden Groups', debug=True, expected_a=1930, expected_b=1206)
        
    def part_a(self):
        original_map = [[x for x in row] for row in self.input]
        height = len(original_map)
        width = len(original_map[0])
        id_map = [[-1 for _ in range(width)] for _ in range(height)]
        plot_id = 0
        plots = dict()


        for i in range(height):
            for j in range(width):
                if id_map[i][j] == -1:
                    current_letter = original_map[i][j]
                    parse_cell_part_a(j, i, plot_id, current_letter, original_map, id_map, plots, width, height)
                    plot_id +=1

        total = 0
        for id, plot in plots.items():
            total += len(plot["coords"]*plot["perimeter"])
        return total
    def part_b(self):
        original_map = [[x for x in row] for row in self.input]
        height = len(original_map)
        width = len(original_map[0])
        id_map = [[-1 for _ in range(width)] for _ in range(height)]
        plot_id = 0
        plots = dict()


        for i in range(height):
            for j in range(width):
                if id_map[i][j] == -1:
                    current_letter = original_map[i][j]
                    parse_cell_part_b(j, i, plot_id, current_letter, original_map, id_map, plots, width, height)
                    plot_id +=1

        total = 0
        for id, plot in plots.items():
            a = clean_perimeter(plot["perimeter"])
            total += len(plot["coords"])*len(clean_perimeter(plot["perimeter"]))
        return total
def clean_perimeter(list_perimeters):
    clean = list(set(list_perimeters))
    to_delete = []
    for elem in clean:
        if any([(elem[0]==x[0] and x[1]-1<=elem[1]<=x[1]+1) or (elem[1]==x[1] and x[0]-1<=elem[0]<=x[0]+1) for x in clean if x!=elem and x not in to_delete]):
            to_delete.append(elem)
    return [x for x in clean if x not in to_delete]

def parse_cell_part_a(x, y, plot_id, current_letter, original_map, id_map, plots, width, height):
    if id_map[y][x] == -1: #and original_map[y][x] == current_letter:
        id_map[y][x] = plot_id
        if plot_id not in plots:
            plots[plot_id] = {'coords':[],'perimeter':0}
        plots[plot_id]["coords"].append((y,x))
        for moving_function in moving_functions:
            new_x, new_y = moving_function(x, y)
            if coordinates_safe(new_x, new_y, width, height) and original_map[new_y][new_x] == current_letter and id_map[new_y][new_x] == -1:
                parse_cell_part_a(new_x,new_y,plot_id,current_letter,original_map, id_map, plots, width, height)
            elif not coordinates_safe(new_x, new_y, width, height) or original_map[new_y][new_x] != current_letter:
                plots[plot_id]["perimeter"] += 1
def parse_cell_part_b(x, y, plot_id, current_letter, original_map, id_map, plots, width, height):
    if id_map[y][x] == -1: #and original_map[y][x] == current_letter:
        id_map[y][x] = plot_id
        if plot_id not in plots:
            plots[plot_id] = {'coords':[],'perimeter':[]}
        plots[plot_id]["coords"].append((y,x))
        for moving_function in moving_functions:
            new_x, new_y = moving_function(x, y)
            if coordinates_safe(new_x, new_y, width, height) and original_map[new_y][new_x] == current_letter and id_map[new_y][new_x] == -1:
                parse_cell_part_b(new_x,new_y,plot_id,current_letter,original_map, id_map, plots, width, height)
            elif not coordinates_safe(new_x, new_y, width, height) or original_map[new_y][new_x] != current_letter:
                plots[plot_id]["perimeter"].append((new_x,new_y))


if __name__ == '__main__':
    ex = [(4, 7), (5, 8), (5, 8), (6, 9), (5, 10), (4, 10), (3, 9), (3, 8)]
    clean_perimeter(ex)
    (Day12()).run()

