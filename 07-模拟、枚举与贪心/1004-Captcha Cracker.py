# 题目：Captcha Cracker
# 题号：1004
# 语言：Python3

t = int(input())
for _ in range(t):
    s = input().strip()
    out = ""
    i = 0
    while i < len(s):
        if s[i] in "02469":
            out += s[i]
            i += 1
        elif s.startswith("zero", i):
            out += "0"; i += 4
        elif s.startswith("two", i):
            out += "2"; i += 3
        elif s.startswith("four", i):
            out += "4"; i += 4
        elif s.startswith("six", i):
            out += "6"; i += 3
        elif s.startswith("nine", i):
            out += "9"; i += 4
        else:
            i += 1
    print(out)
