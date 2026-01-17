import sys
from collections import defaultdict, deque


def parse_input():
    """Parse the input data."""
    modules = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Parse format: broadcaster -> a, b, c or %a -> b or &inv -> a
        left, right = line.split(" -> ")
        destinations = [d.strip() for d in right.split(", ")]

        if left == "broadcaster":
            modules[left] = ("broadcaster", destinations)
        elif left.startswith("%"):
            name = left[1:]
            modules[name] = ("flip-flop", destinations)
        elif left.startswith("&"):
            name = left[1:]
            modules[name] = ("conjunction", destinations)

    return modules


def part1(modules):
    """Solve part 1.

    Push the button 1000 times. Count the total number of low pulses
    and high pulses sent. Return the product of these two counts.
    """

    inputs = defaultdict(set)
    flip_flops = {}
    for name, (t, dest) in modules.items():
        for d in dest:
            inputs[d].add(name)
        if t == "flip-flop":
            flip_flops[name] = False
    storage = {}
    for name, (t, _) in modules.items():
        if t != "conjunction":
            continue
        for input in inputs[name]:
            storage[(name, input)] = "-low"
    counter = {"-low": 0, "-high": 0}

    def run_loop():
        q = deque()
        q.append(("button", "broadcaster", "-low"))
        while q:
            from_, name, pulse = q.popleft()
            counter[pulse] += 1
            if name == "output" or name not in modules:
                continue
            t, dest = modules[name]
            out_pulse = pulse
            skip = False
            if t == "flip-flop":
                if pulse == "-high":
                    skip = True
                    continue
                flip_flops[name] = not flip_flops[name]
                out_pulse = "-high" if flip_flops[name] else "-low"
            if t == "conjunction":
                storage[(name, from_)] = pulse
                out_pulse = "-low"
                for inp in inputs[name]:
                    if storage[(name, inp)] == "-low":
                        out_pulse = "-high"
                        break
            if skip:
                continue
            for d in dest:
                q.append((name, d, out_pulse))
        return counter

    for _ in range(1000):
        run_loop()
    print(counter)

    # bfs
    # process
    return counter["-low"] * counter["-high"]


def part2(modules):
    """Solve part 2.

    Find the fewest button presses to send a single low pulse to rx.
    rx is fed by a conjunction module. That conjunction sends low only
    when all its inputs are high. Find cycle length for each input.
    """
    from math import lcm

    inputs = defaultdict(set)
    flip_flops = {}
    for name, (t, dest) in modules.items():
        for d in dest:
            inputs[d].add(name)
        if t == "flip-flop":
            flip_flops[name] = False
    storage = {}
    for name, (t, _) in modules.items():
        if t != "conjunction":
            continue
        for input in inputs[name]:
            storage[(name, input)] = "-low"

    # Find the conjunction that feeds rx
    rx_feeder = list(inputs["rx"])[0]
    # Track when each input to rx_feeder first sends high
    visited = {}
    targets = set(inputs[rx_feeder])

    def run_loop(press_num):
        q = deque()
        q.append(("button", "broadcaster", "-low"))
        while q:
            from_, name, pulse = q.popleft()
            # Check if this is a high pulse going into rx_feeder
            if name == rx_feeder and pulse == "-high" and from_ not in visited:
                visited[from_] = press_num
            if name == "output" or name not in modules:
                continue
            t, dest = modules[name]
            out_pulse = pulse
            skip = False
            if t == "flip-flop":
                if pulse == "-high":
                    skip = True
                    continue
                flip_flops[name] = not flip_flops[name]
                out_pulse = "-high" if flip_flops[name] else "-low"
            if t == "conjunction":
                storage[(name, from_)] = pulse
                out_pulse = "-low"
                for inp in inputs[name]:
                    if storage[(name, inp)] == "-low":
                        out_pulse = "-high"
                        break
            if skip:
                continue
            for d in dest:
                q.append((name, d, out_pulse))

    press = 0
    while len(visited) < len(targets):
        press += 1
        run_loop(press)

    return lcm(*visited.values())


if __name__ == "__main__":
    modules = parse_input()
    print(f"Part 1: {part1(modules)}")
    print(f"Part 2: {part2(modules)}")
