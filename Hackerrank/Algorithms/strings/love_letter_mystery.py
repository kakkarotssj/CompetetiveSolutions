q = input()
strings = []
for i in range(q):
    strings.append(raw_input())


def find_count(string):
    string_length = len(string)
    count = 0
    if string_length % 2 == 0:
        mid_index = (string_length / 2)
        for j in range(0, string_length/2):
            count += abs(ord(string[mid_index + j]) - ord(string[mid_index - j - 1]))
    else:
        mid_index = (string_length - 1) / 2
        for j in range(1, string_length/2 + 1):
            count += abs(ord(string[mid_index + j]) - ord(string[mid_index - j]))

    return count


for i in range(q):
    count = find_count(strings[i])
    print count
