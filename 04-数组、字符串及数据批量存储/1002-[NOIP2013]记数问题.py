# 题目：[NOIP2013]记数问题
# 题号：1002
# 语言：Python3

n, x = map(int, input().split())
j=0
for i in range(1,n+1):
    for a in str(i):
        if a==str(x):
            j+=1
print(j)
