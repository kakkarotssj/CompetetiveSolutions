n,q = map(int, raw_input().split())
seqList = [[] for i in range(n)]
lastAnswer = 0
for i in range(q):
	queryset = map(int, raw_input().split())
	x = queryset[1]
	y = queryset[2]
	if queryset[0] == 1:
		index = (x ^ lastAnswer) % n
		seqList[index].append(y)
	else:
		index = (x ^ lastAnswer) % n
		temp = y % len(seqList[index])
		value = seqList[index][temp]
		lastAnswer = value
		print lastAnswer