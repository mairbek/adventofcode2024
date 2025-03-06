import sys

def check_combo(options, combo):
    found = False
    for opt in options:
        if combo.startswith(opt):
            rest = combo[len(opt):]
            if rest == '':
                found = True
                break
            if check_combo(options, rest):
                found = True
                break
    return found


def check_combo_dp(options, combo):
    n = len(combo)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for opt in options:
            if i >= len(opt) and combo[i - len(opt):i] == opt:
                dp[i] += dp[i - len(opt)]
    return dp[n]

line = sys.stdin.readline().strip()
options = [s.strip() for s in line.split(',')]

# skip empty line
sys.stdin.readline()

combos = []
for line in sys.stdin:
    combos += [line.strip()]

print(' '.join(options))
for row in combos:
    print(row)


result = 0
for c in combos:
    ss = check_combo_dp(options, c)
    result += ss


print(result)
