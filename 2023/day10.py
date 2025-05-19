import math
import sys

grid = []
for line in sys.stdin:
    grid.append([c for c in line[:-1]])


directions = {
    'S': [(0, 1), (1, 0), (0, -1), (-1, 0)],
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(0, 1), (-1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)]
}

# checks if two points are connected.
def connected(ai, aj, bi, bj):
    di, dj = ai - bi, aj - bj
    if not (di, dj) in directions[grid[bi][bj]]:
        return False
    di, dj = bi - ai, bj - aj
    if not (di, dj) in directions[grid[ai][aj]]:
        return False
    return True

# find the starting point.
(si, sj) = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            si, sj = i, j
            break

# run the loop.
qi, qj = si, sj
visited = set()
distance = 0
while True:
    visited.add((qi, qj))
    found = False
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = qi + di, qj + dj
        if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[ni]):
            continue
        if not grid[ni][nj] in directions:
            continue
        if (ni, nj) in visited:
            continue
        if connected(qi, qj, ni, nj):
            qi, qj = ni, nj
            found = True
            break
    if not found:
        break
    distance += 1

print(math.ceil(distance / 2))
