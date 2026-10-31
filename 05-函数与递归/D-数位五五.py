# 题目：数位五五
# 题号：D
# 语言：Python3

x,y=map(int,input().split())
cnt=0
for i in range(x,y+1):
    a=sum(map(int,str(i)))       #数位之和
    if a%5==0:
        cnt+=1
print(cnt)
