# 题目：数字三角形
# 题号：1002
# 语言：Python3

n = int(input())
k = 1
for i in range(1, n+1):
    for j in range(i):
        print(f"{k:4d}", end="")
        k += 1
    print()
