import sys

n = int(input())

dp = []

for i in range(n):
    dp.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][0] += dp[i-1][0]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[n-1]))