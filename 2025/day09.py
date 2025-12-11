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
    area = None
    visited = {}
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            ax, ay = positions[i]
            bx, by = positions[j]
            # print(ax, ay, bx, by)

            # cright = (ax, by) in positions or ray_cast_inside(
            #     xgrouped, ygrouped, ax, by
            # )
            # drigth = (bx, ay) in positions or ray_cast_inside(
            #     xgrouped, ygrouped, bx, ay
            # )
            # if not cright or not drigth:
            #     continue
            min_x, max_x = ax, bx
            if ax > bx:
                min_x, max_x = bx, ax
            incorrect = False
            for dx in range(min_x + 1, max_x):
                correct_by = (
                    visited.get((dx, by))
                    or (dx, by) in positions
                    or ray_cast_inside(xgrouped, ygrouped, dx, by)
                )
                visited[(dx, by)] = correct_by
                if not correct_by:
                    incorrect = True
                    break
                correct_ay = (
                    visited.get((dx, ay))
                    or (dx, ay) in positions
                    or ray_cast_inside(xgrouped, ygrouped, dx, ay)
                )
                visited[(dx, by)] = correct_ay
                if not correct_ay:
                    incorrect = True
                    break
            if incorrect:
                continue

            min_y, max_y = ay, by
            if ay > by:
                min_y, max_y = by, ay
            incorrect = False
            for dy in range(min_y + 1, max_y):
                correct_bx = (
                    visited.get((bx, dy))
                    or (bx, dy) in positions
                    or ray_cast_inside(xgrouped, ygrouped, bx, dy)
                )
                visited[(bx, dy)] = correct_bx
                if not correct_bx:
                    incorrect = True
                    break
                correct_ax = (
                    visited.get((ax, dy))
                    or (ax, dy) in positions
                    or ray_cast_inside(xgrouped, ygrouped, ax, dy)
                )
                visited[(ax, dy)] = correct_ax
                if not correct_ax:
                    incorrect = True
                    break
            if incorrect:
                continue
            result = rect(ax, ay, bx, by)
            if result > max_rect:
                max_rect = result
                area = (ax, ay, bx, by)
    print(area)
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
