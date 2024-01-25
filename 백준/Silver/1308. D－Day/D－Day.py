import sys
import datetime

y,m,d = map(int,sys.stdin.readline().split())
first_input = datetime.date(y,m,d)
temp = datetime.date(y+1000,m,d)
y,m,d = map(int,sys.stdin.readline().split())
second_input = datetime.date(y,m,d)

if second_input >= temp:
    print("gg")
else:
    print('D'+str((first_input-second_input).days))