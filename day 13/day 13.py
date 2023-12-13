def mirror(board):
    for i in range(1, len(board)):
        for uno, dos in zip(board[:i][::-1], board[i:]):
            if uno != dos:
                break
        else:
            return i
    return 0


def mirror2(board):
    for i in range(1, len(board)):
        difference = 0
        for j, (uno, dos) in enumerate(zip(board[:i][::-1], board[i:])):
            for u, d in zip(uno, dos):
                if u != d:
                    difference += 1
                if difference > 1:
                    break
        if difference == 1:
            return i
    return 0


lines = [list(line) for line in open('input.txt', 'r').read().split('\n')]
index = 0
total1 = 0
total2 = 0
while True:
    current = []
    found = 0
    while index < len(lines) and lines[index] != []:
        current.append(lines[index])
        index += 1
    index += 1

    total1 += 100*(z := mirror(current))

    current_t = list(map(list, zip(*current)))
    total1 += (z2 := mirror(current_t))

    t = mirror2(current)
    total2 += 100*t
    if t == 0:
        total2 += mirror2(current_t)

    if index >= len(lines):
        break

print(f"Part 1: {total1}")
print(f"Part 2: {total2}")
