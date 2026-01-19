import sys


def parse_input():
    """Parse the input data."""
    grid = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        grid.append(list(line))
    return grid


def convert(c):
    if c == ">":
        return 0, 1
    if c == "<":
        return 0, -1
    if c == "^":
        return -1, 0
    if c == "v":
        return 1, 0
    return None


def part1(grid):
    """Solve part 1.

    Find the longest hike through the hiking trails.
    Paths (.), forest (#), and steep slopes (^, >, v, <).
    On slopes, must move in the direction of the arrow.
    Never step on the same tile twice.
    """
    for row in grid:
        print("".join(row))
    n, m = len(grid), len(grid[0])
    si, sj = 0, 0
    ei, ej = n - 1, m - 1
    for j in range(m):
        if grid[0][j] == ".":
            sj = j
        if grid[n - 1][j] == ".":
            ej = j
    q = []
    q.append((si, sj, {(si, sj)}))
    max_path = 0
    while q:
        i, j, path = q.pop()
        # print(i, j, path)
        if (i, j) == (ei, ej):
            max_path = max(max_path, len(path))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if (ni, nj) in path:
                continue
            new_path = path.copy()
            new_path.add((ni, nj))
            if (
                0 <= ni < n
                and 0 <= nj < m
                and (grid[ni][nj] == "." or (di, dj) == convert(grid[ni][nj]))
            ):
                q.append((ni, nj, new_path))

    return max_path - 1


def compress_grid(grid):
    """Compress grid into weighted graph of junctions only."""
    n, m = len(grid), len(grid[0])

    # Find start and end
    si, sj = 0, next(j for j in range(m) if grid[0][j] == ".")
    ei, ej = n - 1, next(j for j in range(m) if grid[n - 1][j] == ".")

    def neighbors(i, j):
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != "#":
                yield ni, nj

    # Junctions: 3+ neighbors, plus start/end
    junctions = {(si, sj), (ei, ej)}
    for i in range(n):
        for j in range(m):
            if grid[i][j] != "#" and len(list(neighbors(i, j))) >= 3:
                junctions.add((i, j))

    # Build graph: junction -> [(other_junction, distance), ...]
    graph = {j: [] for j in junctions}
    for start in junctions:
        q = [(start, 0)]
        visited = {start}
        while q:
            (i, j), dist = q.pop(0)
            if (i, j) != start and (i, j) in junctions:
                graph[start].append(((i, j), dist))
                continue
            for ni, nj in neighbors(i, j):
                if (ni, nj) not in visited:
                    visited.add((ni, nj))
                    q.append(((ni, nj), dist + 1))

    return graph, (si, sj), (ei, ej)


def part2(grid):
    graph, start, end = compress_grid(grid)

    max_path = 0

    def dfs(node, visited, dist):
        nonlocal max_path
        if node == end:
            max_path = max(max_path, dist)
            return
        for next_node, edge_dist in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                dfs(next_node, visited, dist + edge_dist)
                visited.remove(next_node)

    dfs(start, {start}, 0)
    return max_path


if __name__ == "__main__":
    grid = parse_input()
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")
