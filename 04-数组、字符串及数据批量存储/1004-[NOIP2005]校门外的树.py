# 题目：[NOIP2005]校门外的树
# 题号：1004
# 语言：Python3

L,M = map(int,input().split())
trees = [True] * (L + 1)
for n in range(M):
    left,right = map(int,input().split())
    for i in range(left,right + 1):
        trees[i] = False
sum = trees.count(True)
print(sum)
