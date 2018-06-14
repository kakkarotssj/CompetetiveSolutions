n, m = map(int, raw_input().split())
arr = [[0, 0] for i in range(n)]
q = []
for i in range(m):
	q.append(map(int, raw_input().split()))
for i in range(m):
	arr[q[i][0]-1][1] += q[i][2]
	arr[q[i][1]-1][0] += q[i][2]
stack = 0
maxm = 0
for i in range(n):
	stack -= arr[i][0]
	temp = arr[i][0] + arr[i][1] + stack
	if temp > maxm:
		maxm = temp
	# maxmarray[i] = arr[i][0] + arr[i][1] + stack
	stack += arr[i][1]
print maxm

# n, inputs = map(int, raw_input().split())
# list = [0]*(n+1)
# for _ in range(inputs):
#     x, y, incr = map(int, raw_input().split())
#     list[x-1] += incr
#     if((y)<=len(list)): list[y] -= incr;
# max = x = 0
# for i in list:
#    x=x+i;
#    if(max<x): max=x;
# print(max)