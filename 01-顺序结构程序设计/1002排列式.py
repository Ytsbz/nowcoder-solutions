# 题目：排列式
# 题号：1002
# 语言：Python3
def num(a, b, c):
    数字出现次数 = [0] * 10
    for v in (a, b, c):
        while v:
            数字出现次数[v % 10] += 1
            v //= 10
    for d in range(1, 10):
        if 数字出现次数[d] != 1:
            return False
    return 数字出现次数[0] == 0

for c in range(1, 10000):
    a = 2
    while a * a <= c:
        if c % a == 0 and num(a, c // a, c):
            print("%d = %d x %d" % (c, a, c // a))
        a += 1
