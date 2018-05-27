n = input()
strings = []
collection = []
for i in range(n):
	string = raw_input()
	if i == 0:
		collection = list(set(string))
	else:
		string_list = list(set(string))
		j = 0
		while j < len(collection):
			if collection[j] not in string_list:
				collection.pop(j)
			else:
				j += 1

print len(collection)
