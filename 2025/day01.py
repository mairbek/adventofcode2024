import sys


def main():
    counter = 50
    result = 0

    for line in sys.stdin:
        direction = line.strip()[0]
        steps = int(line.strip()[1:])

        sign = 1 if direction == "R" else -1
        counter += sign * steps

        result += abs(counter // 100)
        counter %= 100

    print(result)


if __name__ == "__main__":
    main()
