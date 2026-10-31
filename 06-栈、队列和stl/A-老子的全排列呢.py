# 题目：老子的全排列呢
# 题号：A
# 语言：Python3

from itertools import permutations
for i in permutations(range(1, 9)):
    print(*i)
