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
    print("part 1", count)

    # part two
    ranges.sort()

    total = 0
    st = []
    for i in range(len(ranges)):
        a, b = ranges[i]
        total += b - a + 1
        while st:
            aa, bb = st.pop()
            if a <= bb:
                total -= bb - a + 1
                if b < bb:
                    total += bb - b
                    b = bb
                a = aa
        st.append((a, b))
    print("part 2", total)


if __name__ == "__main__":
    main()
