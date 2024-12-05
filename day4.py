import sys
import numpy as np

lines = []
for line in sys.stdin:
    lines.append(line[:-1])

m = np.array([list(s) for s in lines])

visited = np.zeros_like(m, dtype=int)

def lookup(grid, word, di, dj):
    result = 0
    n = len(grid)
    m = len(grid[0])
    wl = len(word)
    for i in range(n):
        for j in range(m):
            if (i + di * (wl - 1)) < 0 or (i + di * (wl - 1)) >= n:
                continue
            if (j + dj * (wl - 1)) < 0 or (j + dj * (wl - 1)) >= m:
                continue
            match = True
            for k in range(wl):
                if grid[i + di *k][j + dj*k] != word[k]:
                    match = False
                    break
            if match:
                result += 1
    return result

directions = [
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1),
    (0, -1),
    (-1, 0),
    (-1, -1),
    (-1, 1)
]

result = 0
for di, dj in directions:
    c = lookup(lines, "XMAS", di, dj)
    print(di, dj, c)
    result += c
print(result)
