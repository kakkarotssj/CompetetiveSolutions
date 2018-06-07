t = input()
for i in range(t):
	n = input()
	arr = map(int, raw_input().split())
	if n == 1:
		print "YES"
		continue
	if n == 2:
		print "NO"
		continue
	dp = [arr[0]]
	summation = sum(arr)
	for j in range(1, n):
		if j == n-1:
			print "NO"
			break
		elif dp[j-1] == summation - dp[j-1] - arr[j]:
			print "YES"
			break
		else:
			dp.append(dp[j-1] + arr[j])