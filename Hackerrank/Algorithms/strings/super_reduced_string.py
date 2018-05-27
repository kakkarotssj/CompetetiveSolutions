string = raw_input()

string_list = list(string)
i = 0
while i < len(string_list):
    if i < 0:
        i += 1
        continue
    if i != len(string_list) - 1:
        if string_list[i] == string_list[i+1]:
            string_list.pop(i)
            string_list.pop(i)
            string = ''.join(string_list)
            i -= 2
            found = True
    i += 1

if len(string) == 0:
    print "Empty String"
else:
    print string
