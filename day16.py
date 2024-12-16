import sys
import heapq

grid = []
for line in sys.stdin:
    row = [c for c in line[:-1]]
    grid.append(row)

for row in grid:
    print(''.join(row))


def find_route(grid, si, sj):
    n = len(grid)
    m = len(grid[0])
    visited = set()
    q = []
    heapq.heappush(q, (0, si, sj, (0, 1)))
    while q:
        score, i, j, dir = heapq.heappop(q)
        if grid[i][j] == 'E':
            return score
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if grid[i][j] == '#':
            continue
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            cost = 1
            dot = di * dir[0] + dj * dir[1]
            if dot == 0:
                cost += 1000
            if dot == -1:
                continue
            heapq.heappush(q, (score + cost, ni, nj, (di, dj)))
    return None


n = len(grid)
m = len(grid[0])
start = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            start = (i, j)
            break
    if start:
       break
print(start)
if start:
    si, sj = start
    print(find_route(grid, si, sj))
else:
    print('No start point found')
