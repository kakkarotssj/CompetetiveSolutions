n =input()
s = raw_input()
k = input()
alphabets = "abcdefghijklmnopqrstuvwxyz"
d = {}
d1 = {}
for i in range(1, 27):
	d1[i] = alphabets[i-1]
for i in range(1, 27):
	d[alphabets[i-1]] = i

upper = []
for i in range(n):
	if s[i].isupper():
		upper.append(i)
		s = s.replace(s[i], s[i].lower())

for i in range(n):
	if not s[i].isalpha():
		pass
	else:
		num = d[s[i]]
		num += k
		num %= 26
		if num == 0:
			num = d[s[i]]
		s = s[:i] + s[i].replace(s[i], d1[num]) + s[i+1:]
		if i in upper:
			s = s[:i] + s[i].replace(s[i], s[i].upper()) + s[i+1:]
	
print s