# 题目：好串
# 题号：E
# 语言：Python3

s = input().strip()
cnt = 0
for c in s:
    if c == "a":
        cnt += 1
    elif c == "b":
        cnt -= 1
    else:
        print("Bad")
        break
    if cnt < 0:
        print("Bad")
        break
else:
    print("Good" if cnt == 0 else "Bad")
