numbers = "0123456789"
numbers = list(numbers)
lower_case = "abcdefghijklmnopqrstuvwxyz"
lower_case = list(lower_case)
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upper_case = list(upper_case)
special_characters = "!@#$%^&*()-+"
special_characters = list(special_characters)

n = input()
string = raw_input()
len_string = len(string)
ans = 0

def is_there(n):
	for i in n:
		if i in string:
			return
	global ans
	global len_string
	ans += 1
	len_string += 1
	return

x = [numbers, lower_case, upper_case, special_characters]
for i in x:
	is_there(i)

if len_string < 6:
	ans += 6 - len_string
print ans

