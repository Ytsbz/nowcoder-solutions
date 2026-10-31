# 题目：比较月亮大小
# 题号：1005
# 语言：Python3

n=int(input())
nums = list(map(int, input().split()))[:n]
a=nums[-1]
if a==0:
    print("UP")
elif a==15:
    print("DOWN")
elif n==1:
    print("-1")
elif a>nums[-2]:
    print("UP")
else:
    print("DOWN")
