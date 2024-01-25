import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    arr.append([y,x])

arr = sorted(arr)

for y,x in arr:
    print(x,y)