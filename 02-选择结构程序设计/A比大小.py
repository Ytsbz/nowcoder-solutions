# 题目：比大小
# 题号：A
# 语言：Python3
a,b=map(int,input().split())
if a<b:
    print("<")
elif a==b:
    print("=")
elif a>b:
    print(">")
