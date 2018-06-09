import math
t = input()
values = []
times = []
n = int(math.ceil(math.log((pow(10, 12)/3), 2))) +1	# GP sum
for i in range(n):
	value = 3 * pow(2, i)
	values.append(value)
	times.append(value - 2)

for i in range(n):
	if t < times[i]:
		temp = times[i] - t
		print temp
		break
	elif t == times[i]:
		print t + 2
		break

