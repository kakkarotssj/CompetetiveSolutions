import copy
n = input()
arr = map(int, raw_input().split())
def issorted(n, arr):
	if n >= 1:
		for i in range(n-1):
			if arr[i] > arr[i+1]:
				return False
		return True
	else:
		return False
def tryswapping(n, arr):
	newarr = copy.deepcopy(arr)
	for i in range(n-1):
		if newarr[i+1] < newarr[i]:
			l = i+1
			try:
				r = newarr.index(min(newarr[i+1:])) + 1
			except ValueError:
				r = l+1
			break
	newarr[l-1], newarr[r-1] = newarr[r-1], newarr[l-1]
	if issorted(len(newarr), newarr):
		print "yes"
		print "swap", l, r
		exit()
def tryreversing(n, arr):
	newarr = copy.deepcopy(arr)
	for i in range(n-1):
		if newarr[i+1] < newarr[i]:
			l = i+1
			try:
				r = newarr.index(min(newarr[i+2:])) + 1
			except ValueError:
				r = l+1
			break
	newarr = newarr[:l-1] + newarr[r-1:l-2:-1] + newarr[r:]
	if issorted(len(newarr), newarr):
		print "yes"
		print "reverse", l, r
		exit()
issorted(n ,arr)
tryswapping(n, arr)
tryreversing(n, arr)
print "no"