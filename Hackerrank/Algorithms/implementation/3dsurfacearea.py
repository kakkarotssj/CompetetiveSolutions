h, w = map(int, raw_input().split())
a = []
for i in range(h):
	a.append(map(int, raw_input().split()))

area = 0
for i in range(h):
	for j in range(w):
		area += 2 * (2 * a[i][j] + 1)
		if i - 1 >= 0:
			area -= min(a[i][j], a[i-1][j])
		if i + 1 <= h-1:
			area -= min(a[i][j], a[i+1][j])
		if j - 1 >= 0:
			area -= min(a[i][j], a[i][j-1])
		if j+1 <= w-1:
			area -= min(a[i][j], a[i][j+1])

print area
