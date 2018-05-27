import sys

string = raw_input()
list_string = list(string)
set_string = set(string)

odd_count = 0
for i in set_string:
	if list_string.count(i) % 2 != 0:
		odd_count += 1
		if odd_count > 1:
			print "NO"
			sys.exit()

print "YES"
