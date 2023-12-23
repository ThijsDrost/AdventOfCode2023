from collections import deque


def find_nodes(tiles, loc, initial=None, directional=True):
    directions = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
    x, y = loc
    nodes = []
    if initial is None:
        queue = deque([((x, y), (0, 0), 0)])
    else:
        queue = deque([initial])
    new_end = None
    is_node = False
    while queue:
        loc, last_dir, steps = queue.popleft()
        new = []
        if (not directional) or (tiles[loc[0]][loc[1]] == '.'):
            new_directions = directions.values()
        else:
            new_directions = (directions[tiles[loc[0]][loc[1]]],)

        for direction in new_directions:
            new_loc = (loc[0] + direction[0], loc[1] + direction[1])
            if direction == (last_dir[0] * -1, last_dir[1] * -1):
                continue
            if tiles[new_loc[0]][new_loc[1]] == '#':
                continue
            if new_loc[0] == 0:
                continue
            if new_loc[0] == len(tiles) - 1:
                new_end = ((x, y), steps + 1)
                continue
            new.append((new_loc, direction, steps + 1))

        if len(new) >= 2 or is_node:
            if steps != 0:
                nodes.append((loc, steps))
            else:
                queue.extend(new)
        else:
            queue.extend(new)

    if len(nodes) == 0 and new_end is None:
        raise ValueError('No paths', (x, y))
    found_end = True if new_end is not None else False
    new_end = ((0, 0), 0) if new_end is None else new_end
    return nodes, (found_end, new_end)


def do_part(loc, directional):
    tiles = [list(line) for line in open(loc, 'r').read().split('\n') if line]
    directions = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
    map_nodes = {}

    end = []
    for x in range(1, len(tiles)-1):
        for y in range(1, len(tiles[x])-1):
            if tiles[x][y] != '#':
                neighbors = 0
                for direction in directions.values():
                    if tiles[x + direction[0]][y + direction[1]] != '#':
                        neighbors += 1
                if neighbors > 2:
                    if tiles[x][y] != '.':
                        raise NotImplementedError('Slope at intersection')
                    nodes, ends = find_nodes(tiles, (x, y), directional=directional)
                    map_nodes[(x, y)] = nodes
                    if ends[0]:
                        end.append(ends[1])

    start_loc = (1, tiles[0].index('.'))
    start_nodes, *_ = find_nodes(tiles, start_loc, (start_loc, (1, 0), 1), directional)
    for ends in end:
        map_nodes[(ends[0][0], ends[0][1])].append(((-1, -1), ends[1]))

    paths = []
    queue = deque([(x[0], x[1], {x[0]}) for x in start_nodes])
    while queue:
        loc, steps, been = queue.popleft()
        if loc == (-1, -1):
            paths.append(steps)
            continue
        for node, node_steps in map_nodes[loc]:
            if node not in been:
                new_been = been.copy()
                new_been.add(node)
                queue.append((node, steps + node_steps, new_been))
    return max(paths)


print("Part 1:", do_part('input.txt', True))
print("Part 2:", do_part('input.txt', False))
