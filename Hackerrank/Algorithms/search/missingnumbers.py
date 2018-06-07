n = input()
arr1 = map(int, raw_input().split())
m = input()
arr2 = map(int, raw_input().split())

d1 = {}
d2 = {}
for num in arr1:
	try:
		d1[num] += 1
	except KeyError:
		d1[num] = 1
for num in arr2:
	try:
		d2[num] += 1
	except KeyError:
		d2[num] = 1

missing = []
d2_set_keys = list(set(d2.iterkeys()))
for key in d2_set_keys:
	try:
		if d2[key] - d1[key] >0:
			missing.append(key)
	except KeyError:
		missing.append(key)

missing.sort()
for item in missing:
	print item, 