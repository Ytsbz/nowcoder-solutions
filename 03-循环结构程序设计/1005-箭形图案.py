# 题目：箭形图案
# 题号：1005
# 语言：Python3

import sys
data = list(map(int,sys.stdin.read().split()))
for n in data:
    for i in range(1,n+1,1):
        print(" "*(2*(n-i)+2)+"*"*i)
    print("*"*(n+1))
    for i in range(n,0,-1):
        print(" "*(2*(n-i)+2)+"*"*i)
