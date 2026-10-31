# 题目：上下金字塔
# 题号：1001
# 语言：Python3

import sys
for s in sys.stdin.read().split():
    n=int(s)
    for i in range(1,n+1,1):
        print(' '*(n-i), '*'*(2*i-1),sep='')
    for i in range(n-1,0,-1):
        print(' '*(n-i), '*'*(2*i-1),sep='')
