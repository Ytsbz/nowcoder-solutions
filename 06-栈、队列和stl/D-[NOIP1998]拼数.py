# 题目：[NOIP1998]拼数
# 题号：D
# 语言：Python3

from functools import cmp_to_key
n = int(input())
a = input().split()
def cmp(x, y):
    if x + y > y + x:
        return -1
    if x + y < y + x:
        return 1
    return 0
a.sort(key=cmp_to_key(cmp))
print("".join(a))
