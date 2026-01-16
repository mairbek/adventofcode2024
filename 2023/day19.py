import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Part:
    x: int
    m: int
    a: int
    s: int

    def value_of(self, category):
        if category not in ("x", "m", "a", "s"):
            raise ValueError(f"unknown category {category}")
        return getattr(self, category)


@dataclass
class Rule:
    condition: tuple[str, str, int] | None  # ('x', '>', 10) or ('m', '<', 50)
    destination: str  # other condition

    def apply(self, part: Part):
        if not self.condition:
            return self.destination
        category, cond, expected = self.condition
        if cond == ">" and part.value_of(category) > expected:
            return self.destination
        if cond == "<" and part.value_of(category) < expected:
            return self.destination
        return None


def parse_input():
    """Parse the input data."""
    workflows = {}
    parts = []

    parsing_workflows = True
    for line in sys.stdin:
        line = line.strip()
        if not line:
            parsing_workflows = False
            continue

        if parsing_workflows:
            # Parse workflow: px{a<2006:qkq,m>2090:A,rfg}
            name, rules_str = line.split("{")
            rules_str = rules_str.rstrip("}")
            rules = []

            for rule_str in rules_str.split(","):
                if ":" in rule_str:
                    # Conditional rule: "a<2006:qkq"
                    condition_str, destination = rule_str.split(":")
                    # Parse condition: "a<2006"
                    if "<" in condition_str:
                        attr, value = condition_str.split("<")
                        condition = (attr, "<", int(value))
                    else:  # '>'
                        attr, value = condition_str.split(">")
                        condition = (attr, ">", int(value))
                    rules.append(Rule(condition=condition, destination=destination))
                else:
                    # Default rule (no condition)
                    rules.append(Rule(condition=None, destination=rule_str))

            workflows[name] = rules
        else:
            # Parse part ratings: {x=787,m=2655,a=1222,s=2876}
            # Remove braces and split by comma
            ratings_str = line.strip("{}")
            ratings = {}
            for rating in ratings_str.split(","):
                key, value = rating.split("=")
                ratings[key] = int(value)
            part = Part(x=ratings["x"], m=ratings["m"], a=ratings["a"], s=ratings["s"])
            parts.append(part)

    return workflows, parts


def part1(workflows, parts):
    """Solve part 1.

    Sort through all of the parts you've been given; what do you get if you
    add together all of the rating numbers for all of the parts that
    ultimately get accepted?
    """
    result = 0
    for part in parts:
        state = "in"
        while True:
            if state in ("A", "R"):
                break
            for rule in workflows[state]:
                new_state = rule.apply(part)
                if new_state:
                    state = new_state
                    break

        if state == "A":
            result += part.x + part.m + part.a + part.s
    return result


def part2(workflows, _parts):
    """Solve part 2."""
    q = []
    q.append(("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}))
    visited = set()
    result = []
    while q:
        state, pr = q.pop()
        candidate = (state, tuple(sorted(pr.items())))
        if candidate in visited:
            continue
        visited.add(candidate)
        if state == "R":
            continue
        if state == "A":
            result.append(pr)
            continue
        pr = pr.copy()
        for rule in workflows[state]:
            if not rule.condition:
                q.append((rule.destination, pr))
                continue
            new_pr = pr.copy()
            category, cond, expected = rule.condition
            a, b = new_pr[category]
            aa, bb = a, b
            if cond == ">":
                a = max(a, expected + 1)
                bb = a - 1
            if cond == "<":
                b = min(b, expected - 1)
                aa = b + 1
            if a > b:
                continue
            new_pr[category] = (a, b)
            q.append((rule.destination, new_pr))
            if aa > bb:
                break
            pr[category] = (aa, bb)
    val_sum = 0
    for pr in result:
        val = 1
        val *= pr["x"][1] - pr["x"][0] + 1
        val *= pr["m"][1] - pr["m"][0] + 1
        val *= pr["a"][1] - pr["a"][0] + 1
        val *= pr["s"][1] - pr["s"][0] + 1
        val_sum += val
    return val_sum


if __name__ == "__main__":
    workflows, parts = parse_input()
    print(f"Part 1: {part1(workflows, parts)}")
    print(f"Part 2: {part2(workflows, parts)}")
