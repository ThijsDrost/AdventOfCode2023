lines = [list(line) for line in open('input.txt', 'r').read().split('\n')[0].split(',')]
boxes = {i: [] for i in range(256)}
total = 0
for lin in lines:
    value = 0
    for index, character in enumerate(lin):
        if character == '=':
            for b_index, lens in enumerate(boxes[value]):
                if lens[0] == lin[:index]:
                    boxes[value][b_index] = [lin[:index], int(''.join(lin[index + 1:]))]
                    break
            else:
                boxes[value].append([lin[:index], int(''.join(lin[index + 1:]))])
        if character == '-':
            for b_index, lens in enumerate(boxes[value]):
                if lens[0] == lin[:index]:
                    boxes[value].pop(b_index)
                    break
        value += ord(character)
        value *= 17
        value %= 256
    total += value
print("Part 1: ", total)
focussing_power = 0
for key, value in boxes.items():
    for i, v in enumerate(value):
        focussing_power += v[1]*(i+1)*(key+1)
print("Part 2: ", focussing_power)
