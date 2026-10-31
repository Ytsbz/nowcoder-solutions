# 题目：安卓图案解锁
# 题号：1002
# 语言：Python3

import sys
mid = {"13":"2","31":"2","17":"4","71":"4","39":"6","93":"6",
       "79":"8","97":"8","19":"5","91":"5","28":"5","82":"5",
       "37":"5","73":"5","46":"5","64":"5"}
for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    ok = len(s) <= 9 and len(set(s)) == len(s)
    used = set()
    for i in range(len(s)):
        if i > 0:
            m = mid.get(s[i-1] + s[i])
            if m and m not in used:
                ok = False
                break
        used.add(s[i])
    print("YES" if ok else "NO")
