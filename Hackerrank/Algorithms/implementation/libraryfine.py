returndate = map(int, raw_input().split())
duedate = map(int, raw_input().split())
if returndate[2] < duedate[2]:
	print 0
elif returndate[2] > duedate[2]:
	print 10000
elif returndate[2] == duedate[2]:
	if returndate[1] < duedate[1]:
		print 0
	elif returndate[1] > duedate[1]:
		print 500 * (returndate[1] - duedate[1])
	elif returndate[1] == duedate[1]:
		if returndate[0] <= duedate[0]:
			print 0
		elif returndate[0] > duedate[0]:
			print 15 * (returndate[0] - duedate[0])
