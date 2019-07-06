

readfile = open('test.txt','r')
#read all characters in the file and store the count in dict
char_count = {}
for ch in readfile.read():
    if ch not in char_count:
        char_count[ch] = 0
    char_count[ch] = char_count[ch] + 1
print(char_count)

