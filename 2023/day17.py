import heapq
import sys


def parse_input():
    """Parse the input data."""
    data = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        data.append([int(c) for c in line])
    return data


def part1(grid):
    """Solve part 1.

    Find the path from top-left to bottom-right that minimizes heat loss.
    Constraints:
    - Can move at most 3 blocks in a single direction before turning 90 degrees
    - Cannot reverse direction
    - Heat loss is the sum of values of blocks entered (excluding starting block)
    """
    for row in grid:
        print(row)

    n = len(grid)
    m = len(grid[0])

    q = []

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        heapq.heappush(q, (0, di, dj, 1, di, dj, [(di, dj, di, dj, 1)]))

    visited = set()

    min_score, min_path = 1000000, []
    while q:
        score, i, j, moves, di, dj, path = heapq.heappop(q)
        if i < 0 or i >= n or j < 0 or j >= m:
            continue
        if (i, j, moves, di, dj) in visited:
            continue
        visited.add((i, j, moves, di, dj))
        new_score = score + grid[i][j]
        if i == (n - 1) and j == (m - 1):
            if new_score < min_score:
                min_score, min_path = new_score, path
        for ndi, ndj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_moves = moves
            if (ndi, ndj) == (-di, -dj):
                continue
            if (ndi, ndj) == (di, dj):
                new_moves += 1
                if new_moves > 3:
                    continue
            else:
                new_moves = 1
            # new_path = path.copy()
            ni, nj = i + ndi, j + ndj
            # new_path.append((ni, nj, ndi, ndj, new_moves))
            new_path = []
            heapq.heappush(q, (new_score, ni, nj, new_moves, ndi, ndj, new_path))
    return min_score, min_path


def part2(grid):
    """Solve part 2."""
    n = len(grid)
    m = len(grid[0])

    q = []

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        heapq.heappush(q, (0, di, dj, 1, di, dj, [(di, dj, di, dj, 1)]))

    visited = set()

    min_score, min_path = 1000000, []
    while q:
        score, i, j, moves, di, dj, path = heapq.heappop(q)
        if i < 0 or i >= n or j < 0 or j >= m:
            continue
        if (i, j, moves, di, dj) in visited:
            continue
        visited.add((i, j, moves, di, dj))
        new_score = score + grid[i][j]
        if i == (n - 1) and j == (m - 1):
            if new_score < min_score:
                min_score, min_path = new_score, path
        for ndi, ndj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_moves = moves
            if (ndi, ndj) == (-di, -dj):
                continue
            if (ndi, ndj) == (di, dj):
                new_moves += 1
                if new_moves > 10:
                    continue
            else:
                if moves < 4:
                    continue
                new_moves = 1
            # new_path = path.copy()
            ni, nj = i + ndi, j + ndj
            # new_path.append((ni, nj, ndi, ndj, new_moves))
            new_path = []
            heapq.heappush(q, (new_score, ni, nj, new_moves, ndi, ndj, new_path))
    return min_score, min_path


if __name__ == "__main__":
    data = parse_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
