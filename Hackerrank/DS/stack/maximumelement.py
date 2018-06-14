stack = []
maxm = 0
q = input()
for i in range(q):
	query = map(int, raw_input().split())
	if query[0] == 1:
		maxm = max(query[1], maxm)
		stack.append([query[1], maxm])
	elif query[0] == 2:
		stack.pop()
		if len(stack) == 0:
			maxm = 0
		else:
			maxm = stack[len(stack) - 1][1]
	else:
		print maxm