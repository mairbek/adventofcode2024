import re
import sys

import z3


def parse_input(lines):
    """Parse factory machine configurations.

    Each line contains:
    - Indicator light diagram in [square brackets]: [.##.]
    - Button wiring schematics in (parentheses): (3) (1,3) (2)
    - Joltage requirements in {curly braces}: {3,5,4,7}
    """
    machines = []

    for line in lines:
        # Extract indicator lights pattern
        lights_match = re.search(r"\[([.#]+)\]", line)
        if not lights_match:
            continue

        lights_pattern = lights_match.group(1)
        target_state = [1 if c == "#" else 0 for c in lights_pattern]

        # Extract button configurations
        buttons = []
        button_matches = re.findall(r"\(([0-9,]+)\)", line)
        for button_str in button_matches:
            indices = [int(x) for x in button_str.split(",")]
            buttons.append(indices)

        # Extract joltage requirements
        joltage_match = re.search(r"\{([0-9,]+)\}", line)
        joltages = []
        if joltage_match:
            joltages = [int(x) for x in joltage_match.group(1).split(",")]

        machines.append(
            {"target": target_state, "buttons": buttons, "joltages": joltages}
        )

    return machines


def solve_z3_part1(buttons, target_state):
    solver = z3.Optimize()
    n = len(buttons)

    press_counts = z3.IntVector("press_counts", n)
    for i in range(n):
        solver.add(press_counts[i] >= 0)

    press_distribution = []
    for i in range(n):
        distribution = [1 if j in buttons[i] else 0 for j in range(len(target_state))]
        press_distribution.append(distribution)

    for j in range(len(target_state)):
        solver.add(
            z3.Sum([press_distribution[i][j] * press_counts[i] for i in range(n)]) % 2
            == target_state[j]
        )
    total_presses = z3.Int("total_presses")
    solver.add(total_presses == z3.Sum([press_counts[i] for i in range(n)]))
    solver.minimize(total_presses)

    if solver.check() == z3.sat:
        model = solver.model()
        return model[total_presses].as_long()
    else:
        print("No solution found")

    return None


def part1(machines):
    """Calculate total minimum button presses for all machines."""
    total_presses = 0

    for machine in machines:
        target_state = machine["target"]
        buttons = machine["buttons"]
        min_presses = solve_z3_part1(buttons, target_state)
        assert min_presses is not None
        total_presses += min_presses

    return total_presses


def solve_z3(buttons, joltages):
    solver = z3.Optimize()
    n = len(buttons)

    press_counts = z3.IntVector("press_counts", n)
    for i in range(n):
        solver.add(press_counts[i] >= 0)

    press_distribution = []
    for i in range(n):
        distribution = [1 if j in buttons[i] else 0 for j in range(len(joltages))]
        press_distribution.append(distribution)

    for j in range(len(joltages)):
        solver.add(
            z3.Sum([press_distribution[i][j] * press_counts[i] for i in range(n)])
            == joltages[j]
        )
    total_presses = z3.Int("total_presses")
    solver.add(total_presses == z3.Sum([press_counts[i] for i in range(n)]))
    solver.minimize(total_presses)

    if solver.check() == z3.sat:
        model = solver.model()
        return model[total_presses].as_long()
    else:
        print("No solution found")

    return None


def part2(machines):
    total_presses = 0

    for machine in machines:
        x = solve_z3(machine["buttons"], machine["joltages"])
        assert x is not None
        total_presses += x

    return total_presses


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        lines.append(line)

    machines = parse_input(lines)

    result1 = part1(machines)
    print(f"part1={result1}")

    result2 = part2(machines)
    print(f"part2={result2}")


if __name__ == "__main__":
    main()
