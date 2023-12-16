def calc_num(queue: list, mappert):
    been = [[0 for _ in range(len(mappert[0]))] for _ in range(len(mappert))]
    been_set = set()
    while queue:
        loc, direction = queue.pop(0)
        while True:
            if loc[0] < 0 or loc[1] < 0 or loc[0] >= len(mappert) or loc[1] >= len(mappert[0]):
                break
            if (loc, direction) in been_set:
                break
            been_set.add((loc, direction))
            been[loc[0]][loc[1]] = 1
            if mappert[loc[0]][loc[1]] == '.':
                pass
            elif mappert[loc[0]][loc[1]] == '\\':
                direction = (direction[1], direction[0])
            elif mappert[loc[0]][loc[1]] == '/':
                direction = (-direction[1], -direction[0])
            elif mappert[loc[0]][loc[1]] == '|':
                if direction[0] == 0:
                    queue.append((loc, (1, 0)))
                    queue.append((loc, (-1, 0)))
                    break
            elif mappert[loc[0]][loc[1]] == '-':
                if direction[1] == 0:
                    queue.append((loc, (0, 1)))
                    queue.append((loc, (0, -1)))
                    break
            else:
                raise ValueError(mappert[loc[0]][loc[1]], 'not recognized')
            loc = (loc[0] + direction[0], loc[1] + direction[1])
    return sum([sum([1 for v in b if v != 0]) for b in been])


mappert = [list(line) for line in open('input.txt', 'r').read().split('\n') if line]
print(f'Part 1: {calc_num([((0, 0), (0, 1))], mappert)}')

max_val = 0
for index in range(len(mappert)):
    max_val = max(max_val, calc_num([((index, 0), (0, 1))], mappert))
    max_val = max(max_val, calc_num([((0, index), (1, 0))], mappert))
    max_val = max(max_val, calc_num([((index, len(mappert)-1), (0, -1))], mappert))
    max_val = max(max_val, calc_num([((len(mappert)-1, index), (-1, 0))], mappert))
print(f'Part 2: {max_val}')
