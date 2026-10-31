# 题目：涂小天与他的画
# 题号：1004
# 语言：Python3

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)
