import heapq
import sys
from collections import deque

pad_grid = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [".", "0", "A"],
]
pad_n = len(pad_grid)
pad_m = len(pad_grid[0])

track_grid = [
    [".", "^", "A"],
    ["<", "v", ">"],
]
track_n = len(track_grid)
track_m = len(track_grid[0])


def di_to_symbol(di, dj):
    if di == -1 and dj == 0:
        return "^"
    if di == 1 and dj == 0:
        return "v"
    if di == 0 and dj == -1:
        return "<"
    if di == 0 and dj == 1:
        return ">"
    raise ValueError(f"Invalid di, dj: {di}, {dj}")


def compute_moves(grid, si, sj, ei, ej, score_fn):
    n = len(grid)
    m = len(grid[0])
    q = deque()
    q = []
    heapq.heappush(q, (0, si, sj, ""))
    while q:
        cost, i, j, path = heapq.heappop(q)
        if i == -1 and j == -1:
            return cost, path
        if grid[i][j] == ".":
            continue
        if i == ei and j == ej:
            # special 'A' command in the end
            s = "A"
            prev = path[-1] if path else None
            score = score_fn(prev, s)
            npath = path + s
            heapq.heappush(q, (cost + score, -1, -1, npath))
            continue
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != ".":
                s = di_to_symbol(di, dj)
                prev = path[-1] if path else None
                score = score_fn(prev, s)
                npath = path + s
                heapq.heappush(q, (cost + score, ni, nj, npath))
    raise ValueError(f"No path from ({si}, {sj}) to ({ei}, {ej})")


max_depth = 25
track_moves = []
for depth in range(max_depth):
    track_moves.append({})
    for si in range(track_n):
        for sj in range(track_m):
            if track_grid[si][sj] == ".":
                continue
            for ei in range(track_n):
                for ej in range(track_m):
                    if track_grid[ei][ej] == ".":
                        continue
                    expand_fn = (
                        (lambda prev, s: 1)
                        if depth == 0
                        else lambda prev, s: track_moves[depth - 1][(prev or "A", s)]
                    )
                    pathlen, moves = compute_moves(
                        track_grid, si, sj, ei, ej, expand_fn
                    )
                    track_moves[depth][
                        (track_grid[si][sj], track_grid[ei][ej])
                    ] = pathlen

inputs = []
for line in sys.stdin:
    ls = line.strip()
    if not ls:
        break
    inputs.append(ls)

pad_moves = {}
for si in range(pad_n):
    for sj in range(pad_m):
        if pad_grid[si][sj] == ".":
            continue
        for ei in range(pad_n):
            for ej in range(pad_m):
                if pad_grid[ei][ej] == ".":
                    continue
                expand_fn = lambda prev, s: track_moves[max_depth - 1][(prev or "A", s)]
                pathlen, moves = compute_moves(pad_grid, si, sj, ei, ej, expand_fn)
                pad_moves[(pad_grid[si][sj], pad_grid[ei][ej])] = pathlen


def extract_number(input):
    numstr = "".join([i for i in input if i.isnumeric()])
    return int(numstr)


total = 0
for inp in inputs:
    prev = "A"
    result = 0
    for c in inp:
        pathlen = pad_moves[(prev, c)]
        result += pathlen
        prev = c
    total += result * extract_number(inp)

print(total)
