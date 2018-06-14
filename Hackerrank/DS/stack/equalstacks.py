n1, n2, n3 = map(int, raw_input().split())
s1 = map(int, raw_input().split())
s1.reverse()
s2 = map(int, raw_input().split())
s2.reverse()
s3 = map(int, raw_input().split())
s3.reverse()
lens1, sum1 = len(s1), sum(s1)
lens2, sum2 = len(s2), sum(s2)
lens3, sum3 = len(s3), sum(s3)

while sum1 != sum2 or sum1 != sum3 or sum2 != sum3:
	if sum1 >= sum2 and sum1 >= sum3:
		sum1 -= s1.pop()
	elif sum2 >= sum1 and sum2 >= sum3:
		sum2 -= s2.pop()
	elif sum3 >= sum1 and sum3 >= sum2:
		sum3 -= s3.pop()
	sum1 = sum(s1)
	sum2 = sum(s2)
	sum3 = sum(s3)

print sum1

