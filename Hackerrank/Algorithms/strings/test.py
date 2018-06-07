import sys
#sys.stdin=open("in","r")

l=int(raw_input())
B=raw_input()
assert l<=100 and len(B)==l
B = list(B)
ans=0
for i in range(0,len(B)-2):
	if B[i]=='0':
		if B[i+1]=='1':
			if B[i+2]=='0':
				print B[i:i+3]
				B[i+2]='1'
				ans=ans+1
			else:
				print B[i:i+2]
		else:
			print B[i:i+1]

print ans
