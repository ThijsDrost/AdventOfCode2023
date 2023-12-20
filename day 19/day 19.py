def checker(nodes, input):
    node = 'in'
    while node not in ('R', 'A'):
        for rule in nodes[node]['rules']:
            category, comparer, value, destination = rule
            if comparer(input[category], value):
                node = destination
                break
        else:
            node = nodes[node]['return']
    return node


def node_check(nodes: dict, node: str, input: dict):
    if node == 'A':
        start = 1
        for value in input.values():
            start *= (value[-1] - value[0] + 1)
        return start
    if node == 'R':
        return 0

    total = 0
    for rule in nodes[node]['rules']:
        category, comparer, value, destination = rule
        if len(input[category]) == 0:
            continue
        lower, upper = comparer(input[category][0], value), comparer(input[category][-1], value)
        if lower and upper:
            return node_check(nodes, destination, input)
        elif (not lower) and (not upper):
            continue
        else:
            if comparer is less:
                input_out = input.copy()
                input_out[category] = [input[category][0], value-1]
                total += node_check(nodes, destination, input_out)
                input[category] = [value, input[category][-1]]
            if comparer is more:
                input_out = input.copy()
                input_out[category] = [value+1, input[category][-1]]
                total += node_check(nodes, destination, input_out)
                input[category] = [input[category][0], value]
    return total + node_check(nodes, nodes[node]['return'], input)


def less(a, b): return a < b
def more(a, b): return a > b


nodes = {}
values = []
with (open('input.txt', 'r') as file):
    while x := file.readline().removesuffix('\n'):
        name, rules = x.split('{')
        rules = rules.removesuffix('}').split(',')
        ruls = []
        for rule in rules:
            if '<' in rule:
                rule = rule.split('<')
                comparer = less
            elif '>' in rule:
                rule = rule.split('>')
                comparer = more
            else:
                return_val = rule
                continue
            value, destination = rule[1].split(':')
            ruls.append([rule[0].strip(), comparer, int(value), destination])
        nodes[name.strip()] = {'rules': ruls, 'return': return_val.strip()}
    while x := file.readline().removesuffix('\n'):
        name, vals = x.split('{')
        vals = vals.removesuffix('}').split(',')
        categories = {}
        for val in vals:
            val_name, value = val.split('=')
            categories[val_name.strip()] = int(value)
        values.append(categories)


print('Part 1: ', sum([sum(val.values()) for val in values if checker(nodes, val) == 'A']))
bounds = (1, 4000)
test_input = {'x': [bounds[0], bounds[1]], 'm': [bounds[0], bounds[1]],
              'a': [bounds[0], bounds[1]], 's': [bounds[0], bounds[1]]}
print('Part 2: ', node_check(nodes, 'in', test_input))
