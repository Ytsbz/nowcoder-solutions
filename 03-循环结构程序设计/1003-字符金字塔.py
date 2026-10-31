# 题目：字符金字塔
# 题号：1003
# 语言：Python3

x=input().strip()
y=ord(x)-ord("A")
for i in range(y+1):
    j=" "*(y-i)
    left="".join(chr(ord("A")+k) for k in range(i+1))
    right="".join(chr(ord("A")+k) for k in range(i-1,-1,-1))
    print(j+left+right)
