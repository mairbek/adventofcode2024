import sys
from itertools import combinations

import z3


def parse_input():
    """Parse the input data."""
    hailstones = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Parse format: px, py, pz @ vx, vy, vz
        pos_part, vel_part = line.split(" @ ")
        px, py, pz = [int(x.strip()) for x in pos_part.split(",")]
        vx, vy, vz = [int(x.strip()) for x in vel_part.split(",")]
        hailstones.append(((px, py, pz), (vx, vy, vz)))
    return hailstones


def find_intersection(h1, h2):
    (px1, py1, _), (vx1, vy1, _) = h1
    (px2, py2, _), (vx2, vy2, _) = h2
    det = vx2 * vy1 - vx1 * vy2
    if det == 0:
        return None
    dx = px2 - px1
    dy = py2 - py1
    t1 = (vx2 * dy - vy2 * dx) / det
    t2 = (vx1 * dy - vy1 * dx) / det
    if t1 < 0 or t2 < 0:
        return None
    x = px1 + t1 * vx1
    y = py1 + t1 * vy1
    return (x, y)


def part1(hailstones):
    """Solve part 1.

    Considering only the X and Y axes, check all pairs of hailstones'
    future paths for intersections. Return how many of these intersections
    occur within the test area (200000000000000 to 400000000000000).
    """
    # blow, bhigh = 7, 27
    blow, bhigh = 200000000000000, 400000000000000
    result = 0
    for h1, h2 in combinations(hailstones, 2):
        intersection = find_intersection(h1, h2)
        if not intersection:
            continue
        x, y = intersection
        if blow <= x <= bhigh and blow <= y <= bhigh:
            result += 1
    return result


def part2(hailstones):
    """Solve part 2."""
    solver = z3.Solver()
    px, py, pz = z3.Ints("px py pz")
    vx, vy, vz = z3.Ints("vx vy vz")

    for i, ((ipx, ipy, ipz), (ivx, ivy, ivz)) in enumerate(hailstones):
        ti = z3.Int(f"t{i}")
        solver.add(ti >= 0)
        solver.add(px + ti * vx == ipx + ivx * ti)
        solver.add(py + ti * vy == ipy + ivy * ti)
        solver.add(pz + ti * vz == ipz + ivz * ti)

    if solver.check() == z3.sat:
        model = solver.model()
        rpx = model.eval(px).as_long()  # type: ignore
        rpy = model.eval(py).as_long()  # type: ignore
        rpz = model.eval(pz).as_long()  # type: ignore
        return rpx + rpy + rpz
    return 0


if __name__ == "__main__":
    hailstones = parse_input()
    print(f"Part 1: {part1(hailstones)}")
    print(f"Part 2: {part2(hailstones)}")
