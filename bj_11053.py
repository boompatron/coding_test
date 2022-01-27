import sys
n = int(sys.stdin.readline().rstrip())
g = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for _ in range(n + 1)]
dp[0] = 0
g.insert(0, 0)
for i in range(1, n + 1):
    tmp = 0
    for j in range(0, i):
        if g[i] > g[j] and dp[j] + 1 > tmp:
            tmp = dp[j] + 1
    dp[i] = tmp
print(max(dp))
