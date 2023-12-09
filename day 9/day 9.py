def difference(values):
    differences = [y-x for x, y in zip(values, values[1:])]
    if len(set(differences)) == 1:
        return values[-1] + differences[-1]
    else:
        return values[-1] + difference(differences)

def difference_back(values):
    differences = [y-x for x, y in zip(values, values[1:])]
    if len(set(differences)) == 1:
        return values[0] - differences[0]
    else:
        return values[0] - difference_back(differences)


lines = [list(map(int, line.split())) for line in open('input.txt').read().split('\n') if line]
print(f'part 1: {sum(list(map(difference, lines)))}')
print(f'part 2: {sum(list(map(difference_back, lines)))}')