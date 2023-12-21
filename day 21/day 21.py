def read_input(loc: str) -> (tuple[tuple[int, ...], ...], tuple[int, int]):
    grid = [list(line) for line in open(loc, 'r').read().split('\n') if line]

    start = 0, 0
    for index, line in enumerate(grid):
        if 'S' in line:
            start = index, line.index('S')
            break
    grid[start[0]][start[1]] = '.'
    if start == (0, 0):
        raise Exception('No start found')
    grid = tuple(tuple(line) for line in grid)
    return grid, start


def spots(grid: tuple[tuple[int, ...], ...], steps: int, start: tuple[int, int], start_steps: int):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    num = 0
    been = set()
    queue = [(start, start_steps)]
    grid_len = len(grid)
    while queue:
        loc = queue.pop(0)
        if loc[1] % 2 == steps % 2:
            num += 1
        if loc[1] == steps:
            continue
        for direction in directions:
            new_loc = loc[0][0] + direction[0], loc[0][1] + direction[1]
            if (grid[new_loc[0] % grid_len][new_loc[1] % grid_len] == '.') and (new_loc not in been):
                been.add(new_loc)
                queue.append((new_loc, loc[1] + 1))
    if steps % 2 == 0:
        num -= 1
    return num


grid, start = read_input('input.txt')
print('Part 1:', spots(grid, 64, start, 0) - 1)

values = [spots(grid, 65, start, 0), spots(grid, 65 + 131, start, 0), spots(grid, 65 + 131 * 2, start, 0)]
vals = [values[0] / 2 - values[1] + values[2] / 2, -3 * (values[0] / 2) + 2 * values[1] - values[2] / 2, values[0]]
target = int((26_501_365 - 65) / 131)
print('Part 2:', int(vals[0]) * target ** 2 + int(vals[1]) * target + int(vals[2]))
