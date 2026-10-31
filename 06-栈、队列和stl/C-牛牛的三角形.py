# 题目：牛牛的三角形
# 题号：C
# 语言：Python3

n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        print(a[i], a[i + 1], a[i + 2])
        break
else:
    print("No solution")
