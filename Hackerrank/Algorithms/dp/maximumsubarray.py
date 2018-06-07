t = input()
for i in range(t):
	n = input()
	numbers = map(int, raw_input().split())
	dp = [None] * len(numbers)
	dp[0] = numbers[0]
	for j in range(1, len(dp)):
		if numbers[j] + dp[j-1] > numbers[j]:
			dp[j] = dp[j-1] + numbers[j]
		else:
			dp[j] = numbers[j]

	subsequence = 0
	for num in numbers:
		if num > 0:
			subsequence += num
	if subsequence == 0:
		subsequence = max(numbers)

	# dp2 = []
	# for num in numbers:
	# 	dp2.append(num)
	# for j in range(len(dp2)):
	# 	for k in range(j):
	# 		if dp2[j] < dp2[k] + numbers[j]:
	# 			dp2[j] = dp2[k] + numbers[j]


	print max(dp), max(dp2)
