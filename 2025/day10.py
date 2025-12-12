import itertools
import re
import sys
from pickletools import dis

import numpy as np
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


def minimal_solve_mod2(A, b, mod=2):
    """
    Find minimal solution to Ax = b in mod 2 (solution with fewest 1s).
    """
    A = np.array(A, dtype=int)
    if mod:
        A = A % mod
    b = np.array(b, dtype=int).flatten()
    if mod:
        b = b % mod

    m, n = A.shape
    aug = np.column_stack([A, b])

    # Gaussian elimination to RREF
    pivot_cols = []
    pivot_row = 0

    for col in range(n):
        # Find pivot
        pivot_idx = None
        for row in range(pivot_row, m):
            if aug[row, col] == 1:
                pivot_idx = row
                break

        if pivot_idx is None:
            continue

        if pivot_idx != pivot_row:
            aug[[pivot_row, pivot_idx]] = aug[[pivot_idx, pivot_row]]

        pivot_cols.append(col)

        # Eliminate
        for row in range(m):
            if row != pivot_row and aug[row, col] == 1:
                aug[row] = aug[row] + aug[pivot_row]
                if mod:
                    aug[row] %= mod

        pivot_row += 1

    # Check for inconsistency
    for i in range(pivot_row, m):
        if aug[i, -1] == 1:
            return None

    # Find free variables (columns without pivots)
    free_cols = [i for i in range(n) if i not in pivot_cols]

    # Try all combinations of free variables
    min_solution = None
    min_weight = None

    for free_vals in itertools.product([0, 1], repeat=len(free_cols)):
        x = np.zeros(n, dtype=int)

        # Set free variables
        for i, col in enumerate(free_cols):
            x[col] = free_vals[i]

        # Solve for pivot variables
        for i in range(len(pivot_cols)):
            col = pivot_cols[i]
            x[col] = aug[i, -1]
            for j in range(col + 1, n):
                if aug[i, j] == 1:
                    x[col] = x[col] + x[j]
                    if mod:
                        x[col] %= mod

        # Check if this is better
        weight = np.sum(x)
        if min_weight is None or weight < min_weight:
            min_weight = weight
            min_solution = x.copy()

    return min_solution


def part1(machines):
    """Calculate total minimum button presses for all machines."""
    total_presses = 0

    for machine in machines:
        target_state = np.array(machine["target"])
        buttons = machine["buttons"]
        buttons_arr = np.zeros((len(target_state), len(buttons)), dtype=int)

        for col_idx, idx_list in enumerate(buttons):
            buttons_arr[idx_list, col_idx] = 1

        min_presses = minimal_solve_mod2(buttons_arr, target_state)
        assert min_presses is not None
        total_presses += sum(min_presses)

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
