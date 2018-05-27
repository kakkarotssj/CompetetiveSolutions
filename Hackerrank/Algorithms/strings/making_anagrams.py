string1 = raw_input()
string2 = raw_input()
dict1 = {}
dict2 = {}
for i in string1:
	if not dict1.has_key(i):
		dict1[i] = string1.count(i)
for i in string2:
	if not dict2.has_key(i):
		dict2[i] = string2.count(i)

ans = 0
list1 = list(set(string1))
list2 = list(set(string2))
considered = []

for i in range(len(list1)):
	if list1[i] not in considered:
		if list1[i] not in list2:
			ans += dict1[list1[i]]
		else:
			ans += abs(dict1[list1[i]] - dict2[list1[i]])
		considered.append(list1[i])

for i in range(len(list2)):
	if list2[i] not in considered:
		if list2[i] not in list1:
			ans += dict2[list2[i]]
		considered.append(list2[i])

print ans
