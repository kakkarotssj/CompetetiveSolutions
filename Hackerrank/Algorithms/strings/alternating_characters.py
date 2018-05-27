t = input()
for i in range(t):
    count = 0
    string = raw_input()
    string_list = list(string)
    j = 0
    while j < len(string_list) - 1:
        if string_list[j] == string_list[j+1]:
            string_list.pop(j+1)
            count += 1
        else:
            j += 1
    string = ''.join(string_list)
    print count