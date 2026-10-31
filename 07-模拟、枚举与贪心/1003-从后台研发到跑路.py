# 题目：从后台研发到跑路
# 题号：1003
# 语言：Python3

import sys
s = sys.stdin.read()
n = len(s)
out = []
i = 0
in_str = False
while i < n:
    if in_str:
        if s[i] == "\\" and i + 1 < n and s[i + 1] == '"':
            out.append('\\"')
            i += 2
            continue
        out.append(s[i])
        if s[i] == '"':
            in_str = False
        i += 1
    elif s[i] == '"':
        in_str = True
        out.append('"')
        i += 1
    elif s[i] == "\\" and i + 1 < n and s[i + 1] == '"':
        out.append('\\"')
        i += 2
    elif s[i:i + 2] == "/*":
        j = s.find("*/", i + 2)
        if j == -1:
            out.append("/*")
            i += 2
        else:
            i = j + 2
    else:
        out.append(s[i])
        i += 1
sys.stdout.write("".join(out))
