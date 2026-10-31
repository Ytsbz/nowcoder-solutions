# 题目：装进肚子
# 题号：B
# 语言：Python3

n,k=map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total = sum(b)          # 先假设全部晚上吃
diff = []               
for i in range(n):
    diff.append(a[i] - b[i])
diff.sort(reverse=True) 

print(total + sum(diff[:k]))
