import sys

inputs = []
grid = []
for line in sys.stdin:
    ls = line.strip()
    if not ls:
        inputs.append(grid)
        grid = []
        continue
    grid.append(ls)
if grid:
    inputs.append(grid)

def parse_grid(g, top):
    result = []
    n = len(g)
    m = len(g[0])
    for j in range(m):
        v = 0
        rng = range(1, n) if top else range(n - 2, -1, -1)
        for i in rng:
            if g[i][j] == "#":
                v += 1
        if top:
            result.append(n - v - 1)
        else:
            result.append(v)
    return result

keys, locks = [], []
for g in inputs:
    if g[0][0] == "#":
        locks.append(parse_grid(g, True))
    else:
        keys.append(parse_grid(g, False))

print(keys)
print(locks)

result = 0
for k in keys:
    for l in locks:
        fits = True
        for i in range(len(k)):
            if l[i] <= k[i]:
                fits = False
                break
        if fits:
            result += 1
print(result)
