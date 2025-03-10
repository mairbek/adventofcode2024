import sys
from collections import deque
from collections import defaultdict

def fill(grid, si, sj):
    n = len(grid)
    m = len(grid[0])
    result = [[-1] * m for _ in range(n)]
    # print("fill", result)
    q = deque()
    q.append((si, sj, 0))
    while q:
        (i, j, d) = q.popleft()
        # print("i, j, d", i, j, d)
        if grid[i][j] == '#':
            continue
        if result[i][j] >= 0 and result[i][j] <= d:
            continue
        result[i][j] = d
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                q.append((ni, nj, d + 1))
    return result

def run(grid, distances, si, sj, ei, ej, target):
    n = len(grid)
    m = len(grid[0])
    result = []
    q = deque()
    q.append((si, sj, 0))
    visited = set()
    while q:
        (i, j, d) = q.popleft()
        if (i, j) in visited:
            continue
        if d >= target:
            continue
        visited.add((i, j))
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + 2*di, j + 2*dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            dd = distances[ni][nj]
            if dd < 0:
                continue
            dd += (d + 2)
            if dd <= target:
                result.append((dd, [(i+di, j+dj), (ni, nj)]))
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if distances[ni][nj] < 0:
                    continue
                q.append((ni, nj, d + 1))
    return result

grid = []
for line in sys.stdin:
    ls = line.strip()
    if not ls:
        break
    grid.append([c for c in ls])

si, sj = None, None
ei, ej = None, None

n = len(grid)
m = len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            si, sj = i, j
        if grid[i][j] == 'E':
            ei, ej = i, j

if si == None or sj == None or ei == None or ej == None:
    sys.exit(1)

def md_neighbours(i, j, n, m, d):
    for x in range(i - d, i + d + 1):
        diff = d - abs(x - i)
        possible_ys = {j - diff, j + diff}
        for y in possible_ys:
            if 0 <= x < n and 0 <= y < m:
                yield x, y

# TODO(mairbek): can be improved by building the path.
def num_skips(grid, sd, ed, max_skips, target):
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                continue
            for k in range(1, max_skips + 1):
                for ni, nj in md_neighbours(i, j, n, m, k):
                    if grid[ni][nj] == '#':
                        continue
                    d = sd[i][j] + ed[ni][nj] + k
                    if d <= target:
                        result.append((d, [(i, j), (ni, nj), k]))
    return result

ed = fill(grid, ei, ej)
sd = fill(grid, si, sj)
print(si, sj, ei, ej)
print(ed[si][sj])
print(sd[ei][ej])
min_distance = sd[ei][ej]
sk = num_skips(grid, sd, ed, 20, min_distance - 100)

breakdown = defaultdict(int)
for d, l in sorted(sk):
    breakdown[min_distance - d] += 1

print(len(sk))


# r = run(grid, distances, si, sj, ei, ej, distances[si][sj])
# count = 0
# for d, skip in sorted(r):
#     if (distances[si][sj] - d) >= 100:
#         count += 1
#         print(d, distances[si][sj] - d)
    # grid_copy = [row[:] for row in grid]
    # for i in range(len(skip)):
    #     pi, pj = skip[i]
    #     grid_copy[pi][pj] = str(i + 1)
    # for row in grid_copy:
    #     print(''.join(row))

# print(count)
