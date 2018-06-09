def recursum(p):
	if p < 10:
		return p
	else:
		p = str(p)
		numbers = []
		for i in p:
			numbers.append(int(i))
		p = sum(numbers)
		return recursum(p)



n, k = map(int, raw_input().split())
n = str(n)
p = n * k
p = int(p)

ans = recursum(p)
print ans
