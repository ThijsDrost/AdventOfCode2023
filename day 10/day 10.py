from copy import deepcopy

lines = open('input.txt', 'r').read().split('\n')
mappert = [list(line) for line in lines if line]
s_loc = divmod(''.join(lines).index('S'), len(lines[0]))

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

node_dir_dict = {'L': ((-1, 0), (0, 1)), '|': ((-1, 0), (1, 0)), '-': ((0, -1), (0, 1)), 'J': ((-1, 0), (0, -1)),
                 '7': ((1, 0), (0, -1)), 'F': ((1, 0), (0, 1)), '.': ()}

nodes = []
been = set()
been.add(s_loc)
dirs = []
for d in directions:
    if (-d[0], -d[1]) in node_dir_dict[mappert[s_loc[0]+d[0]][s_loc[1]+d[1]]] != ' ':
        connections = node_dir_dict[mappert[s_loc[0]+d[0]][s_loc[1]+d[1]]]
        been.add((s_loc[0] + d[0], s_loc[1] + d[1]))
        dirs.append(d)
        if connections[0] == (-d[0], -d[1]):
            nodes.append(((s_loc[0] + d[0], s_loc[1] + d[1]), connections[1]))
        else:
            nodes.append(((s_loc[0] + d[0], s_loc[1] + d[1]), connections[0]))

for key, value in node_dir_dict.items():
    if (dirs[0] in value) and (dirs[1] in value):
        mappert[s_loc[0]][s_loc[1]] = key

distance = 1
while True:
    new_nodes = []
    for node in nodes:
        if (node[0][0]+node[1][0], node[0][1]+node[1][1]) not in been:
            connections = node_dir_dict[mappert[node[0][0]+node[1][0]][node[0][1]+node[1][1]]]
            been.add((node[0][0]+node[1][0], node[0][1]+node[1][1]))
            if connections[0] == (-node[1][0], -node[1][1]):
                new_nodes.append(((node[0][0]+node[1][0], node[0][1]+node[1][1]), connections[1]))
            else:
                new_nodes.append(((node[0][0]+node[1][0], node[0][1]+node[1][1]), connections[0]))
        else:
            print(f'Part 1: {distance+1} steps')
            break
    else:
        distance += 1
        nodes = new_nodes
        continue
    break

# %%
mappert_copy = deepcopy(mappert)
for i in range(len(mappert_copy)):
    for j in range(len(mappert_copy[0])):
        if (i, j) not in been:
            mappert_copy[i][j] = False
        else:
            mappert_copy[i][j] = True


inside_dict = {'J': {'F': True, 'L': False}, '7': {'F': False, 'L': True}}

filled = 0
for i, line in enumerate(mappert_copy):
    last = mappert[i][0] if ((mappert[i][0] in ('L', 'F')) and mappert_copy[i][0]) else None
    inside = True if ((mappert[i][0] == '|') and mappert_copy[i][0]) else False
    for index in range(1, len(line)):
        value = mappert[i][index]
        if not mappert_copy[i][index]:
            if inside:
                mappert_copy[i][index] = 2
                filled += 1
            last = None
            continue
        if value in ('L', 'F'):
            last = value
            continue
        if value == '-':
            continue
        if value in ('J', '7'):
            if inside_dict[value][last]:
                inside = not inside
            last = None
            continue
        if value == '|':
            inside = not inside
            last = None
            continue
print(f'Part 2: {filled}')
