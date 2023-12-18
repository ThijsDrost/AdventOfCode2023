def distancer(directions, distances):
    total = 0
    y = 0
    for direction, distance in zip(directions, distances):
        if direction == 'L':
            total += int(distance) * (y + 0.5)
        elif direction == 'R':
            total -= int(distance) * (y - 0.5)
        elif direction == 'U':
            total += 0.5 * int(distance)
            y -= int(distance)
        elif direction == 'D':
            total += 0.5 * int(distance)
            y += int(distance)
    return int(total) + 1


def decode(lines):
    directions = [0 for _ in range(len(lines))]
    distances = ['' for _ in range(len(lines))]
    dir_dict = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    for index, (_, _, value) in enumerate(lines):
        distances[index] = int(value[2:7], 16)
        directions[index] = dir_dict[value[7]]
    return directions, distances


lines = [line.split() for line in open('input.txt', 'r').read().split('\n') if line]
directions, distances = [line[0] for line in lines], [line[1] for line in lines]
print(f'Part 1: {distancer(directions, distances)}')
print(f'Part 2: {distancer(*decode(lines))}')
