n = input()
queries = []
for i in range(n):
	q = map(int, raw_input().split())
	queries.append(q)
queue = []
for i in range(n):
	if queries[i][0] == 1:
		queue.append(queries[i][1])
	elif queries[i][0] == 2:
		queue.pop(0)
	else:
		print queue[0]