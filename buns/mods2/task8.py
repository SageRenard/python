si = input("Введите данные через запятую и пробел:")
ind1 = si.find(", ")
s = str(si[:ind1])
i = str(si[ind1+2:])

count = 0
for j in range(len(s)):
    if s[j] == i:
        count += 1
    else:
        break

print(count)
