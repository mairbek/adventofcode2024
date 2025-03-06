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
    costs = {}
    min_score = None
    q = []
    heapq.heappush(q, (0, 0, si, sj, (0, 1), [(si, sj)]))
    items = set()
    while q:
        score, cost, i, j, dir, path = heapq.heappop(q)
        if grid[i][j] == '#':
            continue
        pos = (i, j, dir)
        if pos in costs and costs[pos] < score:
            continue
        costs[pos] = score
        if grid[i][j] == 'E':
            if not min_score or score == min_score:
                min_score = score
                for p in path:
                    items.add(p)
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
            heapq.heappush(q, (score + cost, cost, ni, nj, (di, dj), path + [(ni, nj)]))
    return min_score, items

n = len(grid)
m = len(grid[0])
start = None
end = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'E':
            end = (i, j)
        if start and end:
            break
    if start and end:
       break
if start and end:
    si, sj = start
    ei, ej = end
    score, items = find_route(grid, si, sj)
    for i, j in items:
        grid[i][j] = 'O'
    for row in grid:
        print(''.join(row))
    print(score, len(items))
