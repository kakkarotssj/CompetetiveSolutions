t = input()
for i in range(t):
	m = input()
	n = input()
	flavors = map(int, raw_input().split())
	countflavors = len(flavors)
	for j in range(countflavors):
		for k in range(j+1, countflavors):
			if flavors[j] + flavors[k] == m:
				print j+1, k+1
				break



