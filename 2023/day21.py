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


def part2(grid):
    """Solve part 2."""
    # TODO: Implement solution
    return 0


if __name__ == "__main__":
    grid = parse_input()
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")
