# 题目：乘法表
# 题号：1005
# 语言：Python3
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i:2d}",end=" ")
        j+=1
    print()         
    i+=1
