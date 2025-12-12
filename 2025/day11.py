import sys


def parse_input(lines):
    graph = {}
    for line in lines:
        if not line:
            continue
        parts = line.split(": ")
        device = parts[0]
        outputs = parts[1].split() if len(parts) > 1 else []
        graph[device] = outputs
    return graph


def part1(graph):
    # print(f"graph={graph}")

    count = 0
    q = ["you"]
    while q:
        device = q.pop()
        if device == "out":
            count += 1
            continue
        for output in graph[device]:
            q.append(output)
    return count


def dfs(graph, source, seen_fft, seen_dac, visited):
    if (source, seen_fft, seen_dac) in visited:
        return visited[(source, seen_fft, seen_dac)]
    if source == "out":
        return 1 if seen_fft and seen_dac else 0
    count = 0
    print(source)
    for neighbor in graph[source]:
        if neighbor not in visited:
            count += dfs(
                graph,
                neighbor,
                seen_fft or source == "fft",
                seen_dac or source == "dac",
                visited,
            )
    visited[(source, seen_fft, seen_dac)] = count
    return count


def part2(graph):
    count = 0
    visited = {}
    count = dfs(graph, "svr", False, False, visited)
    return count


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        lines.append(line)

    graph = parse_input(lines)

    # result1 = part1(graph)
    # print(f"part1={result1}")

    result2 = part2(graph)
    print(f"part2={result2}")


if __name__ == "__main__":
    main()
