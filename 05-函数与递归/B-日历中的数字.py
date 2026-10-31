# 题目：日历中的数字
# 题号：B
# 语言：Python3

def leap_year(y):                 #判断闰年
    if y%400==0:
        return True
    elif y%4==0 and y%100!=0:
        return True
    else:
        return False
def year_month(y,m):             #判断每月天数
    if m in (4,6,9,11):
        return 30
    if m==2:
        if leap_year(y):
            return 29
        else:
            return 28
    else:
        return 31
while True:
    try:
        y,m,x=map(int,input().split())           #输入三个整数
    except EOFError:
        break
    cnt=0
    a=str(y)+str(m).zfill(2)          #eg.201704
    for i in range(1,year_month(y,m)+1):
        j=a+str(i).zfill(2)     #eg.20170414
        cnt+=j.count(str(x))
    print(cnt)
