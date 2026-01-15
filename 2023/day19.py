import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Part:
    x: int
    m: int
    a: int
    s: int

    def value_of(self, category):
        if category == "x":
            return self.x
        if category == "m":
            return self.m
        if category == "a":
            return self.a
        if category == "s":
            return self.s
        raise ValueError(f"uknown category {category}")


@dataclass
class Rule:
    condition: tuple[str, str, int] | None  # ('x', '>', 10) or ('m', '<', 50)
    destination: str  # other condition

    def apply(self, part: Part):
        if not self.condition:
            return self.destination
        # print(f"destination={self.destination}")
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
    # TODO: Implement part 1
    result = 0
    for part in parts:
        state = "in"
        while True:
            # print(f"part={part} state={state}")
            if state in ("A", "R"):
                break
            for rule in workflows[state]:
                new_state = rule.apply(part)
                # print(f"new state={new_state}")
                if new_state:
                    state = new_state
                    break

        if state == "A":
            # print(f"part={part}")
            result += part.x + part.m + part.a + part.s
    return result


def part2(workflows, parts):
    """Solve part 2."""
    # TODO: Implement part 2
    return 0


if __name__ == "__main__":
    workflows, parts = parse_input()
    print(f"Part 1: {part1(workflows, parts)}")
    print(f"Part 2: {part2(workflows, parts)}")
