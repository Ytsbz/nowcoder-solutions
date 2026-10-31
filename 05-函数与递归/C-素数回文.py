# 题目：素数回文
# 题号：C
# 语言：Python3

t=int(input())
b=int(str(t)+str(t)[::-1][1:])
if b<2:
    print("noprime")
else:
    for j in range(2,int(b**0.5)+1):
        if b%j==0:
            print("noprime")
            break
    else:
        print("prime")
