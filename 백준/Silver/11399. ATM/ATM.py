
n = int(input())
peoples = list(map(int,input().split()))

peoples.sort()

print(sum(sum(peoples[:i]) for i in range(len(peoples) + 1)))