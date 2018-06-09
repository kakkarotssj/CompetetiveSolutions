# VALLEY
# RISE
# FALL 
# PEAK
import sys

n = input()
arr = []
arr.append(sys.maxsize)
for i in range(n):
	arr.append(input())
arr.append(sys.maxsize)
ans = [0] * (n+2)

# FILLING UP THE VALLEY
for i in range(n+1):
	if arr[i-1] > arr[i] < arr[i+1]:
		ans[i] = 1

# FILLING THE RISE FROM LEFT TO RIGHT
for i in range(1, n+1):
	if arr[i-1] < arr[i] <= arr[i+1]:
		ans[i] = ans[i-1] +1

# FILLING THE FALL FROM RIGHT TO LEFT
for i in range(n, 0, -1):
	if arr[i+1] >= arr[i] > arr[i-1]:
		ans[i] = ans[i+1] + 1

for i in range(1, n+1):
	if arr[i-1] < arr[i] > arr[i+1]:
		ans[i] = max(ans[i-1], ans[i+1]) + 1
print sum(ans)