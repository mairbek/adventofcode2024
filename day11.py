import sys
from functools import lru_cache

nums = []
for line in sys.stdin:
    nums = [int(x) for x in line[:-1].split()]
    break
n = len(nums)

@lru_cache(maxsize=None)  # No limit on the cache size
def update_nums(num, b, n):
    nn = n - b
    for i in range(nn):
        s = str(num)
        if num == 0:
            num = 1
        elif len(s) % 2 == 0:
            mid = len(s) // 2
            l = int(s[:mid])
            r = int(s[mid:])
            result = 0
            result += update_nums(l, b + i + 1, n)
            result += update_nums(r, b + i + 1, n)
            return result
        else:
            num *= 2024
    return 1

r = 0
for i in range(n):
    r += update_nums(nums[i], 0, 75)
print(r)
