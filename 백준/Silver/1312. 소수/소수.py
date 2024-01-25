import sys

a,b,n = map(int,sys.stdin.readline().split())

result = 0

for i in range(n):
    a = (a%b) * 10
    result = a//b

print(result)