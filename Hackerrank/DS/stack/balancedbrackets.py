n = input()
for i in range(n):
	s = raw_input()
	stack = []
	ok = True
	for j in s:
		if j in '[{(':
			stack.append(j)
		else:
			if len(stack) < 1:
				print "NO"
				ok = False
				break
			t = stack.pop()
			if j == ']' and t != '[':
				print "NO"
				ok= False
				break
			elif j == '}' and t != '{':
				print "NO"
				ok = False
				break
			elif j == ')' and t != '(':
				print "NO"
				ok = False
				break
	if ok and len(stack):
		print "YES"