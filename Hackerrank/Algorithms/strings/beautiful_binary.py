n = input()
B = raw_input()
cnt = 0
i = 0
while i < n:
	print i
	if B[i: i + 3] == "010":
		cnt += 1
		i += 2
	i += 1
print cnt
