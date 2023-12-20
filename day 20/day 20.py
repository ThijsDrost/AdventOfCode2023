from dataclasses import dataclass, field
from copy import deepcopy
import math


@dataclass
class Broadcaster:
    destinations: list[str]
    name: str
    origins: list[str] = field(default_factory=list)
    state: bool | dict[str, bool] = None

    def signal(self, signal: bool, origin: str):
        signals = []
        for destination in self.destinations:
            signals.append((destination, signal, self.name))
        return signals

    def tuple(self):
        if isinstance(self.state, dict):
            state = tuple((name, state) for name, state in self.state.items())
        else:
            state = self.state
        return self.name, state


@dataclass
class FlipFlop(Broadcaster):
    state: bool = False

    def signal(self, signal: bool, origin: str):
        if signal:
            return []
        self.state = not self.state
        return super().signal(self.state, origin)


@dataclass
class Conjunction(Broadcaster):
    def __post_init__(self):
        self.state = {name: False for name in self.origins}

    def signal(self, signal: bool, origin: str):
        self.state[origin] = signal
        state = not (sum(self.state.values()) == len(self.state))
        return super().signal(state, origin)


def read_input(loc, add_node: tuple[str], node_name='rx'):
    lines = [line.split(' -> ') for line in open(loc, 'r').read().split('\n') if line]
    nodes = {}
    conjunctions = {}
    for (name, destinations) in lines:
        destinations = destinations.split(', ')
        if name == 'broadcaster':
            nodes[name] = Broadcaster(destinations, name)
        elif name[0] == '%':
            name = name.removeprefix('%')
            nodes[name] = FlipFlop(destinations, name)
        elif name[0] == '&':
            name = name.removeprefix('&')
            conjunctions[name] = [destinations, []]
        else:
            raise ValueError(f'Unknown node type: {name}')
    for node in add_node:
        nodes[node] = Broadcaster([], node)
    for (name, destinations) in lines:
        destinations = destinations.split(', ')
        for dest in destinations:
            if dest in conjunctions:
                name = name.removeprefix('%').removeprefix('&')
                conjunctions[dest][1].append(name)
            else:
                nodes[dest].origins.append(name.removeprefix('%').removeprefix('&'))
    for name, (destinations, origins) in conjunctions.items():
        nodes[name] = Conjunction(destinations, name, origins=origins)
    while len(nodes[node_name].origins) == 1:
        node_name = nodes[node_name].origins[0]
    if not isinstance(nodes[node_name], Conjunction):
        raise ValueError(f'Last node `{node_name}` is not a conjunction, but a {type(nodes[node_name])}')
    return nodes, node_name


def step(nodes, initial=('broadcaster', False, 'init')):
    low, high = 0, 0
    signals = [initial]
    while signals:
        signal = signals.pop(0)
        if signal[1]:
            high += 1
        else:
            low += 1
        if signal[0] in nodes:
            signals.extend(nodes[signal[0]].signal(signal[1], signal[2]))
        else:
            print(f'Unknown node: {signal[0]}')
    return low, high


def previous_nodes(node):
    nodes = set()
    queue = [node]
    while queue:
        if (node := queue.pop(0)) in nodes:
            continue
        nodes.add(node)
        queue.extend(nodes2[node].origins)
    return nodes


def cycle_detectors(nodes, cycle_nodes, init):
    cycle_watched_nodes = [previous_nodes(cycle_node) for cycle_node in cycle_nodes]
    states = [{tuple(nodes[node].tuple() for node in watched_nodes): 0}
              for watched_nodes in cycle_watched_nodes]
    cycle_nums = [0 for _ in cycle_nodes]
    i = 1
    while True:
        step(nodes, initial=init)
        for j, watched_nodes in enumerate(cycle_watched_nodes):
            if cycle_nums[j] == 0:
                if (state := tuple((nodes[node].tuple() for node in cycle_watched_nodes[j]))) in states[j]:
                    cycle_nums[j] = i - states[j][state]
                    if states[j][state] != 1:
                        raise ValueError("Cycle doesn't cycle back to the beginning")
                else:
                    states[j][state] = i
        if all(cycle_nums):
            break
        i += 1
    return math.lcm(*cycle_nums)


nodes, prev_node = read_input('input.txt', add_node=('rx',))
nodes2 = deepcopy(nodes)
l_total, h_total = 0, 0
for i in range(1000):
    low, high = step(nodes)
    l_total += low
    h_total += high
print("Part 1: ", l_total*h_total)
print("Part 2: ", cycle_detectors(deepcopy(nodes2), nodes[prev_node].origins, ('broadcaster', False, 'init')))