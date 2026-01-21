import heapq
import sys


def part1(calories):
    return max(sum(c) for c in calories)


def part2(calories):
    return sum(heapq.nlargest(3, [sum(c) for c in calories]))


def main():
    calories = []
    window = []
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            calories.append(window)
            window = []
        else:
            window.append(int(line))
    if window:
        calories.append(window)

    print(f"Part 1 {part1(calories)}")
    print(f"Part 2 {part2(calories)}")


if __name__ == "__main__":
    main()
