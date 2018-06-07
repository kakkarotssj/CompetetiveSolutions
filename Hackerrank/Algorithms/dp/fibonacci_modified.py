t0, t1, n = map(int, raw_input().split())
dp = [0] * (n)
dp[0] = t0
dp[1] = t1
for i in range(2, n):
	dp[i] = dp[i-2] + dp[i-1]*dp[i-1]

print dp[n-1]