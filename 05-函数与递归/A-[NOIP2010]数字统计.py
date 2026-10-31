# 题目：[NOIP2010]数字统计
# 题号：A
# 语言：Python3

L,R = map(int, input().split())
b=0
for i in range(L,R+1,1):
    a=str(i).count('2')
    b+=a
print(b)
