# 题目：四舍五入
# 题号：1001
# 语言：Python3

import sys
data = sys.stdin.read().split()
t = int(data[1])
s = "".join(data[2:])
if "." not in s:
    print(s)
else:
    dot = s.index(".")
    n = len(s)
    i = dot + 1
    while i < n and s[i] <= "4":
        i += 1
    if i == n:
        print(s)
    else:
        p = i
        while p > dot + 1 and s[p - 1] == "4" and t > 1:
            p -= 1
            t -= 1
        if p == dot + 1:
            a = list(s[:dot])
            k = len(a) - 1
            while k >= 0 and a[k] == "9":
                a[k] = "0"
                k -= 1
            if k < 0:
                a.insert(0, "1")
            else:
                a[k] = str(int(a[k]) + 1)
            print("".join(a))
        else:
            print(s[:p - 1] + str(int(s[p - 1]) + 1))
