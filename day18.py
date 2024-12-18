import sys
from collections import deque

# n = 7
n = 71
grid = [['.' for _ in range(n)] for _ in range(n)]

blocks = []
for line in sys.stdin:
    print(line)
    x = map(int, line.split(","))
    j, i = x
    blocks.append((i, j))
    grid[i][j] = '#'

for row in grid:
    print(''.join(row))

# result_path = None
# q = deque([[(0, 0)]])
# visited = set()
# while q:
#     path = q.popleft()
#     i, j = path[0]
#     if i == n - 1 and j == n - 1:
#         result_path = path
#         break
#     if grid[i][j] == '#':
#         continue
#     if (i, j) in visited:
#         continue
#     visited.add((i, j))
#     for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#         ni, nj = i + di, j + dj
#         if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == '.':
#             q.append([(ni, nj)] + path)
# print(result_path)
# if result_path:
#     for i, j in result_path:
#         grid[i][j] = '0'
#     for row in grid:
#         print(''.join(row))
#     print(len(result_path) - 1)

unionarr = [-1 if grid[i // n][i % n] == '#' else i for i in range(n * n)]
sizes = [-1 if unionarr[i] < 0 else 1 for i in range(n * n)]

def root(p):
    parent = unionarr[p]
    while parent != p:
        p = parent
        parent = unionarr[p]
    return p

def union(p, q):
    rootp = root(p);
    rootq = root(q);
    # pi, pj = p // n, p % n
    # qi, qj = q // n, q % n
    # print("union", (pi, pj), "[", rootp, "]", (qi, qj), "[", rootq, "]")

    if rootp == rootq:
        return
    if sizes[rootp] < sizes[rootq]:
        unionarr[rootp] = rootq
        sizes[rootq] += sizes[rootp]
    else:
        unionarr[rootq] = rootp
        sizes[rootp] += sizes[rootq]
    # print("union-post", (pi, pj), "[", root(p), "]", (qi, qj), "[", root(q), "]")

for i in range(n):
    for j in range(n):
        if grid[i][j] == '.':
            if i + 1 < n and grid[i + 1][j] == '.':
                union(i * n + j, (i + 1) * n + j)
            if j + 1 < n and grid[i][j + 1] == '.':
                union(i * n + j, i * n + j + 1)

# print(unionarr)

# print(n*n-1)
# print(root(0), root(n * n - 1))

bn = len(blocks)
bi, bj = None, None
for i in range(bn):
    ii = bn - 1 - i
    bi, bj = blocks[ii]
    p = bi * n + bj
    unionarr[p] = p
    sizes[p] = 1
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = bi + di, bj + dj
        if 0 <= ni < n and 0 <= nj < n:
            q = ni * n + nj
            if unionarr[q] >= 0:
                union(p, q)
    if root(0) == root(n * n - 1):
        break
print(bj, bi)
