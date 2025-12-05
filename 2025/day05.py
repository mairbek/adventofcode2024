import sys


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
        ranges = []
    # Parse input: ranges, then blank line, then available IDs
    separator_idx = lines.index("")

    ranges = []
    for i in range(separator_idx):
        start, end = map(int, lines[i].split("-"))
        ranges.append((start, end))

    available_ids = []
    for i in range(separator_idx + 1, len(lines)):
        available_ids.append(int(lines[i]))

    count = 0
    for id in available_ids:
        for a, b in ranges:
            if id >= a and id <= b:
                count += 1
                break
    print(count)


if __name__ == "__main__":
    main()
