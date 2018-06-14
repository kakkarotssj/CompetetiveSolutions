n, d = map(int, raw_input().split())
arr = map(int, raw_input().split())
arr = arr[d:] + arr[:d]
print ' '.join(map(str, arr))
# newarr = [None] * n
# for i in range(n):
# 	newarr[-(d-i)] = arr[i]
# for i in range(n):
# 	print newarr[i],