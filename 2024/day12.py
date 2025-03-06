import sys

from collections import defaultdict

grid = []
for line in sys.stdin:
    grid.append([c for c in line[:-1]])

n = len(grid)
m = len(grid[0])

visited = [[0 for _ in range(m)] for _ in range(n)]

def count_seq(numbers):
    sorted_numbers = sorted(numbers)
    sequence_count = 0
    previous_number = None
    for num in sorted_numbers:
        if previous_number is None or num != previous_number + 1:
            sequence_count += 1
        previous_number = num
    return sequence_count


def run_dfs(i, j):
    char = grid[i][j]
    area = 0
    isides = defaultdict(set)
    jsides = defaultdict(set)
    q = [(i, j)]
    while q:
        i, j = q.pop()
        if visited[i][j] == 1:
            continue
        visited[i][j] = 1
        area += 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ii, jj = i + di, j + dj
            if ii >= 0 and ii < n and jj >= 0 and jj < m and grid[ii][jj] == char:
                q.append((ii, jj))
            else:
                if di == 0:
                    jsides[(j, dj)].add(i)
                elif dj == 0:
                    isides[(i, di)].add(j)
    total = 0
    for key, value in isides.items():
        count = count_seq(value)
        total += count
    for key, value in jsides.items():
        count = count_seq(value)
        total += count
    return (area, total)

total = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            continue
        (area, perimeter) = run_dfs(i, j)
        total += area * perimeter

print(total)
