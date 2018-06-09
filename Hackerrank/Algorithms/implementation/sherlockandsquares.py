import math

t = input()
for i in range(t):
	a, b = map(int, raw_input().split())

	l = int(math.ceil(math.sqrt(a)))
	h = int(math.floor(math.sqrt(b)))
	
	ans = 0
	for j in range(l, h+1):
		temp = j * j
		if a <= temp <= b:
			ans += 1

	print ans
