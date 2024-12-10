from linecache import updatecache

from day_base import Day


def calculate_checksum(blocks):
    final_map = []
    for id, times in blocks:
        final_map += [id] * times if id != -1 else [0] * times
    return sum([id * idx for id, idx in enumerate(final_map)])


class Day9(Day):

    def __init__(self):
        super().__init__(
            2024, 9, "Disk Fragmenter", debug=False, expected_a=1928, expected_b=2858
        )

    def part_a(self):
        disk_map = [int(x) for x in self.input[0]]
        blocks = [list(elem) for elem in enumerate(disk_map[0::2])]
        empty_spaces = disk_map[1::2]
        available_space = sum(empty_spaces)
        moved_blocks = 0
        current_slot = 1
        current_empty_space = 0
        while moved_blocks < available_space:
            num_movable = blocks[-1][1]
            num_available = empty_spaces[0]
            num_moving = min(num_movable, num_available)
            blocks.insert(current_slot, [blocks[-1][0], num_moving])

            if num_available < num_movable:

                blocks[-1][1] = blocks[-1][1] - num_moving
                empty_spaces.pop(current_empty_space)
                current_slot += 2

                if blocks[-1][1] == 0:
                    blocks.pop(-1)

            if num_available > num_movable:
                empty_spaces[current_empty_space] = (
                    empty_spaces[current_empty_space] - num_moving
                )
                blocks.pop(-1)
                current_slot += 1

            if num_movable == num_available:
                empty_spaces.pop(current_empty_space)
                current_slot += 2
                blocks.pop(-1)

            moved_blocks += num_moving
        calculate_checksum(blocks)

        return calculate_checksum(blocks)

    def part_b(self):
        disk_map = [int(x) for x in self.input[0]]
        blocks = [list(elem) for elem in enumerate(disk_map[0::2])]
        empty_spaces = disk_map[1::2]
        idx = 1
        for empty_space_len in empty_spaces:
            blocks.insert(idx, [-1, empty_space_len])
            idx += 2
        # input(available_space)

        i = -1
        while i > -1 * len(blocks):
            # filter out empty spaces
            if blocks[i][0] != -1:
                needed_space = blocks[i][1]
                j = 1
                while j < len(blocks) + i:
                    # make sure it is an empty block
                    if (
                        blocks[j][0] == -1
                        and (num_available := blocks[j][1]) >= needed_space
                    ):
                        blocks[j], blocks[i] = blocks[i], blocks[j]
                        # blocks.pop(i)
                        if num_available > needed_space:
                            blocks.insert(j + 1, [-1, num_available - needed_space])
                            blocks[i][1] = needed_space
                        break
                    else:
                        j += 1
            i -= 1

        calculate_checksum(blocks)

        return calculate_checksum(blocks)

        """
        #see from last block in blocks, how many I can move (num_movable)

        #see first slot in empty_spaces (num_available)

        #if num_available==num_movable
            moving = num_movable
            #move moving blocks to space current_slot - insert in position current_slot (id_movable, moving) of blocks

            #current slot += 2
            current_block  -= 1
            moved_blocks += moving
            blocks.pop(current_block)
            empty_spaces.pop(current_empty_space)
        # if num_available< num_movable
            moving = num_available
            #move moving block to space current_slot - insert in position current_slot (id_movable, moving)
            current_slot += 2
            empty_spaces.pop(current_slot)
            moved_blocks += moving
            blocks[current_block][1] = blocks[current_block][1]-moving

        if num_available>num_movable
            moving = num_movable
            # move moving block to space current_slot - insert in position current_slot (id_movable, moving)
            current_block -= 1
            blocks.pop(current_slot)
            empty_spaces[current_empty_space] = empty_spaces[current_empty_space] - moving
            moved_blocks += moving
        """

        print("")


if __name__ == "__main__":
    (Day9()).run()
