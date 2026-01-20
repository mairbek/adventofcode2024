import sys

import networkx as nx


def parse_input():
    """Parse the input data."""
    graph = nx.Graph()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Parse format: jqt: rhn xhk nvd
        left, right = line.split(": ")
        neighbors = right.split()
        for neighbor in neighbors:
            graph.add_edge(left, neighbor, capacity=1)
    return graph


def part1(graph: nx.Graph):
    """Solve part 1.

    Find the three wires to disconnect that divide the components into
    two separate groups. Return the product of the sizes of these two groups.
    """
    nodes = list(graph.nodes)
    for i in range(1, len(nodes)):
        cut, partition = nx.minimum_cut(graph, nodes[0], nodes[i])
        print(f"{i}/{len(nodes)} cut {cut}")
        if cut == 3:
            a, b = partition
            return len(a) * len(b)
    return 0


if __name__ == "__main__":
    graph = parse_input()
    print(f"Part 1: {part1(graph)}")
