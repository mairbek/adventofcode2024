import sys

inputs = []
for line in sys.stdin:
    inputs.append([int(c) for c in line.strip().split()])


def solve(input):
    diffs = [input]
    while True:
        all_zeros = True
        diff = []
        source = diffs[-1]
        for j in range(1, len(source)):
            val = source[j] - source[j - 1]
            diff.append(val)
            all_zeros &= val == 0
        source = diff
        diffs.append(diff)
        if all_zeros:
            break
    n = len(diffs)
    # part 1
    # s = 0
    # ll = []
    # for i in range(n-1, -1, -1):
    #     s += diffs[i][-1]
    #     ll.append(s)
    s = 0
    ll = []
    for i in range(n-1, -1, -1):
        s = diffs[i][0] - s
        ll.append(s)
    # print(ll)
    return s
s = 0
for inp in inputs:
    s += solve(inp)
print(s)
