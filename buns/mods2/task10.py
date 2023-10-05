string = input()
word = ""
for i in range(len(string)):
    if string[i]==' ':
        word += string[i-1]
word += string[len(string)-1]
print(word)
