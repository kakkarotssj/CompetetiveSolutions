n, m = map(int, raw_input().split())
stations = map(int, raw_input().split())
stations.sort()

maxm = 0
i, j =0 ,0
while i < n:
	temp1 = abs(i-stations[j])
	if temp1 == 0:
		pass
	else:
		if j != m-1:
			temp2 = abs(i-stations[j+1])
			if temp2 <= temp1:
				j += 1
				if maxm < temp2:
					maxm = temp2
			else:
				if maxm < temp1:
					maxm = temp1
		else:
			if temp1 > maxm:
				maxm = temp1
	
	i += 1

print maxm