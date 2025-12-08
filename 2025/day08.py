import heapq
import sys


def parse_input(lines):
    """Parse the junction box positions."""
    positions = []
    for line in lines:
        coords = line.split(",")
        x, y, z = int(coords[0]), int(coords[1]), int(coords[2])
        positions.append((x, y, z))
    return positions


def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return dx * dx + dy * dy + dz * dz


def root(unionarr, p):
    parent = unionarr[p]
    while parent != p:
        p = parent
        parent = unionarr[p]
    return p


def union(unionarr, sizes, p, q):
    rootp = root(unionarr, p)
    rootq = root(unionarr, q)

    if rootp == rootq:
        return
    if sizes[rootp] < sizes[rootq]:
        unionarr[rootp] = rootq
        sizes[rootq] += sizes[rootp]
        return sizes[rootq]
    else:
        unionarr[rootq] = rootp
        sizes[rootp] += sizes[rootq]
        return sizes[rootp]


def part1(positions, rounds=10):
    """Connect the 1000 closest pairs of junction boxes and multiply the sizes of the three largest circuits."""
    n = len(positions)
    hq = []
    for i in range(n):
        for j in range(i + 1, n):
            heapq.heappush(hq, (distance(positions[i], positions[j]), i, j))
    unionar = [i for i in range(n)]
    sizes = [1 for _ in range(n)]

    for _ in range(rounds):
        _, p, q = heapq.heappop(hq)
        union(unionar, sizes, p, q)

    # Find the three largest sizes
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def part2(positions):
    n = len(positions)
    hq = []
    for i in range(n):
        for j in range(i + 1, n):
            heapq.heappush(hq, (distance(positions[i], positions[j]), i, j))
    unionar = [i for i in range(n)]
    sizes = [1 for _ in range(n)]

    rp, rq = None, None
    while True:
        _, p, q = heapq.heappop(hq)
        s = union(unionar, sizes, p, q)
        if s == len(unionar):
            rp = positions[p][0]
            rq = positions[q][0]
            break
    return rp * rq


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        lines.append(line)

    positions = parse_input(lines)

    result1 = part1(positions, rounds=10)
    print(f"part1={result1}")

    result2 = part2(positions)
    print(f"part2={result2}")


if __name__ == "__main__":
    main()
