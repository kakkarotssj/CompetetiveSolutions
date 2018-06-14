# n = input()
# strings = []
# for i in range(n):
# 	strings.append(raw_input())
# q = input()
# queries = []
# for i in range(q):
# 	queries.append(strings.count(raw_input()))
# for i in range(q):
# 	print queries[i]

from collections import defaultdict
n = input()
d = defaultdict(int)
for i in range(n):
	d[raw_input()] += 1
q = input()
for i in range(q):
	print d[raw_input()]
print d