import sys

def check_valid(eq, i, prev, acc, r):
    if i == len(eq):
        return acc == r
    a = acc + eq[i]
    b = acc * eq[i]
    c = int(str(acc) + str(eq[i]))
    left = a <= r and check_valid(eq, i + 1, acc, a, r)
    right = b <= r and check_valid(eq, i + 1, acc, b, r)
    third = c <= r and check_valid(eq, i + 1, acc, c, r)

    return left or right or third


eqs = []
results = []
for line in sys.stdin:
    res, eq = line.split(':')
    results.append(int(res))
    eqs.append([int(s) for s in eq.split()])

sum = 0
for i in range(len(eqs)):
    if check_valid(eqs[i], 0, 0, 0, results[i]):
        sum += results[i]
print(sum)
