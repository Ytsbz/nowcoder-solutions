# 题目：C Simple math problem
# 题号：E
# 语言：Python3
X,Y=map(int,input().split())
if Y%X==0:
    Z=X+Y
    print(Z)
else:
    Z=Y-X
    print(Z)
