import time
import heapq


def find_path_astar(mappert, max_dir, min_dir):
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    ref_mappert = [
        [{(x, y): int(2 ** 15) for x in directions for y in range(min_dir, max_dir + 1)} for _ in range(len(lines[0]))]
        for _ in
        range(len(lines))]
    queue = []
    heapq.heappush(queue, (0, (0, 0), (0, 0), 0, 0))
    dist_cost = min(map(min, mappert))
    lens = (len(mappert) - 1, len(mappert[0]) - 1)

    while queue:
        g, loc, last_dir, dir_num, cost = heapq.heappop(queue)

        if loc == lens:
            return cost

        for next_dir in directions:
            if next_dir == (-last_dir[0], -last_dir[1]) or (dir_num == max_dir and next_dir == last_dir):
                continue

            if next_dir != last_dir:
                next_loc = (loc[0] + min_dir * next_dir[0], loc[1] + min_dir * next_dir[1])
            else:
                next_loc = (loc[0] + next_dir[0], loc[1] + next_dir[1])
            if next_loc[0] < 0 or next_loc[1] < 0 or next_loc[0] > lens[0] or next_loc[1] > lens[1]:
                continue

            new_num = min_dir if next_dir != last_dir else dir_num + 1

            if next_dir != last_dir:
                new_cost = cost
                for i in range(1, min_dir + 1):
                    new_cost += mappert[loc[0] + i * next_dir[0]][loc[1] + i * next_dir[1]]
            else:
                new_cost = cost + mappert[next_loc[0]][next_loc[1]]

            if new_cost < ref_mappert[next_loc[0]][next_loc[1]][(next_dir, new_num)]:
                ref_mappert[next_loc[0]][next_loc[1]][(next_dir, new_num)] = new_cost
                g = new_cost + dist_cost*(lens[0]-next_loc[0] + lens[1]-next_loc[1])
                heapq.heappush(queue, (g, next_loc, next_dir, new_num, new_cost))
    return min(ref_mappert[-1][-1].values())


lines = [list(map(int, line)) for line in open('input.txt', 'r').read().split('\n') if line]
start = time.time()
print('Part 1: ', find_path_astar(lines, 3, 1), f' in {time.time() - start:.2f} s')
start = time.time()
print('Part 2: ', find_path_astar(lines, 10, 4), f' in {time.time() - start:.2f} s')
