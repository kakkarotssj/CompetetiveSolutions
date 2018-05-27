n = input()
strings = []
for i in range(n):
    strings.append(raw_input())

for i in range(n):
    count = 0
    string = strings[i]
    new_string = ""
    k = 0
    while len(new_string) < len(string):
        if len(new_string) == 0:
            new_string = string[0]
            count += 1
            k += 1
        else:
            if string[k] in new_string:
                j = k
                while j < len(string):
                    if string[k:j+1] in new_string:
                        j += 1
                    else:
                        break
                new_string += string[k:j]
                k = j
            else:
                new_string += string[k]
                count += 1
                k += 1

    print count
