import sys
from functools import cache


def parse_line(line):
    parts = line.split(" ")
    pattern, requirement = parts[0], parts[1]
    return pattern, [int(i) for i in requirement.split(",")]


def solve(pattern, requirement):
    @cache
    def rec(pattern_pos, req_pos):
        if pattern_pos >= len(pattern) and req_pos >= len(requirement):
            return 1
        if pattern_pos >= len(pattern):
            return 0
        skip = 0
        i = pattern_pos
        while i < len(pattern) and pattern[i] == ".":
            skip += 1
            i += 1
        if skip > 0:
            return rec(pattern_pos + skip, req_pos)
        if req_pos >= len(requirement):
            i = pattern_pos
            while i < len(pattern):
                if pattern[i] == "#":
                    break
                i += 1
            if i == len(pattern):
                return 1
            return 0
        req = requirement[req_pos]
        blocks = 0
        for i in range(req):
            ip = pattern_pos + i
            if ip >= len(pattern):
                break
            if pattern[ip] == ".":
                break
            blocks += 1
        result = 0
        if req == blocks:
            ip = pattern_pos + req
            if ip == len(pattern) or (ip < len(pattern) and pattern[ip] != "#"):
                result += rec(pattern_pos + req + 1, req_pos + 1)
        if pattern[pattern_pos] != "#":
            result += rec(pattern_pos + 1, req_pos)
        return result

    return rec(0, 0)


rows = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    rows.append(parse_line(line))

# Process and solve
result = 0
for row in rows:
    pattern, requirement = row
    pattern = "?".join([pattern] * 5)
    requirement *= 5
    r = solve(pattern, requirement)
    print(pattern, requirement, r)
    result += r

print(result)
