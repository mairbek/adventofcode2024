import re
import sys

pattern = r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don\'t)\(\)"

lines = []
for line in sys.stdin:
    lines.append(line)
lines = ''.join(lines)
matches = re.findall(pattern, lines)
result = 0
do = True
for match in matches:
    if match[0] == 'mul':
        x, y = int(match[1]), int(match[2])
        product = x * y
        if do:
            result += product
    elif match[3] == 'do':
        do = True
    else:
        do = False

print(result)
