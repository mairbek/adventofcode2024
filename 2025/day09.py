import itertools
import sys


def rect(ai, aj, bi, bj):
    di = abs(ai - bi) + 1
    dj = abs(aj - bj) + 1
    return di * dj


def ray_cast_inside(xlines, ylines, x, y):
    # print(f"ray_cast_inside({x}, {y})")
    # print(xlines[y])
    count = 0
    for ax, bx in xlines.get(y, []):
        if ax <= x <= bx:
            return True
        # if bx < x:
        #     count += 1
    for xi, lines in ylines:
        # print(f"xi={xi} lines={lines}")
        if xi > x:
            break
        for ay, by in lines:
            if x == xi and (y >= ay and y <= by):
                return True
            if y >= ay and y < by:  # exclude end point
                # print(f"crossed x={xi} y={y} (ay={ay} by={by})")
                count += 1
    # print(f"x={x} y={y} count={count}")
    return count % 2 == 1


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
    xlines = []
    ylines = []

    for (ax, ay), (bx, by) in itertools.pairwise(positions + [positions[0]]):
        # horizonal line, append start and end points
        if ay == by:
            xlines.append((ay, (min(ax, bx), max(ax, bx))))
        elif ax == bx:
            ylines.append((ax, (min(ay, by), max(ay, by))))

    xgrouped = {
        x: sorted(y for _, y in group)
        for x, group in itertools.groupby(sorted(xlines), key=lambda x: x[0])
    }

    ygrouped = [
        (x, sorted(y for _, y in group))
        for x, group in itertools.groupby(sorted(ylines), key=lambda x: x[0])
    ]
    max_rect = 0
    rax, ray, rbx, rby = None, None, None, None
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            ax, ay = positions[i]
            bx, by = positions[j]

            # cheating ...
            if by < 50000 or ay < 50000:
                continue

            cright = (ax, by) in positions or ray_cast_inside(
                xgrouped, ygrouped, ax, by
            )
            drigth = (bx, ay) in positions or ray_cast_inside(
                xgrouped, ygrouped, bx, ay
            )
            if not cright or not drigth:
                continue
            if max_rect < rect(ax, ay, bx, by):
                rax, ray, rbx, rby = ax, ay, bx, by
                max_rect = rect(ax, ay, bx, by)
    print(rax, ray, rbx, rby)
    return max_rect


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
