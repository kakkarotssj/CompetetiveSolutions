t = input()
def replace(char1, char2):
	if char1 == 'a':
		if char2 == 'b':
			return 'c'
		else:
			return 'b'
	elif char1 == 'b':
		if char2 == 'a':
			return 'c'
		else:
			return 'a'
	else:
		if char1 == 'a':
			return 'b'
		else:
			return 'a'

strings = []
for i in range(t):
	strings.append(raw_input())

for i in range(t):
	s = strings[i]
	slist = list(s)
	i = len(slist) - 1
	while i > 0:
		try:
			if slist[i] != slist[i-1]:
				replacement = replace(slist[i], slist[i-1])
				slist.insert(i-1, replacement)
				slist.pop(i)
				slist.pop(i)
			else:
				i -= 1
		except IndexError:
			if i != 0:
				i -= 1
			else:
				break

	print len(slist)
