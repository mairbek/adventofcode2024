import sys

def check_safe(arr):
    all_increasing = True
    all_decreasing = True
    previous = None
    for a in arr:
        diff = 0
        if previous != None:
            if a > previous:
                all_decreasing = False
                diff = a - previous
            if a < previous:
                all_increasing = False
                diff = previous - a
        if not all_increasing and not all_decreasing:
            return False
        if previous != None and (diff == 0 or diff > 3):
            return False
        previous = a
    return True


reports = []
for line in sys.stdin:
    reports.append([int(a) for a in line.split()])

num_safe = 0
for i, l in enumerate(reports):
    if check_safe(l):
        num_safe += 1
    else:
        safe_unsafe = False
        for j, _  in enumerate(reports):
            if check_safe(l[:j]+l[j+1:]):
                safe_unsafe = True
                break
        if safe_unsafe:
            num_safe += 1
print(num_safe)
