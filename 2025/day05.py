import sys


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    # Parse input: ranges, then blank line, then available IDs
    separator_idx = lines.index("")

    ranges = []
    for i in range(separator_idx):
        start, end = map(int, lines[i].split("-"))
        ranges.append((start, end))

    available_ids = []
    for i in range(separator_idx + 1, len(lines)):
        available_ids.append(int(lines[i]))

    count = sum(1 for id in available_ids if any(a <= id <= b for a, b in ranges))
    print("part 1", count)

    # part two
    ranges.sort()
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent - merge
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    total = sum(end - start + 1 for start, end in merged)
    print("part 2", total)


if __name__ == "__main__":
    main()
