n, m = map(int, raw_input().split())
data = []
for i in range(n):
	data.append(raw_input())

maxm = 0
counttotal= 0
for i in range(n):
	for j in range(i+1, n):
		number = bin(int(data[i], 2) | int(data[j], 2))[2:]
		count1 = number.count('1')
		if count1 > maxm:
			maxm = count1
			counttotal = 1
		elif count1 == maxm:
			counttotal += 1


print maxm
print counttotal
