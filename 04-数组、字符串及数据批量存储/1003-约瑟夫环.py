# 题目：约瑟夫环
# 题号：1003
# 语言：Python3

n, k, m = map(int, input().split())
new = list(range(n))          
i = k                         
for _ in range(n - 1):        
    for a in range(1, m + 1):
        if a == m:
            new.pop(i)       
            if i == len(new): 
                i = 0
        else:
            i += 1            
            if i == len(new):
                i = 0
print(new[0])
