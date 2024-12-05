import sys
import numpy as np

lines = []
for line in sys.stdin:
    lines.append(line[:-1])

m = np.array([list(s) for s in lines])

visited = np.zeros_like(m, dtype=int)

def lookup_one(grid, word, di, dj):
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

def lookup_mas(grid):
    result = 0
    n = len(grid)
    m = len(grid[0])
    word = "MAS"
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] != 'A':
                continue
            one = ''.join([grid[i-1][j-1], grid[i][j], grid[i+1][j+1]])
            two = ''.join([grid[i+1][j-1], grid[i][j], grid[i-1][j+1]])
            if (one == word or one == word[::-1]) and (two == word or two == word[::-1]):
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
    c = lookup_one(lines, "XMAS", di, dj)
    print(di, dj, c)
    result += c
print(result)
print(lookup_mas(lines))
