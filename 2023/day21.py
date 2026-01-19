import sys
from collections import deque


def parse_input():
    """Parse the input data."""
    grid = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        grid.append(line)
    return grid


def part1(grid):
    """Solve part 1.

    Starting from the garden plot marked S on your map, how many garden
    plots could the Elf reach in exactly 64 steps?
    """
    # TODO: Implement solution
    for row in grid:
        print(row)
    si, sj = -1, -1
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                si, sj = i, j
                break

    q = deque()

    result = set()
    q.append((si, sj, 0))
    visited = set()
    while q:
        item = q.popleft()
        if item in visited:
            continue
        visited.add(item)
        i, j, steps = item
        if steps == 64:
            result.add((i, j))
            continue
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != "#":
                q.append((ni, nj, steps + 1))

    return len(result)


def bfs_count(grid, si, sj, max_steps):
    """Count reachable plots at exactly max_steps using BFS on infinite grid."""
    rows, cols = len(grid), len(grid[0])

    # Use two sets: current positions and next positions
    current = {(si, sj)}

    for step in range(max_steps):
        next_positions = set()
        for i, j in current:
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                # Use modulo only for grid lookup
                gi = ni % rows
                gj = nj % cols
                if grid[gi][gj] != "#":
                    next_positions.add((ni, nj))
        current = next_positions

    return len(current)


def part2(grid):
    """Solve part 2.

    The grid is 131x131 with S at center (65, 65).
    Target: 26501365 = 65 + 131 * 202300

    The reachable count grows quadratically with the number of grid-widths traveled.
    We sample at n=0,1,2 (steps 65, 196, 327) and fit a quadratic.
    """
    rows, _cols = len(grid), len(grid[0])

    # Find starting position
    si, sj = -1, -1
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                si, sj = i, j
                break

    size = rows  # 131
    offset = si  # 65 (S is at center)

    # Sample at 3 points: n=0, n=1, n=2
    f0 = bfs_count(grid, si, sj, offset)
    f1 = bfs_count(grid, si, sj, offset + size)
    f2 = bfs_count(grid, si, sj, offset + size * 2)

    print(f"f(0) = {f0} at {offset} steps")
    print(f"f(1) = {f1} at {offset + size} steps")
    print(f"f(2) = {f2} at {offset + size * 2} steps")

    # Fit quadratic: f(n) = a*n^2 + b*n + c
    # c = f(0)
    # a = (f(2) - 2*f(1) + f(0)) / 2
    # b = f(1) - f(0) - a
    c = f0
    a = (f2 - 2 * f1 + f0) // 2
    b = f1 - f0 - a

    print(f"Quadratic: {a}n² + {b}n + {c}")

    n = (26501365 - offset) // size
    print(f"n = {n}")

    return a * n * n + b * n + c


if __name__ == "__main__":
    grid = parse_input()
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")
