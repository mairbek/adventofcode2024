import sys
from itertools import groupby
from pstats import SortKey
from this import s


def rect(ai, aj, bi, bj):
    di = abs(ai - bi) + 1
    dj = abs(aj - bj) + 1
    return di * dj


def parse_input(lines):
    """Parse the red tile positions."""
    positions = []
    for line in lines:
        coords = line.split(",")
        x, y = int(coords[0]), int(coords[1])
        positions.append((x, y))
    return positions


def part1(positions):
    """Find the largest rectangle using red tiles as opposite corners."""
    n = len(positions)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            ai, aj = positions[i]
            bi, bj = positions[j]
            max_area = max(rect(ai, aj, bi, bj), max_area)
    return max_area


def part2(positions):
    """TODO: Implement part 2 when revealed."""
    # TODO: Implement part 2
    n = len(positions)
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            pass
    return max(max(row) for row in grid)


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        lines.append(line)

    positions = parse_input(lines)

    result1 = part1(positions)
    print(f"part1={result1}")

    result2 = part2(positions)
    print(f"part2={result2}")


if __name__ == "__main__":
    main()


# %%
def ray_cast_inside(grouped, x, y):
    count = 0
    for ii, points in grouped.items():
        if ii > x:
            break
        points = sorted(points)
        for jj in range(1, len(points)):
            if y > points[jj - 1] and jj < points[jj]:
                print(
                    f"i={x}, j={y}, jj={jj}, points[jj-1]={points[jj - 1]}, points[jj]={points[jj]}"
                )
                count += 1
    return count % 2 == 1


positions = [(7, 1), (11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3)]
positions.sort(key=lambda x: x[1])

grouped = {
    k: {x for x, y in group} for k, group in groupby(positions, key=lambda x: x[1])
}
print(grouped)

grid = [["." for _ in range(14)] for _ in range(11)]
for x in range(14):
    for y in range(14):
        if ray_cast_inside(grouped, x, y):
            grid[y][x] = "X"

print("\n".join("".join(row) for row in grid))
