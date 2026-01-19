import sys
from collections import defaultdict, deque


def parse_input():
    """Parse the input data."""
    bricks = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Parse format: x1,y1,z1~x2,y2,z2
        left, right = line.split("~")
        x1, y1, z1 = map(int, left.split(","))
        x2, y2, z2 = map(int, right.split(","))
        bricks.append(((x1, y1, z1), (x2, y2, z2)))
    return bricks


def part1(bricks):
    """Solve part 1.

    Figure how the blocks will settle based on the snapshot.
    Once they've settled, consider disintegrating a single brick;
    how many bricks could be safely chosen as the one to get disintegrated?
    """
    # TODO: Implement solution
    print(bricks)
    bricks.sort(key=lambda x: x[0][2])
    xn, yn, zn = -1, -1, -1
    for (xa, ya, za), (xb, yb, zb) in bricks:
        print(f"Brick: ({xa}, {ya}, {za}) -> ({xb}, {yb}, {zb})")
        xn, yn, zn = max(xn, xa, xb), max(yn, ya, yb), max(zn, za, zb)
    print(xn, yn, zn)
    grid = [[-1] * (yn + 1) for _ in range(xn + 1)]
    max_height = [[0] * (yn + 1) for _ in range(xn + 1)]
    deps = defaultdict(set)
    # has_deps = set()
    for i, ((xa, ya, za), (xb, yb, zb)) in enumerate(bricks):
        print(za, zb)
        h = 0
        for x in range(xa, xb + 1):
            for y in range(ya, yb + 1):
                h = max(h, max_height[x][y])

        for x in range(xa, xb + 1):
            for y in range(ya, yb + 1):
                if max_height[x][y] == h and grid[x][y] >= 0:
                    deps[i].add(grid[x][y])
                    # has_deps.add(grid[x][y])
                grid[x][y] = i
                max_height[x][y] = h + zb - za + 1
    print(deps)
    keep = set()
    for i, dep in deps.items():
        if len(dep) == 1:
            (item,) = dep
            keep.add(item)
    print(len(bricks), len(keep))
    return len(bricks) - len(keep)


def part2(bricks):
    """Solve part 2."""
    bricks.sort(key=lambda x: x[0][2])
    xn, yn, zn = -1, -1, -1
    for (xa, ya, za), (xb, yb, zb) in bricks:
        xn, yn, zn = max(xn, xa, xb), max(yn, ya, yb), max(zn, za, zb)
    grid = [[-1] * (yn + 1) for _ in range(xn + 1)]
    max_height = [[0] * (yn + 1) for _ in range(xn + 1)]
    deps = defaultdict(set)
    inverted_deps = defaultdict(set)
    for i, ((xa, ya, za), (xb, yb, zb)) in enumerate(bricks):
        h = 0
        for x in range(xa, xb + 1):
            for y in range(ya, yb + 1):
                h = max(h, max_height[x][y])

        for x in range(xa, xb + 1):
            for y in range(ya, yb + 1):
                if max_height[x][y] == h and grid[x][y] >= 0:
                    deps[i].add(grid[x][y])
                    inverted_deps[grid[x][y]].add(i)
                    # has_deps.add(grid[x][y])
                grid[x][y] = i
                max_height[x][y] = h + zb - za + 1
    keep = set()
    for i, dep in deps.items():
        if len(dep) == 1:
            (item,) = dep
            keep.add(item)
    result = 0
    for item in keep:
        q = deque()
        q.append(item)
        visited = set()
        while q:
            d = q.popleft()
            if d in visited:
                continue
            visited.add(d)
            if d != item:
                result += 1
            for dep in inverted_deps[d]:
                if all(dd in visited for dd in deps[dep]):
                    q.append(dep)
    return result


if __name__ == "__main__":
    bricks = parse_input()
    print(f"Part 1: {part1(bricks)}")
    print(f"Part 2: {part2(bricks)}")
