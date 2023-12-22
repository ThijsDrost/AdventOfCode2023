from collections import OrderedDict


blocks = [[list(map(int, l[0].split(','))), list(map(int, l[1].split(',')))] for l in
          (line.split('~') for line in open('input.txt', 'r').read().split('\n') if line)]
sorted_blocks = sorted(blocks, key=lambda x: min(x[0][2], x[1][2]))

columns = {}
set_blocks = OrderedDict()
for index, block in enumerate(sorted_blocks):
    block_height = abs(block[0][2] - block[1][2]) + 1
    height = 0
    names = set()
    for x in range(block[0][0], block[1][0] + 1):
        for y in range(block[0][1], block[1][1] + 1):
            if x not in columns:
                columns[x] = {}
            if y not in columns[x]:
                columns[x][y] = []
            else:
                column_height, name = columns[x][y]
                if column_height > height:
                    height = column_height
                    names = {name}
                elif column_height == height:
                    names.add(name)
    set_blocks[index] = (names, set())
    for name in names:
        set_blocks[name][1].add(index)
    for x in range(block[0][0], block[1][0] + 1):
        for y in range(block[0][1], block[1][1] + 1):
            columns[x][y] = height + block_height, index

total, total2 = 0, 0
for block in set_blocks:
    falling = {block}
    queue = list(set_blocks[block][1])
    while queue:
        if (b := queue.pop(0)) in falling:
            continue
        if set_blocks[b][0].issubset(falling):
            falling.add(b)
            queue.extend(list(set_blocks[b][1]))
    total += 0 if len(falling) != 1 else 1
    total2 += len(falling) - 1

print("Part 1:", total)
print("Part 2:", total2)
