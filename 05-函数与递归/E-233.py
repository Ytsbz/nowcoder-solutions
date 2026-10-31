# 题目：233
# 题号：E
# 语言：Python3

import sys
data = sys.stdin.read().split()      
T = int(data[0])                    
out = []
for i in range(T):
    a = int(data[1 + 2 * i])         
    b = int(data[2 + 2 * i])
    out.append(str(a * b))           
print("\n".join(out))
