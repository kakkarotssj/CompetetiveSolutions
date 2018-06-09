# RECURSIVE APPROACH

'''
t = input()
ans = []
def recur(curno, a, b, i):
	global ans
	if i == n:
		if curno not in ans:
			ans.append(curno)
		else:
			pass
	else:
		i += 1
		recur(curno+a, a, b, i)
		recur(curno+b, a, b, i)
for i in range(t):
	n = input()
	a = input()
	b = input()

	curno = 0
	i = 1
	ans = []
	recur(curno, a, b, i)
	for j in ans:
		print j,
	print ""
'''

# ITERATIVE APPROACH


def lastvalue(n, a, b):
	if a == b:
		print (n-1) * a
	else:
		minm = min(a, b)
		maxm = max(a, b)

		for i in range(n):
			print minm * (n-1-i) + i * maxm,
		print ""

t = input()
for i in range(t):
	n = input()
	a = input()
	b = input()
	lastvalue(n, a, b)