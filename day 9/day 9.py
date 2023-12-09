def difference(values, operator):
    differences = [y-x for x, y in zip(values, values[1:])]
    if len(set(differences)) == 1:
        return operator(values, differences[0])
    else:
        return operator(values, difference(differences, operator))


lines = [list(map(int, line.split())) for line in open('input.txt').read().split('\n') if line]
print(f'part 1: {sum(list(map(lambda x: difference(x, lambda y, z: y[-1] + z), lines)))}')
print(f'part 12 {sum(list(map(lambda x: difference(x, lambda y, z: y[0] - z), lines)))}')