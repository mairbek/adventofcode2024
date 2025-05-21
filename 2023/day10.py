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
visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
distance = 0
while True:
    visited[qi][qj] = 1
    found = False
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = qi + di, qj + dj
        if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[ni]):
            continue
        if not grid[ni][nj] in directions:
            continue
        if visited[ni][nj] != 0:
            continue
        if connected(qi, qj, ni, nj):
            qi, qj = ni, nj
            found = True
            break
    if not found:
        break
    distance += 1

print(math.ceil(distance / 2))

# for each non visited, run point in polygon ray cast.
total_in = 0
for i in range(len(visited)):
    intersections = 0
    for j in range(len(visited[i])):
        # 'S' is tricky and might not work. see example 4.
        if visited[i][j] == 1 and grid[i][j] in ['S', '|', 'L', 'J']:
            intersections += 1
        elif visited[i][j] == 0:
            if intersections % 2 == 1:
                visited[i][j] = 2
                total_in += 1
for row in visited:
    print(row)

print(total_in)
# TODO Reddit's favorite Pick's & Shoelace https://www.reddit.com/r/adventofcode/comments/18evyu9/comment/kcqmhwk/?utm_source=share&utm_medium=web2x&context=3
