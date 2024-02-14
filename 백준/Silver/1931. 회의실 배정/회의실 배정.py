import sys


n = int(input())

time_list = []

for _ in range(n):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    time_list.append([s,e])

time_list.sort(key=lambda x: (x[1], x[0]))

temp = 0
answer = 0
for start,end in time_list:
    if temp <= start:
        answer += 1
        temp = end
print(answer)