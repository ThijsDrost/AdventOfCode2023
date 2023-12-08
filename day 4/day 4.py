loc = r'input.txt'
lines = [line for line in open(loc, 'r').read().split('\n') if line]

value = 0
nums = [1 for _ in range(len(lines))]
for index, line in enumerate(lines):
    winners, values = line.split(':')[1].split('|')
    winners = set((int(x) for x in winners.split()))
    values = set((int(x) for x in values.split()))
    # first part
    if (overlap := len(values.intersection(winners))) != 0:
        value += 2**(overlap - 1)
    # second part
    for i in range(1, len(values.intersection(winners))+1):
        nums[index + i] += nums[index]

print(value)
print(sum(nums))
