g = input()
for i in range(g):
	ans = True
	n = input()
	b = list(raw_input())
	a = list(set(b))
	b.sort()
	if a.count('_') > 0:
		for j in a:
			if j != "_":
				if b.count(j) < 2:
					print "NO"
					ans = False
					break
		if ans:
			print "YES"
	else:
		for i in range(n):
			if i > 0 and i < n-1:
				if b[i] != b[i+1] or b[i] != b[i-1]:
					print "NO"
					ans = False
					break
			else:
				if i == 0 and i + 1 <= n-1:
					if b[i] != b[i+1]:
						print "NO"
						ans = False
						break
				elif i == n-1 and i-1 >= 0:
					if b[i] != b[i-1]:
						print "NO"
						ans = False
						break

		if ans:
			print "YES"